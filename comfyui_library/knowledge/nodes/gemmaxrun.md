# GemmaxRun

## 节点类型

`GemmaxRun`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:COMBO`（2 次）
- `source_language:COMBO`（2 次）
- `target_language:COMBO`（2 次）
- `text:STRING`（2 次）
- `max_new_tokens:INT`（2 次）
- `unload_model:BOOLEAN`（2 次）

## 输出

- `translations:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["GemmaX2-28-2B-v0.1", "中文", "Japanese", "", 200, true]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
