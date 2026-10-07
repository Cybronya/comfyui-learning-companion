# LoadFramePackModel

## 节点类型

`LoadFramePackModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `compile_args:FRAMEPACKCOMPILEARGS`（1 次）
- `lora:FPLORA`（1 次）

## 输出

- `model:FramePackMODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["FramePackI2V_HY_fp8_e4m3fn.safetensors", "bf16", "fp8_e4m3fn", "sdpa", "sdpa"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
