# WanVideoImageResizeToClosest

## 节点类型

`WanVideoImageResizeToClosest`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `image:IMAGE`（8 次）
- `generation_width:INT`（8 次）
- `generation_height:INT`（8 次）
- `aspect_ratio_preservation:COMBO`（8 次）

## 输出

- `image:IMAGE`（8 次）
- `width:INT`（8 次）
- `height:INT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[480, 832, "keep_input"]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
