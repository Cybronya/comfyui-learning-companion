# Resample Audio (HQ)

## 节点类型

`Resample Audio (HQ)`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `target_sr:INT`（1 次）
- `mode:COMBO`（1 次）
- `kaiser_beta:FLOAT`（1 次）

## 输出

- `audio_out:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[48000, "torchaudio", 14.8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
