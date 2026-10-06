# easy multiTrackTaskOutput

## 节点类型

`easy multiTrackTaskOutput`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `tracks_info:TRACKS_INFO`（5 次）
- `images:IMAGE`（5 次）
- `audio:AUDIO`（5 次）
- `video:VIDEO`（5 次）
- `previous:*`（5 次）
- `task_index:INT`（5 次）
- `prompt_format:COMBO`（5 次）

## 输出

- `SYSTEM_PROMPT:STRING`（5 次）
- `USER_PROMPT:STRING`（5 次）
- `TYPE:STRING`（5 次）
- `LENGTH:INT`（5 次）
- `IMAGES:IMAGE`（5 次）
- `AUDIO:AUDIO`（5 次）
- `VIDEO:VIDEO`（5 次）
- `IMAGE_INDEXES:STRING`（5 次）
- `LOCKED_AUDIO:AUDIO`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "default"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
