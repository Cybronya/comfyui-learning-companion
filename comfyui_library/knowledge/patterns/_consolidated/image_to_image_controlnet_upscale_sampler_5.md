---
name: image_to_image_controlnet_upscale_sampler_5
type: Image To Image
frequency: 4
level: strong
coverage: 0.8015
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, Image Comparer (rgthree), ImageResize+, KSampler, LoadImage, Miaoshouai_Tagger, PreviewImage, SUPIR_Upscale, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品CMF材质拓展_1922496385088946178.json, 图片生成/图生图/毛坯房效果图生成_1922658809972494338.json, 图片生成/图生图/氛围颜色更改_1922667276154146818.json, 图片生成/图生图/草图上色_1922509195185197058.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/产品CMF材质拓展_1922496385088946178.json、图片生成/图生图/毛坯房效果图生成_1922658809972494338.json、图片生成/图生图/氛围颜色更改_1922667276154146818.json、图片生成/图生图/草图上色_1922509195185197058.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `Miaoshouai_Tagger`
- `PreviewImage`
- `SUPIR_Upscale`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `ColorMatch` —— 3/4 个有
- `easy ipadapterApplyADV` —— 3/4 个有
- `AnyLineArtPreprocessor_aux` —— 2/4 个有
- `ACN_ControlNetLoaderAdvanced` —— 1/4 个有
- `ACN_ScaledSoftControlNetWeights` —— 1/4 个有
- `ACN_SoftT2IAdapterWeights` —— 1/4 个有
- `BiRefNetRMBG` —— 1/4 个有
- `BiRefNet_Hugo` —— 1/4 个有
- `Seed Everywhere` —— 1/4 个有
- `TimestepKeyframe` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 35 | 35 - 35 | 4 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 4 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，观测区间 35 - 35，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
