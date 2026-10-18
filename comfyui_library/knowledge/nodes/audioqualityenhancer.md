# AudioQualityEnhancer

## 节点类型

`AudioQualityEnhancer`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `enhancement_level:FLOAT`（1 次）
- `use_source_separation:BOOLEAN`（1 次）
- `demucs_model:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vocals_enhance:FLOAT`（1 次）
- `drums_enhance:FLOAT`（1 次）
- `bass_enhance:FLOAT`（1 次）
- `other_enhance:FLOAT`（1 次）
- `clarity:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, true, "htdemucs", "cuda", 0.8800000000000001, 0.6, 0.4, 0.4, 0.4, 0.3, 0.2, 0.3, 1, "Standard", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
