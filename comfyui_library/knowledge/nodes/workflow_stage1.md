# workflow/Stage1

## 节点类型

`workflow/Stage1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（1 次）
- `guider:GUIDER`（1 次）
- `SamplerCustomAdvanced guider:GUIDER`（1 次）
- `SamplerCustomAdvanced 2 guider:GUIDER`（1 次）

## 输出

- `denoised_output:LATENT`（2 次）
- `SamplerCustomAdvanced denoised_output:LATENT`（2 次）
- `IMAGE:IMAGE`（2 次）
- `output:*`（2 次）
- `SamplerCustomAdvanced 23 denoised_output:LATENT`（1 次）
- `MODEL:MODEL`（1 次）
- `SamplerCustomAdvanced 22 denoised_output:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[247417502228701, "randomize", "flux1-dev-fp8-Kijai.safetensors", "fp8_e4m3fn", 30, "fixed", 25, "fixed", "euler", 1024,`（1 次）
- `[943713583328488, "randomize", "flux1-dev-fp8-Kijai.safetensors", "fp8_e4m3fn", 30, "fixed", 25, "fixed", "euler", 1024,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
