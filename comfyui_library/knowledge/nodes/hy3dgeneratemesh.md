# Hy3DGenerateMesh

## 节点类型

`Hy3DGenerateMesh`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipeline:HY3DMODEL`（2 次）
- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `guidance_scale:FLOAT`（2 次）
- `steps:INT`（2 次）
- `seed:INT`（2 次）
- `scheduler:COMBO`（2 次）
- `force_offload:BOOLEAN`（2 次）

## 输出

- `latents:HY3DLATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[5.5, 50, 123, "fixed", "FlowMatchEulerDiscreteScheduler", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
