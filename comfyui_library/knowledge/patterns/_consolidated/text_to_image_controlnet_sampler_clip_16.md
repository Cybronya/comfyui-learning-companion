---
name: text_to_image_controlnet_sampler_clip_16
type: Text To Image
frequency: 3
level: strong
coverage: 0.733667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Int, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy imageIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image+t2i++Controlnet+(6G显存可用)_2074078629277028354.json, 图片生成/文生图/Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817.json, 图片生成/文生图/Z-image+t2i++Controlnet_1998348287713402881.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image+t2i++Controlnet+(6G显存可用)_2074078629277028354.json、图片生成/文生图/Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817.json、图片生成/文生图/Z-image+t2i++Controlnet_1998348287713402881.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `ImpactConditionalBranch` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.65 - 1 | 3 | 81% |
| 宽度 | 1024 | 1024 - 1280 | 3 | 89% |
| 高度 | 1536 | 1536 - 1920 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.65 - 1，3 个样本，取值集中（一致性 81%）
- 宽度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
- 高度 中位数 1536，观测区间 1536 - 1920，3 个样本，取值集中（一致性 89%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
