# DotsTTSLoadModel

## 节点类型

`DotsTTSLoadModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:COMBO`（1 次）
- `device:COMBO`（1 次）
- `dtype:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `download_if_missing:BOOLEAN`（1 次）
- `compile:BOOLEAN`（1 次）

## 输出

- `dotstts_model:DOTSTTS_MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dots.tts SOAR BF16 (local files)", "auto", "auto", "flash_attention", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
