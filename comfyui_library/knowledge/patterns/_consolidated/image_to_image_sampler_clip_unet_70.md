---
name: image_to_image_sampler_clip_unet_70
type: Image To Image
frequency: 6
level: strong
coverage: 0.938
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 - Klein _  九宫格分镜_2015362104047443970.json, 图片生成/图生图/Flux2 Klein 图像重构-线色分离组合_2017242186005356545.json, 图片生成/图生图/Flux2-klein9B多角度分镜直出_2022298975256186881.json, 图片生成/图生图/切换镜头klein9b_2037790414211653633.json, 图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2014686037674561538.json, 图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2024685759059464194.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_70

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux2 - Klein _  九宫格分镜_2015362104047443970.json、图片生成/图生图/Flux2 Klein 图像重构-线色分离组合_2017242186005356545.json、图片生成/图生图/Flux2-klein9B多角度分镜直出_2022298975256186881.json、图片生成/图生图/切换镜头klein9b_2037790414211653633.json、图片生成/图生图/图片模糊变高清+高清放大+增强细节-Flux2 Klein_2014686037674561538.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `GetImageSize` —— 3/6 个有
- `Qwen3_VQA` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `easy promptLine` —— 3/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `FluxGuidance` —— 2/6 个有
- `Image Compare (mtb)` —— 2/6 个有
- `JWStringConcat` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `ResizeImagesByLongerEdge` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 6 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
