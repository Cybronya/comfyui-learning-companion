# VHS_LoadVideo

## 节点类型

`VHS_LoadVideo`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 21 个 workflow 中。

## 输入

- `meta_batch:VHS_BatchManager`（35 次）
- `vae:VAE`（35 次）
- `video:STRING`（35 次）
- `force_rate:INT`（35 次）
- `force_size:COMBO`（35 次）
- `custom_width:INT`（35 次）
- `custom_height:INT`（35 次）
- `frame_load_cap:INT`（35 次）
- `skip_first_frames:INT`（35 次）
- `select_every_nth:INT`（35 次）

## 输出

- `IMAGE:IMAGE`（35 次）
- `frame_count:INT`（35 次）
- `audio:AUDIO`（35 次）
- `video_info:VHS_VIDEOINFO`（35 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"choose video to upload": "image", "custom_height": 0, "custom_width": 0, "force_rate": 0, "force_size": "Disabled", "f`（6 次）
- `{"choose video to upload": "image", "custom_height": 0, "custom_width": 0, "force_rate": 0, "force_size": "Disabled", "f`（4 次）
- `{"choose video to upload": "image", "custom_height": 0, "custom_width": 0, "force_rate": 0, "force_size": "Disabled", "f`（4 次）
- `{"choose video to upload": "image", "custom_height": 0, "custom_width": 0, "force_rate": 0, "force_size": "Disabled", "f`（2 次）
- `{"choose video to upload": "image", "custom_height": 0, "custom_width": 0, "force_rate": 0, "force_size": "Disabled", "f`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
