# FSampler

## 节点类型

`FSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（12 次）
- `positive:CONDITIONING`（12 次）
- `negative:CONDITIONING`（12 次）
- `latent_image:LATENT`（12 次）
- `seed:INT`（12 次）
- `steps:INT`（12 次）
- `cfg:FLOAT`（12 次）
- `scheduler:COMBO`（12 次）
- `sampler:COMBO`（12 次）
- `skip_mode:COMBO`（12 次）

## 输出

- `LATENT:LATENT`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1032620527253338, "randomize", 25, 2.5, "simple", "euler", "h4/s5", false]`（1 次）
- `[545299456324909, "randomize", 25, 2.5, "simple", "euler", "h2/s2", false]`（1 次）
- `[1124848275088866, "randomize", 25, 2.5, "simple", "euler", "h2/s3", false]`（1 次）
- `[166906943138456, "randomize", 25, 2.5, "simple", "euler", "h2/s4", false]`（1 次）
- `[547306159080563, "randomize", 25, 2.5, "simple", "euler", "h2/s5", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
