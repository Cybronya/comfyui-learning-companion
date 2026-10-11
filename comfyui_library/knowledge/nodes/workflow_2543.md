# workflow>运行采样

## 节点类型

`workflow>运行采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `av_latent:LATENT`（1 次）
- `Turbo 4 video / 5 audio model:MODEL`（1 次）
- `Turbo 4 video / 5 audio av_latent:LATENT`（1 次）
- `BasicScheduler model:MODEL`（1 次）
- `Turbo 4 video / 5 audio 2 model:MODEL`（1 次）
- `Turbo 4 video / 5 audio 2 av_latent:LATENT`（1 次）
- `Turbo 4 video / 5 audio 3 model:MODEL`（1 次）
- `Turbo 4 video / 5 audio 3 av_latent:LATENT`（1 次）
- `BasicGuider model:MODEL`（1 次）

## 输出

- `NOISE:NOISE`（1 次）
- `RandomNoise NOISE:NOISE`（1 次）
- `RandomNoise 2 NOISE:NOISE`（1 次）
- `RandomNoise 3 NOISE:NOISE`（1 次）
- `RandomNoise 4 NOISE:NOISE`（1 次）
- `SAMPLER:SAMPLER`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `Turbo 4 video / 5 audio sampler:SAMPLER`（1 次）
- `Turbo 4 video / 5 audio sigmas:SIGMAS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[102469134, "fixed", 106172835, "fixed", 104938268, "fixed", 147263133599881, "fixed", 103703701, "fixed", "res_multiste`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
