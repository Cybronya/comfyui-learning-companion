---
name: text_to_image_upscale_lora_sampler_41
type: Text To Image
frequency: 6
level: strong
coverage: 0.8455
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, FastFilmGrain, INTConstant, ImageFromBatch, ImageScaleToTotalPixels, KSampler, LayerColor: BrightnessContrastV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, Pick From Batch (mtb), PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/zimage视频反推图片_2063085404601012226.json, 图片生成/反推提示词/zimage视频反推图片_2063090959159742465.json, 图片生成/反推提示词/zimage视频反推图片_2063090995717296129.json, 图片生成/图生图/参考视频出图+提示词换装_2067756798664335362.json, 图片生成/图生图/啊癫 zimage视频出图_2062910897399619586.json, 图片生成/图生图/啊癫 视频出图+图像自动换装编辑_2067646903717818369.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/zimage视频反推图片_2063085404601012226.json、图片生成/反推提示词/zimage视频反推图片_2063090959159742465.json、图片生成/反推提示词/zimage视频反推图片_2063090995717296129.json、图片生成/图生图/参考视频出图+提示词换装_2067756798664335362.json、图片生成/图生图/啊癫 zimage视频出图_2062910897399619586.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `FastFilmGrain`
- `INTConstant`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/6 个有
- `CFGGuider` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `Flux2Scheduler` —— 2/6 个有
- `KSamplerSelect` —— 2/6 个有
- `RandomNoise` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `SamplerCustomAdvanced` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `LazySwitch1way` —— 1/6 个有
- `easy boolean` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 6 | 100% |
| 高度 | 1920 | 1920 - 1920 | 6 | 100% |
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_2s | - | 6 | 100% |
| 调度器 | bong_tangent | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，6 个样本，一致性 100%
- 调度器 最常用 bong_tangent，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
