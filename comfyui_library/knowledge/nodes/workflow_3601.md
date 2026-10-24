# workflow>不要动

## 节点类型

`workflow>不要动`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（1 次）
- `pixels:IMAGE`（1 次）
- `ReferenceLatent conditioning:CONDITIONING`（1 次）
- `samples:LATENT`（1 次）
- `image_1:IMAGE`（1 次）
- `vae_name:COMBO`（1 次）
- `guidance:FLOAT`（1 次）
- `inputcount:INT`（1 次）
- `direction:COMBO`（1 次）
- `match_image_size:BOOLEAN`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `LATENT:LATENT`（1 次）
- `FluxGuidance CONDITIONING:CONDITIONING`（1 次）
- `IMAGE:IMAGE`（1 次）
- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ae.sft", 2.5, 2, "right", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
