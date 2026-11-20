# RH_PoseGallery

## 节点类型

`RH_PoseGallery`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `pose_id:STRING`（3 次）
- `resize_mode:COMBO`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `flip_horizontal:BOOLEAN`（3 次）

## 输出

- `姿势图:IMAGE`（3 次）
- `宽度:INT`（3 次）
- `高度:INT`（3 次）
- `姿势ID:STRING`（3 次）
- `描述:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["full_sexy_P010_front", "原尺寸", 768, 1024, false]`（1 次）
- `["full_sexy_P015_front", "原尺寸", 768, 1024, false]`（1 次）
- `["upper80v2_P014_front", "原尺寸", 768, 1024, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
