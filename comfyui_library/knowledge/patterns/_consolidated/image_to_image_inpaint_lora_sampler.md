---
name: image_to_image_inpaint_lora_sampler
type: Image To Image
frequency: 3
level: strong
coverage: 0.891667
common_nodes: [AILab_QwenVL, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, KSamplerSelect, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskBlur+, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Klein模型+Krea2模型工作流集合-养老院级解说_2096611076698890242.json, 图片生成/文生图/Klein模型工作流集合_2092442362462167041.json, 图片生成/文生图/工作流系列22-Klein模型工作流集合_2082269935987941378.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Klein模型+Krea2模型工作流集合-养老院级解说_2096611076698890242.json、图片生成/文生图/Klein模型工作流集合_2092442362462167041.json、图片生成/文生图/工作流系列22-Klein模型工作流集合_2082269935987941378.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ReferenceLatent`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `FastCanvas` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `INPAINT_ExpandMask` —— 2/3 个有
- `ImageAndMaskPreview` —— 2/3 个有
- `ImageCompositeMasked` —— 2/3 个有
- `MaskPreview` —— 2/3 个有
- `SAM3_Detect` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy imageColorMatch` —— 2/3 个有
- `easy positive` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Krea2EditGroundedEncode` —— 1/3 个有
- `Krea2EditModelPatch` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy bookmark` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 3 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（24/3 个样本）：Steps较低可能导致细节不足
