# DownloadAndLoadHyVideoTextEncoder

## 节点类型

`DownloadAndLoadHyVideoTextEncoder`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llm_model:COMBO`（1 次）
- `clip_model:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `apply_final_norm:BOOLEAN`（1 次）
- `hidden_state_skip_layer:INT`（1 次）
- `quantization:COMBO`（1 次）
- `load_device:COMBO`（1 次）

## 输出

- `hyvid_text_encoder:HYVIDTEXTENCODER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Kijai/llava-llama-3-8b-text-encoder-tokenizer", "openai/clip-vit-large-patch14", "fp16", false, 2, "bnb_nf4", "offload`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
