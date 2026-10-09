# MiniMaxH3Director

## 节点类型

`MiniMaxH3Director`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `video_vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `clip:CLIP`（1 次）
- `i2v_groups:MMX_DIR_GROUP`（1 次）
- `r2v_groups:MMX_DIR_GROUP`（1 次）
- `selflift:MMX_DIR_SELFLIFT`（1 次）
- `refine:MMX_DIR_REFINE`（1 次）
- `face_refine:MMX_DIR_FACE_REFINE`（1 次）
- `sigmas:SIGMAS`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `fps:FLOAT`（1 次）
- `frame_count:INT`（1 次）
- `source_images:IMAGE`（1 次）
- `report:STRING`（1 次）
- `images_pre_refine:IMAGE`（1 次）
- `images_pre_face_refine:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["i2v — 图生视频(Image to Video)", "", "采样设置", 1, 666, "fixed", 24, 576, 736, 736, 124, "{\"version\":5,\"editMode\":\"segme`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
