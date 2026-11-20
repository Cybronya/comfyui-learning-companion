---
name: image_to_image_inpaint_lora_sampler_29
type: Image To Image
frequency: 2
level: weak
coverage: 0.8125
common_nodes: [BiRefNetRMBG, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DetailTransfer, DualCLIPLoader, Fast Groups Muter (rgthree), FastCanvas, FastCanvasTool, FluxGuidance, Image Comparer (rgthree), InpaintCrop, InpaintStitch, Int, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, LoraLoaderModelOnly, PreviewImage, RMBG, ReferenceLatent, RepeatLatentBatch, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen edit 2509_ 产品迁移溶图，还原细节纹理，戒指耳环珠宝产品增强_1988819451309068289.json, 平台全量/qwen image edit万物迁移融合_1964618629482430465.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Qwen edit 2509_ 产品迁移溶图，还原细节纹理，戒指耳环珠宝产品增强_1988819451309068289.json、平台全量/qwen image edit万物迁移融合_1964618629482430465.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DetailTransfer`
- `DualCLIPLoader`
- `Fast Groups Muter (rgthree)`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintStitch`
- `Int`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RMBG`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `InpaintResize` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `LayerUtility: CropByMask V3` —— 1/2 个有
- `LayerUtility: ImageCombineAlpha` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.9 | - | 2 | 100% |
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
