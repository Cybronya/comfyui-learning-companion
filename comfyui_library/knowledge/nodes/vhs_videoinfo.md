# VHS_VideoInfo

## 节点类型

`VHS_VideoInfo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video_info:VHS_VIDEOINFO`（2 次）

## 输出

- `source_fps🟨:FLOAT`（2 次）
- `source_frame_count🟨:INT`（2 次）
- `source_duration🟨:FLOAT`（2 次）
- `source_width🟨:INT`（2 次）
- `source_height🟨:INT`（2 次）
- `loaded_fps🟦:FLOAT`（2 次）
- `loaded_frame_count🟦:INT`（2 次）
- `loaded_duration🟦:FLOAT`（2 次）
- `loaded_width🟦:INT`（2 次）
- `loaded_height🟦:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{}`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
