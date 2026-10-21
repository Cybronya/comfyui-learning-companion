# Krea2StyleSemanticFusion

## 节点类型

`Krea2StyleSemanticFusion`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `style_image:IMAGE`（2 次）
- `target_image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `style_strength:COMBO`（2 次）
- `vision_resolution:INT`（2 次）
- `custom_instruction:STRING`（2 次）

## 输出

- `条件:CONDITIONING`（2 次）
- `目标Latent:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a young girl in a red coat standing in a crowded subway station corridor, commuters around her, overhead fluorescent l`（1 次）
- `["", "轻微", 512, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
