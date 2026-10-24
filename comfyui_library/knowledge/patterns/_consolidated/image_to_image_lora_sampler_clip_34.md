---
name: image_to_image_lora_sampler_clip_34
type: Image To Image
frequency: 8
level: strong
coverage: 0.911625
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去水印+高清修复qwen2511_2015565550251941889.json, 图片生成/图生图/图片去水印+高清修复Qwen_2511_fp8_2077787394471976961.json, 图片生成/图生图/建筑-Qwen2511增强细节工作流_2040792748348936193.json, 图片生成/图生图/批量去水印+高清修复（保持原图一致性，qwen2511）_2017477681155149826.json, 图片生成/图生图/白底转场景_1998207104886431746.json, 图片生成/图生图/白底转场景_2059536696349384705.json, 图片生成/图生图/白底转场景_2059548594629332993.json, 图片生成/图生图/背景大师_2072968660100145154.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/去水印+高清修复qwen2511_2015565550251941889.json、图片生成/图生图/图片去水印+高清修复Qwen_2511_fp8_2077787394471976961.json、图片生成/图生图/建筑-Qwen2511增强细节工作流_2040792748348936193.json、图片生成/图生图/批量去水印+高清修复（保持原图一致性，qwen2511）_2017477681155149826.json、图片生成/图生图/白底转场景_1998207104886431746.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 7/8 个有
- `RandomNoise` —— 7/8 个有
- `SamplerCustomAdvanced` —— 7/8 个有
- `SeedVR2LoadDiTModel` —— 6/8 个有
- `SeedVR2LoadVAEModel` —— 6/8 个有
- `SeedVR2VideoUpscaler` —— 6/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/8 个有
- `ReferenceLatent` —— 5/8 个有
- `CFGGuider` —— 4/8 个有
- `Canny` —— 4/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `EmptyFlux2LatentImage` —— 4/8 个有
- `Flux2Scheduler` —— 4/8 个有
- `FluxGuidance` —— 4/8 个有
- `GetImageSize` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `LoadDiffusionModelShared //Inspire` —— 4/8 个有
- `LoadTextEncoderShared //Inspire` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `BasicGuider` —— 3/8 个有
- `BasicScheduler` —— 3/8 个有
- `CR Prompt Text` —— 3/8 个有
- `ImageScaleBy` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 8 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
