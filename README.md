# simpliset

as i implemented two script for this assignment 1st one shiva.ipynb file relatively slow in size and token genreation is also slow in 1st one as problem statement said to optimise llm so i fine-tuned the llm of mistral 7b and try to run it but it is relatively very slow so 

# 1st inference script shiva.ipynb
 I fine-tuned the Mistral 7 billion parameter model using Auto Train and Hugging Face. First, I installed the necessary libraries and set up Auto Train. Then, I authenticated the notebook with Hugging Face and prepared a training dataset. Using Auto Train, I specified the project name and model name for fine-tuning. The model was fine-tuned using LoRA and the adapted was uploaded to the Hugging Face Model Hub. Finally, I ran inference on the fine-tuned model to generate text. However, due to limited training data and training loss not decreasing significantly, the model's performance was not optimal. To improve performance, I suggested improving the training data, LoRA layers, and increasing the training size.

 # 2nd inference script shiva.ipynb

 AWQ - 4-bit quantized model on a single GPU

vLLM supports AWQ (Activation-aware Weight Quantization for LLM Compression and Acceleration) for serving 4-bit quantized models. Quantization involves decreasing the model's precision from FP16 to INT4, leading to a significant reduction in file size, approximately by 70%. This results in advantages such as reduced latency and lower memory usage.

To initialize Mistral-7B 4-bit quantized model, we will use "TheBloke/Mistral-7B-v0.1-AWQ", set dtype to torch.float16, and the quantization argument to AWQ.

i achieved a speed 2.78 times faster with a single GPU through quantization. This saves costs and memory, enabling us to batch more requests and process them in parallel . 