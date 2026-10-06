# Video Slice

## 节点类型

`Video Slice`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `video:VIDEO`（13 次）
- `start_time:FLOAT`（13 次）
- `duration:FLOAT`（13 次）
- `strict_duration:BOOLEAN`（13 次）

## 输出

- `VIDEO:VIDEO`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 15, false]`（9 次）
- `[0, 5, false]`（3 次）
- `[0, 10.000000000000002, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
