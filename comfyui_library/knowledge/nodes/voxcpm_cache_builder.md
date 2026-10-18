# VoxCPM_Cache_Builder

## 节点类型

`VoxCPM_Cache_Builder`

## 分类

Optimization

## 作用

缓存/优化类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:VOXCPM_MODEL`（1 次）
- `prompt_audio:AUDIO`（1 次）
- `speaker_name:STRING`（1 次）
- `prompt_text:STRING`（1 次）

## 输出

- `VOXCPM_CACHE:VOXCPM_CACHE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["speaker2 ", "我发现，人生想要成功，只要做到两件事：一是不做愚蠢的事，二是活得久。做到这两点，你一定是人生赢家。\n"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
