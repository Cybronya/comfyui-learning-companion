# VHS_LoadVideoFFmpegPath

## 节点类型

`VHS_LoadVideoFFmpegPath`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `meta_batch:VHS_BatchManager`（1 次）
- `vae:VAE`（1 次）
- `video:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `audio:AUDIO`（1 次）
- `video_info:VHS_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"custom_height": 0, "custom_width": 0, "force_rate": 0, "format": "AnimateDiff", "frame_load_cap": 0, "start_time": 0, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
