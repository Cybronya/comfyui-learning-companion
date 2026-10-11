# LlamaServeDocLoader

## 节点类型

`LlamaServeDocLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:COMBO`（2 次）
- `mmproj:COMBO`（2 次）
- `context_length:INT`（2 次）
- `gpu_layers:INT`（2 次）
- `flash_attention:COMBO`（2 次）
- `cache_type_k:COMBO`（2 次）
- `cache_type_v:COMBO`（2 次）
- `backend:COMBO`（2 次）

## 输出

- `server_config:LLAMA_SERVER_CONFIG`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen2.5-Omni-7B-H3-Prompt-Rewriter-Q8_0.gguf", "mmproj-Qwen2.5-Omni-7B-F16.gguf", 32768, -1, "on", "q8_0", "q8_0", "au`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
