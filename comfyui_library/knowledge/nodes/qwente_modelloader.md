# QwenTE_ModelLoader

## 节点类型

`QwenTE_ModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型系列:COMBO`（1 次）
- `主模型:COMBO`（1 次）
- `视觉投影mmproj:COMBO`（1 次）
- `启用思考:BOOLEAN`（1 次）
- `保留历史think:BOOLEAN`（1 次）
- `上下文长度:INT`（1 次）
- `GPU层数:INT`（1 次）
- `KV缓存K类型:COMBO`（1 次）
- `KV缓存V类型:COMBO`（1 次）
- `MoE专家上CPU:BOOLEAN`（1 次）

## 输出

- `qwen模型:QWENLLAMA`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.5-VL", "Qwen3.5-4B-Q4_K_M.gguf", "Qwen3.5-4B-mmproj-BF16.gguf", false, false, 23296, -1, "默认(F16)", "默认(F16)", f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
