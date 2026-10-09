# workflow>自定义采样

## 节点类型

`workflow>自定义采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `噪波生成:NOISE`（1 次）
- `引导:GUIDER`（1 次）
- `采样器:SAMPLER`（1 次）
- `Sigmas:SIGMAS`（1 次）
- `Latent:LATENT`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `模型:MODEL`（1 次）
- `BasicGuider model:MODEL`（1 次）
- `条件:CONDITIONING`（1 次）
- `BasicGuider 2 model:MODEL`（1 次）

## 输出

- `输出:LATENT`（1 次）
- `降噪输出:LATENT`（1 次）
- `Sigmas:SIGMAS`（1 次）
- `引导:GUIDER`（1 次）
- `SamplerCustomAdvanced 输出:LATENT`（1 次）
- `SamplerCustomAdvanced 降噪输出:LATENT`（1 次）
- `SamplerCustomAdvanced 8 降噪输出:LATENT`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["deis", 357327958629835, "randomize", 3.5, "beta", 20, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
