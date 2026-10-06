# LoadWanVideoT5TextEncoder

## 节点类型

`LoadWanVideoT5TextEncoder`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `wan_t5_model:WANTEXTENCODER`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.1/umt5-xxl-enc-bf16.safetensors", "bf16", "offload_device", "disabled"]`（1 次）
- `["umt5-xxl-enc-bf16.safetensors", "bf16", "offload_device", "disabled"]`（1 次）
- `["umt5-xxl-enc-bf16.safetensors", "bf16", "offload_device"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
