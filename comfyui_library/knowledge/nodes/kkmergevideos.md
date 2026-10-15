# kkMergeVideos

## 节点类型

`kkMergeVideos`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `video1:VIDEO`（5 次）
- `video2:VIDEO`（5 次）
- `video3:VIDEO`（5 次）
- `video4:VIDEO`（5 次）
- `video5:VIDEO`（5 次）
- `audio:AUDIO`（5 次）
- `size_reference:COMBO`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）
- `fps:FLOAT`（5 次）

## 输出

- `video:VIDEO`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["keep", 0, 0, 0]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
