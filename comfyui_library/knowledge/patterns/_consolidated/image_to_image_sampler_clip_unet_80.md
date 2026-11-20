---
name: image_to_image_sampler_clip_unet_80
type: Image To Image
frequency: 7
level: moderate
coverage: 0.925429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 - Klein _  九宫格分镜_2015362104047443970.json, 图片生成/图生图/Flux2 Klein 图像重构-线色分离组合_2017242186005356545.json, 图片生成/图生图/Flux2-klein9B多角度分镜直出_2022298975256186881.json, 图片生成/图生图/切换镜头klein9b_2037790414211653633.json, 图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2014686037674561538.json, 图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2024685759059464194.json, 平台全量/Flux2 Klein 去AI感 增加皮肤细节质感 控油+高清放大+增强细节_2015235708214059010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux2 - Klein _  九宫格分镜_2015362104047443970.json、图片生成/图生图/Flux2 Klein 图像重构-线色分离组合_2017242186005356545.json、图片生成/图生图/Flux2-klein9B多角度分镜直出_2022298975256186881.json、图片生成/图生图/切换镜头klein9b_2037790414211653633.json、图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2014686037674561538.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `GetImageSize` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `DualCLIPLoader` —— 3/7 个有
- `FluxGuidance` —— 3/7 个有
- `Image Compare (mtb)` —— 3/7 个有
- `Qwen3_VQA` —— 3/7 个有
- `Text Multiline` —— 3/7 个有
- `easy promptLine` —— 3/7 个有
- `JWStringConcat` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `ResizeImagesByLongerEdge` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有
- `SeedVR2ExtraArgs` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 7 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.25 - 1 | 7 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，7 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，7 个样本
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
