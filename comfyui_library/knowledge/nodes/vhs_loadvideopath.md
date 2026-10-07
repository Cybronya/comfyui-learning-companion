# VHS_LoadVideoPath

## 节点类型

`VHS_LoadVideoPath`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `meta_batch:VHS_BatchManager`（5 次）
- `vae:VAE`（5 次）
- `frame_load_cap:INT`（5 次）
- `skip_first_frames:INT`（5 次）
- `video:STRING`（1 次）
- `force_rate:FLOAT,INT`（1 次）

## 输出

- `IMAGE:IMAGE`（5 次）
- `frame_count:INT`（5 次）
- `audio:AUDIO`（5 次）
- `video_info:VHS_VIDEOINFO`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"custom_height": 0, "custom_width": 0, "force_rate": 0, "format": "AnimateDiff", "frame_load_cap": 121, "select_every_n`（1 次）
- `{"custom_height": 0, "custom_width": 0, "force_rate": 0, "format": "AnimateDiff", "frame_load_cap": 121, "select_every_n`（1 次）
- `{"custom_height": 0, "custom_width": 0, "force_rate": 0, "format": "AnimateDiff", "frame_load_cap": 0, "select_every_nth`（1 次）
- `{"custom_height": 0, "custom_width": 0, "force_rate": 0, "format": "AnimateDiff", "frame_load_cap": 0, "select_every_nth`（1 次）
- `{"custom_height": 0, "custom_width": 0, "force_rate": 0, "format": "AnimateDiff", "frame_load_cap": 0, "select_every_nth`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
