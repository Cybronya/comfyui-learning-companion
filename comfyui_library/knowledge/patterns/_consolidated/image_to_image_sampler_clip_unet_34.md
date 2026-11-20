---
name: image_to_image_sampler_clip_unet_34
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8787
common_nodes: [CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json, 图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流_2052361394179321858.json, 图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流教学版（内含教程）_2020116611205701634.json, 图片生成/图生图/Flux Klein 多图编辑工作流 可多图融合_2018923003224002561.json, 图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json, 图片生成/图生图/Flux2-klein-海-真实感修复_2026489323687776257.json, 图片生成/图生图/Flux2-klein-海-进阶版_2020737366507393025.json, 图片生成/图生图/Flux2-klein_2018972817487826946.json, 图片生成/图生图/人像精修_一键磨皮美颜_2012010082908774402.json, 图片生成/图生图/磨皮+放大无像素偏移_2072204479679787010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json、图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流_2052361394179321858.json、图片生成/图生图/FLUX2 Klein 多图编辑、多图融合工作流教学版（内含教程）_2020116611205701634.json、图片生成/图生图/Flux Klein 多图编辑工作流 可多图融合_2018923003224002561.json、图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 8/10 个有
- `PreviewImage` —— 7/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `FluxKontextImageScale` —— 5/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `SeedVR2LoadDiTModel` —— 4/10 个有
- `SeedVR2LoadVAEModel` —— 4/10 个有
- `SeedVR2VideoUpscaler` —— 4/10 个有
- `ColorMatch` —— 3/10 个有
- `EmptyFlux2LatentImage` —— 3/10 个有
- `EmptySD3LatentImage` —— 3/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `RepeatLatentBatch` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `DualCLIPLoader` —— 2/10 个有
- `FluxGuidance` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 10 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 10 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，10 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，10 个样本，取值集中（一致性 92%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
