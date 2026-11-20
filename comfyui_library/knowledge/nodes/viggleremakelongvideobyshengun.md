# ViggleRemakeLongVideoByShenGun

## 节点类型

`ViggleRemakeLongVideoByShenGun`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `keyframe_until:FLOAT`（4 次）
- `context_length:INT`（4 次）
- `context_overlap:INT`（4 次）
- `fuse_method:COMBO`（4 次）
- `freenoise:BOOLEAN`（4 次）
- `split_conds_to_windows:BOOLEAN`（4 次）
- `slice_source:BOOLEAN`（4 次）

## 输出

- `model:MODEL`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.9, 124, 39, "pyramid", true, false, true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
