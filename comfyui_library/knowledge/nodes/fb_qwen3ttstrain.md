# FB_Qwen3TTSTrain

## 节点类型

`FB_Qwen3TTSTrain`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `init_model:COMBO`（3 次）
- `tokenizer:COMBO`（3 次）
- `audio_folder:STRING`（3 次）
- `speaker_name:STRING`（3 次）
- `test_text:STRING`（3 次）
- `language:COMBO`（3 次）
- `learning_rate:FLOAT`（3 次）
- `num_epochs:INT`（3 次）
- `batch_size:INT`（3 次）
- `gradient_accumulation_steps:INT`（3 次）

## 输出

- `custom_speaker:CUSTOM_SPEAKER`（3 次）
- `model_path:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen/Qwen3-TTS-12Hz-1.7B-Base", "Qwen/Qwen3-TTS-Tokenizer-12Hz", "", "new_speaker", "Hello, this is a test of my new v`（1 次）
- `["Qwen/Qwen3-TTS-12Hz-1.7B-Base", "Qwen/Qwen3-TTS-Tokenizer-12Hz", "", "", "new_speaker", "Hello, this is a test of my n`（1 次）
- `["Qwen/Qwen3-TTS-12Hz-1.7B-Base", "Qwen/Qwen3-TTS-Tokenizer-12Hz", "", "zhenzhen", "Hello, this is a test of my new voic`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
