# LLava Loader Simple

## 节点类型

`LLava Loader Simple`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CUSTOM`（2 次）
- `ckpt_name:COMBO`（2 次）
- `max_ctx:INT`（2 次）
- `gpu_layers:INT`（2 次）
- `n_threads:INT`（2 次）

## 输出

- `model:CUSTOM`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["llava-v1.6-mistral-7b.Q5_K_M.gguf", 2924, 27, 8]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
