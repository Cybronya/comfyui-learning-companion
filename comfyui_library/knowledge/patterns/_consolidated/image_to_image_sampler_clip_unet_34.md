---
name: image_to_image_sampler_clip_unet_34
type: Image To Image
frequency: 9
level: moderate
coverage: 0.835778
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2015711272569937921.json, 图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2055150677059489793.json, 图片生成/图生图/FLUX-Klein 3图融合工作流_2014225545059373057.json, 图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json, 图片生成/图生图/Flux2-klein-海-真实感修复_2026489323687776257.json, 图片生成/图生图/Flux2-klein-海-进阶版_2020737366507393025.json, 图片生成/图生图/Flux2-klein_2018972817487826946.json, 图片生成/图生图/人像精修_一键磨皮美颜_2012010082908774402.json, 图片生成/图生图/磨皮+放大无像素偏移_2072204479679787010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2015711272569937921.json、图片生成/图生图/FLUX-2-Klein-图生图洗图工作流_2055150677059489793.json、图片生成/图生图/FLUX-Klein 3图融合工作流_2014225545059373057.json、图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json、图片生成/图生图/Flux2-klein-海-真实感修复_2026489323687776257.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/9 个有
- `CLIPLoader` —— 7/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `ReferenceLatent` —— 7/9 个有
- `FluxKontextImageScale` —— 5/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `SeedVR2LoadDiTModel` —— 4/9 个有
- `SeedVR2LoadVAEModel` —— 4/9 个有
- `SeedVR2VideoUpscaler` —— 4/9 个有
- `ColorMatch` —— 3/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `RepeatLatentBatch` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `DualCLIPLoader` —— 2/9 个有
- `FluxGuidance` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `BiRefNetRMBG` —— 1/9 个有
- `PowerfulMaskCrop` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 9 | 17% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 0.9 | 0.5 - 1 | 9 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，9 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.5 - 1，9 个样本
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
