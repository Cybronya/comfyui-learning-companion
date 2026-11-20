# FlexVideoDirection

## 节点类型

`FlexVideoDirection`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（6 次）
- `feature:FEATURE`（6 次）
- `feature_pipe:FEATURE_PIPE`（6 次）

## 输出

- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.99, "relative", "direction", 0]`（4 次）
- `[0.99, "absolute", "direction", 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
