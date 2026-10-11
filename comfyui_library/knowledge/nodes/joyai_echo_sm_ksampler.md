# JoyAI_Echo_SM_KSampler

## 节点类型

`JoyAI_Echo_SM_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `model:MODEL`（9 次）
- `te_cond:CONDITIONING`（9 次）
- `width:INT`（9 次）
- `height:INT`（9 次）
- `seed:INT`（9 次）
- `num_frames:INT`（9 次）
- `frame_rate:FLOAT`（9 次）
- `prefetch_count:INT`（9 次）
- `enable_tiles:BOOLEAN`（5 次）
- `tile_size_in_frames:INT`（5 次）

## 输出

- `images:IMAGE`（9 次）
- `audio:AUDIO`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 12345, "fixed", 121, 24, 1, false, true]`（3 次）
- `[832, 480, 295764869, "randomize", 121, 24, 1, false, 16, 512, "fast"]`（1 次）
- `[832, 480, 176638833, "randomize", 121, 24, 1, false, 16, 512, "fast"]`（1 次）
- `[832, 480, 465848633, "randomize", 121, 24, 1, false, true]`（1 次）
- `[832, 480, 862812363, "randomize", 121, 24, 1, false, 16, 512, "fast"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
