# VoiceBridgeASRLoader

## 节点类型

`VoiceBridgeASRLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `repo_id:COMBO`（3 次）
- `precision:COMBO`（3 次）
- `attention:COMBO`（3 次）
- `max_new_tokens:INT`（3 次）
- `forced_aligner:COMBO`（3 次）

## 输出

- `model_key:MODEL_KEY`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen/Qwen3-ASR-1.7B", "bf16", "flash_attention_2", 1024, "Qwen/Qwen3-ForcedAligner-0.6B"]`（2 次）
- `["Qwen/Qwen3-ASR-1.7B", "bf16", "flash_attention_2", 1024, "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
