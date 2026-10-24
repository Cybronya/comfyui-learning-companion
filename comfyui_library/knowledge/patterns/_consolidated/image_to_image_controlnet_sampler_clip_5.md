---
name: image_to_image_controlnet_sampler_clip_5
type: Image To Image
frequency: 7
level: moderate
coverage: 0.726143
common_nodes: [AILab_ImageToList, AIO_Preprocessor, CLIPTextEncode, CR Seed, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, JanusImageUnderstanding, JanusModelLoader, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingDiscrete, ModelSamplingFlux, PreviewImage, SaveImage, ShowText|pysssss, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/Controlnet图像控制_涂鸦_颜色_TTPlanet_2061994887289069570.json, 图片生成/图生图/Controlnet图像控制_涂鸦_颜色_TTPlanet_2063446628295593985.json, 图片生成/图生图/Controlnet图像控制涂鸦上颜色_2067050039389810690.json, 图片生成/图生图/Controlnet图像控制涂鸦上颜色_2067414914137944065.json, 图片生成/图生图/Controlnet图像控制涂鸦上颜色_2067509832881623042.json, 图片生成/图生图/Controlnet（图像控制）姿态与深度控制类_2055995843945222146.json, 图片生成/图生图/全新3.0简笔画动漫自动上色修改瑕疵_2064622748084826113.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Controlnet图像控制_涂鸦_颜色_TTPlanet_2061994887289069570.json、图片生成/图生图/Controlnet图像控制_涂鸦_颜色_TTPlanet_2063446628295593985.json、图片生成/图生图/Controlnet图像控制涂鸦上颜色_2067050039389810690.json、图片生成/图生图/Controlnet图像控制涂鸦上颜色_2067414914137944065.json、图片生成/图生图/Controlnet图像控制涂鸦上颜色_2067509832881623042.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `AILab_ImageToList`
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CR Seed`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingDiscrete`
- `ModelSamplingFlux`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Manga2Anime_LineArt_Preprocessor` —— 6/7 个有
- `CLIPSetLastLayer` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `DWPreprocessor` —— 1/7 个有
- `DepthAnythingV2Preprocessor` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `IPAdapterAdvanced` —— 1/7 个有
- `IPAdapterModelLoader` —— 1/7 个有
- `IPAdapterNoise` —— 1/7 个有
- `Metric3D-DepthMapPreprocessor` —— 1/7 个有
- `Metric3D-NormalMapPreprocessor` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 40 | 3.5 - 40 | 7 | 63% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 6 | 100% |
| 调度器 | dpmpp_2m_sde | - | 7 | 86% |
| 重绘幅度 | karras | - | 7 | 86% |
| ControlNet 权重 | 0.4 | 0.4 - 0.9 | 7 | 63% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 40，观测区间 3.5 - 40，7 个样本
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde，7 个样本，一致性 86%
- 重绘幅度 最常用 karras，7 个样本，一致性 86%
- ControlNet 权重 中位数 0.4，观测区间 0.4 - 0.9，7 个样本
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
