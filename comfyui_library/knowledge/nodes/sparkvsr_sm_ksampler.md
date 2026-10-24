# SparkVSR_SM_KSampler

## 节点类型

`SparkVSR_SM_KSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `conds:CONDITIONING`（2 次）
- `seed:INT`（2 次）
- `overlap_t:INT`（2 次）
- `chunk_len:INT`（2 次）
- `overlap_hw:COMBO`（2 次）
- `tile_size_hw:COMBO`（2 次）
- `noise_step:INT`（2 次）
- `sr_noise_step:INT`（2 次）
- `ref_guidance_scale:FLOAT`（2 次）

## 输出

- `images:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[647960148, "randomize", 8, 0, "32x32", "0x0", 0, 399, 1, true, 1]`（1 次）
- `[1980494247, "randomize", 8, 0, "32x32", "0x0", 0, 399, 1, true, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
