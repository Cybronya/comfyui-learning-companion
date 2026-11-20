---
name: image_to_image_ipadapter_sampler_clip_2
type: Image To Image
frequency: 4
level: strong
coverage: 0.8455
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, GrowMask, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Blend by Mask, Image Blending Mode, Image Levels Adjustment, ImageCompositeMasked, ImageInvert, ImageResize+, KSampler, LoadAndApplyICLightUnet, LoadImage, MaskToImage, PreviewImage, SaveImage, SplitImageWithAlpha, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/电商提示词更换产品背景+打光_1910221041443008514.json, 平台全量/Product Image to Hero Shot_1864141217469759490.json, 平台全量/商拍优化-灯光、阴影和背景细节_1836377720430424065.json, 平台全量/超好用的电商背景生成工作流，一键生成全使用场景，运行时间10分钟，一次出30张图_1906948405485244418.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/电商提示词更换产品背景+打光_1910221041443008514.json、平台全量/Product Image to Hero Shot_1864141217469759490.json、平台全量/商拍优化-灯光、阴影和背景细节_1836377720430424065.json、平台全量/超好用的电商背景生成工作流，一键生成全使用场景，运行时间10分钟，一次出30张图_1906948405485244418.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GrowMask`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Blend by Mask`
- `Image Blending Mode`
- `Image Levels Adjustment`
- `ImageCompositeMasked`
- `ImageInvert`
- `ImageResize+`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SplitImageWithAlpha`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ICLightApplyMaskGrey` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageGaussianBlur` —— 3/4 个有
- `easy imageRemBg` —— 2/4 个有
- `BackgroundScaler` —— 1/4 个有
- `Display Int (rgthree)` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `Image Filter Adjustments` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `InspyrenetRembg` —— 1/4 个有
- `LayerFilter: GaussianBlur` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/4 个有
- `RandomPrompt` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 4 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
