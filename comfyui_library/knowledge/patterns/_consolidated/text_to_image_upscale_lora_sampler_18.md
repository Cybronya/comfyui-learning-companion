---
name: text_to_image_upscale_lora_sampler_18
type: Text To Image
frequency: 3
level: strong
coverage: 0.913333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, ImpactInt, JjkText, KSampler, LayerUtility: PurgeVRAM V2, Lora Loader Stack (rgthree), LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2+SeedVR放大4K写实增强二版｜文生图高清放大写实一步到位不返工_2100478328087072770.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强处理_2100294226142654465.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强｜文生图再叠高清放大，写实质感直接拉满_2100455779584266241.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2+SeedVR放大4K写实增强二版｜文生图高清放大写实一步到位不返工_2100478328087072770.json、图片生成/文生图/Krea2加SeedVR放大4K写实增强处理_2100294226142654465.json、图片生成/文生图/Krea2加SeedVR放大4K写实增强｜文生图再叠高清放大，写实质感直接拉满_2100455779584266241.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ImpactInt`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `Lora Loader Stack (rgthree)`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
