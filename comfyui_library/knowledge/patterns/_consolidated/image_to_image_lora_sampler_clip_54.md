---
name: image_to_image_lora_sampler_clip_54
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9866
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, RH_LLMAPI_NODE, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext Presets官方预设模板_1944785081019846657.json, 图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json, 图片生成/图生图/单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937.json, 图片生成/图生图/双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722.json, 图片生成/图生图/极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext Presets官方预设模板_1944785081019846657.json、图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json、图片生成/图生图/单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937.json、图片生成/图生图/双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722.json、图片生成/图生图/极速超级卸妆Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1955657512878051330.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 4/5 个有
- `ImageStitch` —— 3/5 个有
- `GetImageSize+` —— 2/5 个有
- `Int` —— 2/5 个有
- `Bjornulf_ShowStringText` —— 1/5 个有
- `ImageScaleByAspectRatio_UTK` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `LoadKontextPresets` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
