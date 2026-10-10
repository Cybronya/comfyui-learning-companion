# LoadVideoFromURL

## 节点类型

`LoadVideoFromURL`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `url:STRING`（1 次）
- `force_rate:INT`（1 次）
- `force_size:COMBO`（1 次）
- `custom_width:INT`（1 次）
- `custom_height:INT`（1 次）
- `frame_load_cap:INT`（1 次）
- `skip_first_frames:INT`（1 次）
- `select_every_nth:INT`（1 次）

## 输出

- `frames:IMAGE`（1 次）
- `frame_count:INT`（1 次）
- `video_info:VHS_VIDEOINFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://example.com/video.mp4", 0, "Disabled", 512, 512, 0, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
