---
name: image_to_image_ipadapter_sampler_clip
type: Image To Image
frequency: 6
level: strong
coverage: 0.7245
common_nodes: [CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, DetailTransfer, FreeU_V2, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageCASharpening+, KSampler, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadAndApplyICLightUnet, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/ICLight更换背景打光_1909561877968449537.json, 图片生成/图生图/ic-light 舞台打光_1917798131273240577.json, 图片生成/图生图/人物打光_1916654914070843394.json, 图片生成/图生图/照片打光自然真实质感_1891814057979097090.json, 图片生成/图生图/照片随意提示词打光_1915583640741548034.json, 图片生成/文生图/人物照片打光+高清_1912047591742238722.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_sampler_clip

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/ICLight更换背景打光_1909561877968449537.json、图片生成/图生图/ic-light 舞台打光_1917798131273240577.json、图片生成/图生图/人物打光_1916654914070843394.json、图片生成/图生图/照片打光自然真实质感_1891814057979097090.json、图片生成/图生图/照片随意提示词打光_1915583640741548034.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DetailTransfer`
- `FreeU_V2`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageCASharpening+`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `easy imageSize` —— 5/6 个有
- `easy negative` —— 5/6 个有
- `easy positive` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `easy stylesSelector` —— 5/6 个有
- `ArgosTranslateTextNode` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 6 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 6 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 6 | 100% |
| 调度器 | karras | - | 6 | 100% |
| 重绘幅度 | 0.7 | 0.7 - 0.8 | 6 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，6 个样本，一致性 100%
- 调度器 最常用 karras，6 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.7 - 0.8，6 个样本，取值集中（一致性 95%）
