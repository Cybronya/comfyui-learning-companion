# workflow>Pre-FIX

## 节点类型

`workflow>Pre-FIX`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `image:IMAGE`（1 次）
- `ImageToMask image:IMAGE`（1 次）
- `pixels:IMAGE`（1 次）
- `ttN text text:STRING`（1 次）
- `clip_name1:COMBO`（1 次）
- `clip_name2:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `style_model_name:COMBO`（1 次）

## 输出

- `VAE:VAE`（1 次）
- `show_help:STRING`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["clip_l.safetensors", "sd3/t5xxl_fp16.safetensors", "flux", "default", "flex1_redux_siglip2_512.safetensors", "ae.safet`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
