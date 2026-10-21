# MiniMaxH3StillDecodeT8

## 节点类型

`MiniMaxH3StillDecodeT8`

## 分类

Decoding

## 作用

解码类节点：把编码数据还原（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `av_latent:LATENT`（3 次）
- `video_vae:VAE`（3 次）
- `frame_selection:COMBO`（3 次）
- `frame_index:INT`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `candidate_frames:IMAGE`（3 次）
- `report_json:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["middle", 0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
