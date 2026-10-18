# YuE2ModelLoader

## 节点类型

`YuE2ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `backend:COMBO`（1 次）
- `memory_budget_gib:FLOAT`（1 次）
- `offload_ar:BOOLEAN`（1 次）
- `model_loading:COMBO`（1 次）
- `nar_attention:COMBO`（1 次）
- `nar_query_chunk_size:INT`（1 次）

## 输出

- `model:YUE2_MODEL`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["torch-eager", 23.5, true, "auto", "sdpa", 256]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
