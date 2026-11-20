---
name: image_to_image_upscale_lora_sampler_34
type: Image To Image
frequency: 5
level: strong
coverage: 0.94
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein漫画转真实照片4K_2027344351319302146.json, 图片生成/图生图/Klein面部一致超真实4K编辑_2026581313737723905.json, 图片生成/图生图/Z-Image增加真实质感去ai感，真实系_2046044910419185666.json, 图片生成/图生图/ZImage增加真实质感去油腻写实系_2053332475044212738.json, 图片生成/图生图/ZImage增加真实质感去油腻写实系_2057137840416448513.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein漫画转真实照片4K_2027344351319302146.json、图片生成/图生图/Klein面部一致超真实4K编辑_2026581313737723905.json、图片生成/图生图/Z-Image增加真实质感去ai感，真实系_2046044910419185666.json、图片生成/图生图/ZImage增加真实质感去油腻写实系_2053332475044212738.json、图片生成/图生图/ZImage增加真实质感去油腻写实系_2057137840416448513.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `Int` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ImageScaleBy` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `ReferenceLatent` —— 2/5 个有
- `TT_img_enc` —— 2/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 60% |
| 重绘幅度 | 0.45 | 0.45 - 1 | 5 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 60%
- 重绘幅度 中位数 0.45，观测区间 0.45 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
