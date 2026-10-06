# MiniMaxH3ImageToVideo

## 节点类型

`MiniMaxH3ImageToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `clip:CLIP`（18 次）
- `vae:VAE`（18 次）
- `first_frame:IMAGE`（18 次）
- `last_frame:IMAGE`（18 次）
- `prompt:STRING`（18 次）
- `width:INT`（18 次）
- `height:INT`（18 次）
- `length:INT`（18 次）

## 输出

- `positive:CONDITIONING`（18 次）
- `LATENT:LATENT`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1344, 1008, 22]`（10 次）
- `["Vaporwave title sequence look: pink and blue gradient palette, VHS tracking artifacts, Greek statue motifs, chrome pal`（6 次）
- `["integrated_multimodal_description:\n\n[Shot 1] A single continuous 12-second cinematic fantasy-realism shot inside a b`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
