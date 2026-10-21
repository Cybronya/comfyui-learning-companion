# KSampler Adv. (Efficient)

## 节点类型

`KSampler Adv. (Efficient)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）
- `latent_image:LATENT`（6 次）
- `optional_vae:VAE`（6 次）
- `script:SCRIPT`（6 次）
- `add_noise:COMBO`（6 次）
- `noise_seed:INT`（6 次）
- `steps:INT`（6 次）
- `cfg:FLOAT`（6 次）

## 输出

- `MODEL:MODEL`（6 次）
- `CONDITIONING+:CONDITIONING`（6 次）
- `CONDITIONING-:CONDITIONING`（6 次）
- `LATENT:LATENT`（6 次）
- `VAE:VAE`（6 次）
- `IMAGE:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", 717411847197327, null, 40, 5, "euler_ancestral", "normal", 0, 4650, "disable", "latent2rgb", "false"]`（2 次）
- `["enable", 717411847197327, null, 45, 5, "euler_ancestral", "normal", 0, 4650, "disable", "latent2rgb", "false"]`（1 次）
- `["enable", 912861269153287, null, 50, 5, "euler_ancestral", "normal", 0, 4650, "disable", "latent2rgb", "false"]`（1 次）
- `["enable", 832715465179503, null, 35, 5, "euler_ancestral", "karras", 0, 4650, "disable", "latent2rgb", "false"]`（1 次）
- `["enable", 462827102402729, null, 30, 5, "euler_ancestral", "karras", 0, 4650, "disable", "latent2rgb", "false"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
