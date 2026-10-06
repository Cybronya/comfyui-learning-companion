# llama_cpp_parameters

## 节点类型

`llama_cpp_parameters`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 28 个 workflow 中。

## 输入

- `max_tokens:INT`（33 次）
- `top_k:INT`（33 次）
- `top_p:FLOAT`（33 次）
- `min_p:FLOAT`（33 次）
- `typical_p:FLOAT`（33 次）
- `temperature:FLOAT`（33 次）
- `repeat_penalty:FLOAT`（33 次）
- `frequency_penalty:FLOAT`（33 次）
- `present_penalty:FLOAT`（33 次）
- `mirostat_mode:INT`（33 次）

## 输出

- `parameters:LLAMACPPARAMS`（33 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4096, 30, 0.9, 0.05, 1, 0.8, 1, 0, 1, 0, 0.1, 5, -1]`（10 次）
- `[1024, 30, 0.9, 0.05, 1, 0.8, 1, 0, 1, 0, 0.1, 5, -1]`（5 次）
- `[768, 30, 0.9, 0.05, 1, 0.4, 1, 0, 0, 0, 0.1, 5, -1]`（5 次）
- `[4096, 30, 0.9, 0.05, 1, 0.8, 1, 0, 0, 0, 0.1, 5, -1]`（3 次）
- `[4096, 1, 0.7000000000000002, 0.05000000000000001, 0, 0.22000000000000003, 1.0500000000000003, 0.12000000000000002, 0.20`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
