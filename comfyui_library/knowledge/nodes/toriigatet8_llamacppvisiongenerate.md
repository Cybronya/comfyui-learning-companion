# ToriiGateT8_LlamaCppVisionGenerate

## 节点类型

`ToriiGateT8_LlamaCppVisionGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `local_model_path:COMBO`（1 次）
- `local_mmproj_path:COMBO`（1 次）
- `chat_handler:COMBO`（1 次）
- `n_ctx:INT`（1 次）
- `n_gpu_layers:INT`（1 次）
- `n_threads:INT`（1 次）
- `keep_model_alive:BOOLEAN`（1 次）
- `verbose:BOOLEAN`（1 次）

## 输出

- `caption:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["models/LLM/ToriiGate-0.5-Q8_0.gguf", "models/LLM/ToriiGate-0.5-Q8_0.mmproj.gguf", "auto", 8192, -1, 0, false, false, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
