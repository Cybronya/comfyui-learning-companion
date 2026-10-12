# JWLoadImageSequenceWithStopIndex

## 节点类型

`JWLoadImageSequenceWithStopIndex`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `path_pattern:STRING`（2 次）
- `start_index:INT`（2 次）
- `stop_index:INT`（2 次）
- `inclusive:COMBO`（2 次）
- `ignore_missing_images:COMBO`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["./fxai/video/{:06d}.png", 0, 162, "false", "true"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
