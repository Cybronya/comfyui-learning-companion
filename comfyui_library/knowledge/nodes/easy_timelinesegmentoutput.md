# easy timelineSegmentOutput

## 节点类型

`easy timelineSegmentOutput`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `timeline_info:TIMELINE_INFO`（3 次）
- `images:IMAGE`（3 次）
- `audio:AUDIO`（3 次）
- `prompt_format:COMBO`（3 次）
- `segment_index:INT`（3 次）

## 输出

- `PROMPT:STRING`（3 次）
- `TYPE:INT`（3 次）
- `NO_IMAGES:BOOLEAN`（3 次）
- `IMAGE_INDEXES:STRING`（3 次）
- `LENGTH:INT`（3 次）
- `IMAGES:IMAGE`（3 次）
- `AUDIO:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["default", 0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
