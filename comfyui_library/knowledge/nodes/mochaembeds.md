# MochaEmbeds

## 节点类型

`MochaEmbeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `vae:WANVAE`（2 次）
- `input_video:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `ref1:IMAGE`（2 次）
- `ref2:IMAGE`（2 次）
- `force_offload:BOOLEAN`（2 次）
- `tiled_vae:BOOLEAN`（2 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false]`（1 次）
- `[832, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
