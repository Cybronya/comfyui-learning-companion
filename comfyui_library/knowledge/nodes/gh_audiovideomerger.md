# GH_AudioVideoMerger

## 节点类型

`GH_AudioVideoMerger`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（4 次）
- `音频:AUDIO`（4 次）
- `帧率:FLOAT`（4 次）
- `编码质量:COMBO`（4 次）
- `保存视频:BOOLEAN`（4 次）

## 输出

- `视频:VIDEO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, "标准", false]`（2 次）
- `[24, "标准", true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
