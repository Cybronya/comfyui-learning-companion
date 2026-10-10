# HAIGC_VideoSubtitleTimestampPro

## 节点类型

`HAIGC_VideoSubtitleTimestampPro`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `字幕格式:COMBO`（1 次）
- `字幕内容:STRING`（1 次）
- `视频帧率:FLOAT`（1 次）
- `开始时间:FLOAT`（1 次）
- `结束时间:FLOAT`（1 次）
- `每段显示时长:FLOAT`（1 次）
- `字幕间隔:FLOAT`（1 次）
- `字体选择:COMBO`（1 次）
- `字体大小:INT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `开始时间:FLOAT`（1 次）
- `结束时间:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["括号格式", "", 24.000000000000004, 0, 0, 2, 0.5, "AlibabaHealthFont2.0CN-85B", 173, 1, "粗体", "#FFFF00", 5, "#000000", 1, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
