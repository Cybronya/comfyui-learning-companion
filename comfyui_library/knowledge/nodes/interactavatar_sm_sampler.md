# InteractAvatar_SM_Sampler

## 节点类型

`InteractAvatar_SM_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `data_dict:CONDITIONING`（4 次）
- `steps:INT`（4 次）
- `seed:INT`（4 次）
- `sample_shift:FLOAT`（4 次）
- `text_guide_scale:FLOAT`（4 次）
- `audio_guide_scale:FLOAT`（4 次）
- `bad_thres:INT`（4 次）
- `motion_frame:INT`（4 次）
- `bad_cfg:BOOLEAN`（4 次）

## 输出

- `Latent:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 1292619922, "randomize", 5, 5, 7.5, 800, 25, true, false]`（1 次）
- `[20, 353668599, "randomize", 5, 5, 7.5, 800, 25, 1000, false]`（1 次）
- `[20, 356140698, "randomize", 5, 5, 7.5, 800, 25, true, false]`（1 次）
- `[50, 1903171835, "randomize", 5, 5, 7.5, 800, 25, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
