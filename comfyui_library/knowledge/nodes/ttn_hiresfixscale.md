# ttN hiresfixScale

## 节点类型

`ttN hiresfixScale`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:VAE`（1 次）
- `image:IMAGE`（1 次）
- `model_name:COMBO`（1 次）
- `rescale_after_model:COMBO`（1 次）
- `rescale_method:COMBO`（1 次）
- `rescale:COMBO`（1 次）
- `percent:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `longer_side:INT`（1 次）

## 输出

- `latent:LATENT`（1 次）
- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1x-ITF-SkinDiffDetail-Lite-v1.pth", true, "nearest-exact", "by percentage", 50, 1024, 1024, 1024, "disabled", "Hide", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
