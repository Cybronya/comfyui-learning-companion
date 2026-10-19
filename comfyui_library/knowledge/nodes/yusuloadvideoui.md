# YusuLoadVideoUI

## 节点类型

`YusuLoadVideoUI`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `video:STRING`（11 次）
- `start_time:FLOAT`（11 次）
- `end_time:FLOAT`（11 次）
- `duration:FLOAT`（11 次）
- `start_frame:INT`（11 次）
- `end_frame:INT`（11 次）
- `duration_frames:INT`（11 次）
- `resize_method:COMBO`（11 次）
- `custom_width:INT`（11 次）
- `custom_height:INT`（11 次）

## 输出

- `images:IMAGE`（11 次）
- `audio:AUDIO`（11 次）
- `duration:FLOAT`（11 次）
- `frame_count:INT`（11 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["f3dc187e90be7298b27ef61669e4ef884496196a70de3a9ba6f16f549bda6fd1.mp4", 3.08, 4, 0.92, 74, 96, 22, "maintain aspect rat`（1 次）
- `["f3dc187e90be7298b27ef61669e4ef884496196a70de3a9ba6f16f549bda6fd1.mp4", 0.48, 1.4, 0.92, 12, 34, 22, "maintain aspect r`（1 次）
- `["e419bf483c2cc3d2fafa76024043ed6b1b975e3e11d2c1d156258f5f5899f8fd.mp4", 3.08, 4, 0.92, 74, 96, 22, "maintain aspect rat`（1 次）
- `["e419bf483c2cc3d2fafa76024043ed6b1b975e3e11d2c1d156258f5f5899f8fd.mp4", 0.48, 1.4, 0.92, 12, 34, 22, "maintain aspect r`（1 次）
- `["f3dc187e90be7298b27ef61669e4ef884496196a70de3a9ba6f16f549bda6fd1.mp4", 3.08, 4, 0.92, 74, 96, 22, "maintain aspect rat`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
