# workflow>大模型+

## 节点类型

`workflow>大模型+`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `text:STRING`（5 次）
- `width:INT`（4 次）
- `height:INT`（4 次）
- `CLIPTextEncode text:STRING`（1 次）

## 输出

- `模型:MODEL`（5 次）
- `VAE:VAE`（5 次）
- `Latent:LATENT`（5 次）
- `条件:CONDITIONING`（5 次）
- `CLIPTextEncode 条件:CONDITIONING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["SDXL-Anime _  天空之境 _v3.1.safetensors", 768, 1024, 1, "Depth of field, blurry street background,photo of a cyberpunk ba`（1 次）
- `["ReVAnimated_v122_V122.safetensors", 768, 1024, 1, "Depth of field, blurry street background,photo of a cyberpunk barba`（1 次）
- `["hellokid2d_V152g.safetensors", 768, 1024, 1, "", ""]`（1 次）
- `["LEOSAM HelloWorld 新世界 - V7.safetensors", 768, 1024, 1, "Depth of field, blurry street background,photo of a cyberpunk `（1 次）
- `["awpainting_v14.safetensors", 768, 1024, 1, "Depth of field, blurry street background,photo of a cyberpunk barbarian Ba`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
