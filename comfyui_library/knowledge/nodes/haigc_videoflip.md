# HAIGC_VideoFlip

## 节点类型

`HAIGC_VideoFlip`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `视频帧率:FLOAT`（2 次）
- `翻转方式:COMBO`（2 次）

## 输出

- `视频:IMAGE`（2 次）
- `输出帧数:INT`（2 次）
- `输出时长:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, "水平翻转"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
