# AudioFeatureExtractor

## 节点类型

`AudioFeatureExtractor`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（4 次）
- `feature_pipe:FEATURE_PIPE`（4 次）

## 输出

- `FEATURE:FEATURE`（4 次）
- `FEATURE_PIPE:FEATURE_PIPE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["amplitude_envelope"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
