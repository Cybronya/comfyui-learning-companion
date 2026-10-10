# TranscribeConfig

## 节点类型

`TranscribeConfig`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `转录模型:COMBO`（1 次）
- `语言:COMBO`（1 次）
- `模型大小:COMBO`（1 次）
- `使用缓存:BOOLEAN`（1 次）
- `词级时间戳:BOOLEAN`（1 次）
- `语音检测过滤:BOOLEAN`（1 次）
- `语音检测阈值:FLOAT`（1 次）
- `提示模式:COMBO`（1 次）
- `设备:COMBO`（1 次）
- `语音检测方法:COMBO`（1 次）

## 输出

- `转录配置:TRANSCRIBE_CONFIG`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["必剪接口", "zh", "belle-large-v3-zh-punct", false, false, false, 0.5, "中英混合 🌐", "cpu", "silero_v4_fw"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
