# workflow>Load Models/加载模型

## 节点类型

`workflow>Load Models/加载模型`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输出

- `VAE:VAE`（1 次）
- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.safetensors", "svdq-int4_r32-flux.1-kontext-dev.safetensors", 0, "nunchaku-fp16", "auto", 0, "bfloat16", "enabled",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
