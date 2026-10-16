# XB_VideoParamsMaster

## 节点类型

`XB_VideoParamsMaster`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `aspect_ratio:COMBO`（1 次）
- `duration_display:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `length:INT`（1 次）
- `fps:INT`（1 次）
- `fps_float:FLOAT`（1 次）

## 输出

- `Width:INT`（1 次）
- `Height:INT`（1 次）
- `Frames:INT`（1 次）
- `FPS:INT`（1 次）
- `FPS_Float:FLOAT`（1 次）
- `Scale Size:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["9:16", "视频时长: 5.00 秒", 480, 848, 121, 24, 24]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
