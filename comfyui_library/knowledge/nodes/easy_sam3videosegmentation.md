# easy sam3VideoSegmentation

## 节点类型

`easy sam3VideoSegmentation`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sam3_model:EASY_SAM3_MODEL`（2 次）
- `video_frames:IMAGE`（2 次）
- `session_id:STRING`（2 次）
- `extra_config:EASY_SAM3_EXTRA_CONFIG`（2 次）
- `positive_coords:STRING`（2 次）
- `negative_coords:STRING`（2 次）
- `bbox:BBOX`（2 次）
- `prompt:STRING`（2 次）
- `frame_index:INT`（2 次）
- `object_id:INT`（2 次）

## 输出

- `masks:MASK`（2 次）
- `session_id:STRING`（2 次）
- `objects:EASY_SAM3_OBJECTS_OUTPUT`（2 次）
- `obj_masks:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0, 1, 0.5, 0.7, "both", 0, -1, true, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
