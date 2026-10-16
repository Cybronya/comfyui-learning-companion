# XB_VideoLoader

## 节点类型

`XB_VideoLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `meta_batch:VHS_BatchManager`（1 次）
- `vae:VAE`（1 次）
- `video:COMBO`（1 次）
- `force_rate:FLOAT`（1 次）
- `custom_width:INT`（1 次）
- `custom_height:INT`（1 次）
- `frame_load_cap:INT`（1 次）
- `skip_first_frames:INT`（1 次）
- `select_every_nth:INT`（1 次）
- `format:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `frame_count:INT`（1 次）
- `audio:AUDIO`（1 次）
- `video_info:VHS_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", 0, 0, 0, 0, 0, 1, "AnimateDiff", "image", {"paused": false, "hidden": false, "params": {"custom_height": 0, "fi`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
