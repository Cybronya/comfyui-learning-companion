# LTXVAudioVideoMask

## 节点类型

`LTXVAudioVideoMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `video_latent:LATENT`（3 次）
- `audio_latent:LATENT`（3 次）
- `video_fps:FLOAT`（3 次）
- `video_start_time:FLOAT`（3 次）
- `video_end_time:FLOAT`（3 次）
- `audio_start_time:FLOAT`（3 次）
- `audio_end_time:FLOAT`（3 次）
- `max_length:COMBO`（3 次）
- `existing_mask_mode:COMBO`（3 次）

## 输出

- `video_latent:LATENT`（3 次）
- `audio_latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 0, 15, 0, 15, "pad", "add"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
