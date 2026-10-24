---
name: unknown_workflow_lora_sampler_clip_165
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.925
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, ImpactImageInfo, KSamplerSelect, LayerMask: MaskPreview, LayerUtility: ColorImage V2, LayerUtility: ImageBlendAdvance, LoadImage, LoraLoader, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, 取色器_孤海]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-klein-4B-消除流水线_2060191230574813185.json, 图片生成/图生图/FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089.json, 图片生成/图生图/【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_165

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX2-klein-4B-消除流水线_2060191230574813185.json、图片生成/图生图/FLUX2-klein-9b——object-remove移除万物+重绘_2013596554896089089.json、图片生成/图生图/【遇见AI】FLUX2-klein-4b，red-zoom局部放大，fal版lora_2014167810544508930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImpactImageInfo`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `取色器_孤海`

**可变部分**（部分 workflow 才有）：
- `Mask Fill Holes` —— 2/3 个有
- `BlockifyMask` —— 1/3 个有
- `ColorMatchV2` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.1 | 0.5 - 1.1 | 3 | 69% |
| LoRA 文本强度 | 1.1 | 1 - 1.1 | 3 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1.1，观测区间 0.5 - 1.1，3 个样本
- LoRA 文本强度 中位数 1.1，观测区间 1 - 1.1，3 个样本，取值集中（一致性 96%）
