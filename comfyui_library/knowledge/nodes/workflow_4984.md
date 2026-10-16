# workflow>参数调整组

## 节点类型

`workflow>参数调整组`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `模型:MODEL`（5 次）
- `clip:CLIP`（5 次）
- `vae:VAE`（5 次）
- `first_frame:IMAGE`（5 次）
- `last_frame:IMAGE`（5 次）
- `images:IMAGE`（5 次）
- `audio:AUDIO`（5 次）
- `aspect_ratio:COMBO`（5 次）
- `megapixels:FLOAT`（5 次）
- `multiple:INT`（5 次）

## 输出

- `FLOAT:FLOAT`（5 次）
- `噪波生成:NOISE`（5 次）
- `Sigmas:SIGMAS`（5 次）
- `positive:CONDITIONING`（5 次）
- `LATENT:LATENT`（5 次）
- `VIDEO:VIDEO`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["16:9 (Widescreen)", 0.4, 32, 5, 5, "increment", "simple", 20, 1, "Strictly preserve the original composition, architec`（2 次）
- `["16:9 (Widescreen)", 0.4, 32, 10, 5, "increment", "simple", 20, 1, "{ \"scene_description\": \"A futuristic rider escap`（1 次）
- `["16:9 (Widescreen)", 0.4, 32, 12, 6, "increment", "simple", 20, 1, "{\n\n  \"shot_id\": 1,\n\n  \"duration\": 3,\n\n  \`（1 次）
- `["9:16 (Portrait Widescreen)", 1, 32, 2, 6, "increment", "simple", 20, 1, "0‑2 秒【0‑2s】：沿用参考图人物作为视频首帧，美丽的东亚年轻女生，黑色蓬松长卷发，精`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
