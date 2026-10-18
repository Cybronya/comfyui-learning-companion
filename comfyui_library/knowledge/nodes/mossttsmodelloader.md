# MossTTSModelLoader

## 节点类型

`MossTTSModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_variant:COMBO`（4 次）
- `dtype:COMBO`（4 次）
- `offload:COMBO`（4 次）
- `attention:COMBO`（4 次）

## 输出

- `MOSS_TTS_PIPE:MOSS_TTS_PIPE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MOSS-VoiceGenerator", "auto", "auto", "flash_attention_2"]`（1 次）
- `["MOSS-TTS (Local 1.7B)", "auto", "auto", "flash_attention_2"]`（1 次）
- `["MOSS-TTSD v1.0", "auto", "auto", "flash_attention_2"]`（1 次）
- `["MOSS-SoundEffect", "auto", "auto", "flash_attention_2"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
