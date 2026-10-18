# StaticSubtitlesToVideoMW

## 节点类型

`StaticSubtitlesToVideoMW`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `视频:IMAGE`（1 次）
- `帧率:FLOAT`（1 次）
- `字幕文本:STRING`（1 次）
- `字体:COMBO`（1 次）
- `字体大小比例:FLOAT`（1 次）
- `字体颜色:STRING`（1 次）
- `字体背景色:STRING`（1 次）
- `背景透明度:FLOAT`（1 次）
- `字幕宽度比例:FLOAT`（1 次）
- `垂直向上偏移:INT`（1 次）

## 输出

- `静态字幕视频:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Asimsun.ttc", 0.05, "#FFFFFF", "#0000FF", 0.5, 0.9, 30, "center", 4, 0, "", 5, 10, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
