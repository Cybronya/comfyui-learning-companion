# VideoTranscribe

## 节点类型

`VideoTranscribe`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `音频:AUDIO`（1 次）
- `转录配置:TRANSCRIBE_CONFIG`（1 次）
- `最小置信度:FLOAT`（1 次）
- `时间戳精度:INT`（1 次）
- `合并阈值:FLOAT`（1 次）
- `包含元数据:BOOLEAN`（1 次）
- `裁剪静音:BOOLEAN`（1 次）
- `过滤关键词:STRING`（1 次）

## 输出

- `字幕数据:SUBTITLE_DATA`（1 次）
- `字幕文本:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 3, 0, false, false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
