# TextEncodeQwenImageEditPlusCustom_lrzjason

## 节点类型

`TextEncodeQwenImageEditPlusCustom_lrzjason`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）
- `vae:VAE`（6 次）
- `configs:LIST`（6 次）
- `prompt:STRING`（6 次）
- `return_full_refs_cond:BOOLEAN`（6 次）
- `instruction:STRING`（6 次）

## 输出

- `conditioning:CONDITIONING`（6 次）
- `latent:LATENT`（6 次）
- `custom_output:ANY`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["溶图,纠正产品透视角度和光影并使产品融入背景", true, "Describe the key features of the input image (color, shape, size, texture, objects, ba`（3 次）
- `["将图1中的角色移至图2中，并调整为与图2角色相似的姿势。保持图1角色的外貌特征一致性，重新进行光线处理，使其与图2场景的光线和整体氛围自然融合，确保无明显人工痕迹。", true, "Describe the key features `（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
