# AniCrafterSampler

## 节点类型

`AniCrafterSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text_emb:AniCrafter_TEXT`（2 次）
- `data_dict:AniCrafter_PREDATA`（2 次）
- `model:MODEL_AniCrafter`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `fps:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1816693368, "randomize", 50, 1.5, 24, true]`（1 次）
- `[623219624, "randomize", 10, 1, 24, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
