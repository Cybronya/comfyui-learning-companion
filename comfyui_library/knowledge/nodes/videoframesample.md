# VideoFrameSample

## 节点类型

`VideoFrameSample`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `video:VIDEO`（30 次）
- `num_frames:INT`（30 次）
- `strategy:COMBO`（30 次）
- `seed:INT`（30 次）

## 输出

- `video:VIDEO`（30 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[39, "tail", 0, "fixed"]`（10 次）
- `[39, "head", 0, "fixed"]`（10 次）
- `[22, "tail", 0, "fixed"]`（5 次）
- `[1, "tail", 0, "fixed"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
