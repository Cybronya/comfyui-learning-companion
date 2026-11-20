---
name: image_to_image_sampler_clip_unet_21
type: Image To Image
frequency: 14
level: moderate
coverage: 0.826929
common_nodes: [CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.2-Klein_镜头角度编辑_2024306802296360961.json, 图片生成/图生图/FLUX.2-Klein图生图洗图工作流_2068593056466694146.json, 图片生成/图生图/FLUX2高清_2027640980047925250.json, 图片生成/图生图/FLUX2高清修复人像_2086408949896671233.json, 图片生成/图生图/FLUX3图像编辑_2110915403957497858.json, 图片生成/图生图/Flux2-Klein-9B-万物精修_2016119793451016194.json, 图片生成/图生图/Flux2-Klein-9B-毛坯图转效果图_2016119803773198338.json, 图片生成/图生图/Flux2-klein-万物精修（产品盒标贴一致性）_2036777306714279938.json, 图片生成/图生图/Flux2-klein-海-真实感修复_2026489323687776257.json, 图片生成/图生图/Flux2-klein-海-进阶版_2020737366507393025.json, 图片生成/图生图/Flux2-klein_2018972817487826946.json, 图片生成/图生图/人像精修_一键磨皮美颜_2012010082908774402.json, 图片生成/图生图/磨皮+放大无像素偏移_2072204479679787010.json, 平台全量/图片转线稿重新上色修改_2045723391201644546.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/FLUX.2-Klein_镜头角度编辑_2024306802296360961.json、图片生成/图生图/FLUX.2-Klein图生图洗图工作流_2068593056466694146.json、图片生成/图生图/FLUX2高清_2027640980047925250.json、图片生成/图生图/FLUX2高清修复人像_2086408949896671233.json、图片生成/图生图/FLUX3图像编辑_2110915403957497858.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 13/14 个有
- `Image Comparer (rgthree)` —— 13/14 个有
- `ReferenceLatent` —— 13/14 个有
- `CLIPLoader` —— 12/14 个有
- `FluxKontextImageScale` —— 9/14 个有
- `ColorMatch` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `PreviewImage` —— 6/14 个有
- `ImageResizeKJv2` —— 5/14 个有
- `SeedVR2LoadDiTModel` —— 4/14 个有
- `SeedVR2LoadVAEModel` —— 4/14 个有
- `SeedVR2VideoUpscaler` —— 4/14 个有
- `CR Text` —— 3/14 个有
- `DualCLIPLoader` —— 3/14 个有
- `FluxGuidance` —— 3/14 个有
- `RepeatLatentBatch` —— 3/14 个有
- `easy cleanGpuUsed` —— 3/14 个有
- `CR Prompt List` —— 1/14 个有
- `GetImageSize+` —— 1/14 个有
- `GetNode` —— 1/14 个有
- `ImageResize+` —— 1/14 个有
- `LayerUtility: NanoBananaImageScale` —— 1/14 个有
- `QwenEditTextEncode_EditUtils` —— 1/14 个有
- `ResizeImagesByLongerEdge` —— 1/14 个有
- `SetNode` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 30 | 14 | 16% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 0.9 | 0.5 - 1 | 14 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 30，14 个样本，取值分散，一致性仅 16%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 0.9，观测区间 0.5 - 1，14 个样本，取值集中（一致性 86%）
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足
