# Flux3PELoader

## 节点类型

`Flux3PELoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model_name:COMBO`（8 次）
- `context_size:INT`（8 次）
- `backend:COMBO`（8 次）

## 输出

- `pe_model:FLUX3_PE_MODEL`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux3-klein-pup-Q4_K_M.gguf", 8192, "llama-cpp-python"]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
