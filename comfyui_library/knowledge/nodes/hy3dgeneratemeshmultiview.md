# Hy3DGenerateMeshMultiView

## 节点类型

`Hy3DGenerateMeshMultiView`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:HY3DMODEL`（1 次）
- `front:IMAGE`（1 次）
- `left:IMAGE`（1 次）
- `right:IMAGE`（1 次）
- `back:IMAGE`（1 次）

## 输出

- `latents:HY3DLATENT`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[5.5, 30, 416935455784444, "fixed", "FlowMatchEulerDiscreteScheduler"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
