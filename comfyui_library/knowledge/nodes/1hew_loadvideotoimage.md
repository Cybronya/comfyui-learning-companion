# 1hew_LoadVideoToImage

## 节点类型

`1hew_LoadVideoToImage`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `file:STRING`（2 次）
- `frame_limit:INT`（2 次）
- `fps:FLOAT`（2 次）
- `start_skip:INT`（2 次）
- `end_skip:INT`（2 次）
- `format:COMBO`（2 次）
- `video_index:INT`（2 次）
- `include_subdir:BOOLEAN`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `fps:FLOAT`（2 次）
- `frame_count:INT`（2 次）
- `filename:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["/data/ComfyUI/personal/input/1hew_uploads/FX01-reference-kinetic-title_1791510231752158674.mp4", 0, 0, 0, 0, "4n+1", 0`（1 次）
- `["", 0, 0, 0, 0, "4n+1", 0, false, null, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
