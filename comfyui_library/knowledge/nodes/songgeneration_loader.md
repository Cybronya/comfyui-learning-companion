# SongGeneration_Loader

## 节点类型

`SongGeneration_Loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `infer_model:COMBO`（1 次）
- `gguf:COMBO`（1 次）
- `version:COMBO`（1 次）
- `use_flash_attn:BOOLEAN`（1 次）
- `offload_audiolm:BOOLEAN`（1 次）

## 输出

- `model:SongGeneration_Audiolm`（1 次）
- `cfg:SongGeneration_Cfg`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["none", "SongGeneration-v2-large-Q6_K.gguf", "v2", true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
