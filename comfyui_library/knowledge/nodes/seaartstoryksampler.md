# SeaArtStoryKSampler

## 节点类型

`SeaArtStoryKSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent_image:LATENT`（2 次）

## 输出

- `LATENT:LATENT`（2 次）
- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[230600189288560, "randomize", 25, 3.5, "dpmpp_2m_sde_gpu", "karras", 1]`（1 次）
- `[63502119285986, "randomize", 25, 3.5, "dpmpp_2m_sde_gpu", "karras", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
