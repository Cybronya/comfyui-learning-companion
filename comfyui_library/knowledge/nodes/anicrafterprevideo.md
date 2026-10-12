# AniCrafterPreVideo

## 节点类型

`AniCrafterPreVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_data:AniCrafter_DATA`（2 次）
- `video_image:IMAGE`（2 次）
- `video_mask:IMAGE`（2 次）
- `video_bkgd:IMAGE`（2 次）
- `fps:FLOAT`（2 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `max_frames:INT`（1 次）

## 输出

- `data_dict:AniCrafter_PREDATA`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", 768, 768, 80, 24, 60, true, true, "none"]`（1 次）
- `["none", 720, 720, 80, true, 45, true, true, "none"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
