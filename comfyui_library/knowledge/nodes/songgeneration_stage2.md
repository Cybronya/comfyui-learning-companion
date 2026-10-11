# SongGeneration_Stage2

## 节点类型

`SongGeneration_Stage2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:SongGeneration_Audiolm`（1 次）
- `cfg:SongGeneration_Cfg`（1 次）
- `cond:SongGeneration_Cond`（1 次）
- `gen_type:COMBO`（1 次）
- `description:STRING`（1 次）
- `cfg_coef:FLOAT`（1 次）
- `temp:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `top_p:FLOAT`（1 次）
- `record_tokens:BOOLEAN`（1 次）

## 输出

- `cond:SongGeneration_Cond`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mixed", "female jazz vocalist, melancholic ballad, intimate grand piano with rich jazz voicings, soft brushed drums an`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
