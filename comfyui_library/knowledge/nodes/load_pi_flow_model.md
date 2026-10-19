# Load pi-Flow Model

## 节点类型

`Load pi-Flow Model`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `lora_name:COMBO`（1 次）
- `adapter_strength:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux2_dev_fp8mixed.safetensors", "default", "flux2-pi-4steps.safetensors", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
