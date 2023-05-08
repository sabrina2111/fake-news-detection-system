import torch
from transformers import BertTokenizer
from transformers import BertForSequenceClassification


def preprocess_input(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    # 建立第一個句子的 BERT tokens 並加入分隔符號 [SEP]
    word_pieces = ["[CLS]"]
    tokens = tokenizer.tokenize(text)
    word_pieces += tokens + ["[SEP]"]
    text_len = len(word_pieces)
    
    # 將整個 token 序列轉換成索引序列
    ids = tokenizer.convert_tokens_to_ids(word_pieces)
    tokens_tensor = torch.tensor(ids, dtype=torch.long).unsqueeze(0)
    
    # 將第一句包含 [SEP] 的 token 位置設為 0，其他為 1 表示第二句
    segments_tensor = torch.tensor([0] * text_len, dtype=torch.long).unsqueeze(0)
    
    # mask tensor
    masks_tensors = torch.ones(text_len, dtype=torch.long).unsqueeze(0)

    return (tokens_tensor, segments_tensor, masks_tensors)

def detect(data):
    model = BertForSequenceClassification.from_pretrained("bert-base-chinese", 
                                                          num_labels = 2, 
                                                          output_attentions = False, 
                                                          output_hidden_states = False) 
    device = torch.device("cpu")
    model.to(device)
    model.load_state_dict(torch.load("rumor_detector_model_weights.pth", map_location=torch.device('cpu')))

    model.eval()
    
    tokens_tensor, segments_tensor, masks_tensors = data  
    
    with torch.no_grad():
        output = model(tokens_tensor, 
                   token_type_ids = segments_tensor, 
                   attention_mask = masks_tensors,
                   return_dict=True)
    
    logits = output.logits
    prediction = torch.argmax(logits).to(device)
    
    if prediction == 0:
        return "經過模型檢測這可能是假資訊！"
    else:
        return "經過模型檢測這可能是真實資訊！"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


