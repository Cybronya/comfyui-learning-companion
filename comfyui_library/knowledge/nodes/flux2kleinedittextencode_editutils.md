# Flux2KleinEditTextEncode_EditUtils

## 节点类型

`Flux2KleinEditTextEncode_EditUtils`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `prompt:STRING`（2 次）
- `ref_longest_edge:INT`（2 次）

## 输出

- `conditioning:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `custom_output:ANY`（2 次）
- `main_image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["High definition, 4K, Add realistic details to the corrupted image, Restore high frequence details from the corrupted i`（1 次）
- `["High definition, 4K, Add realistic details to the corrupted image, Restore high frequence details from the corrupted i`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
