# Load Lora

## 节点类型

`Load Lora`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `lora_name:COMBO`（1 次）
- `strength_model:FLOAT`（1 次）
- `strength_clip:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `NAME_STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["turbo加速.safetensors", 1, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
