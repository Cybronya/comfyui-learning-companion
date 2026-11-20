---
name: image_to_image_inpaint_lora_sampler_3
type: Image To Image
frequency: 5
level: strong
coverage: 0.8882
common_nodes: [AILab_QwenVL, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, KSamplerSelect, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskBlur+, PreviewImage, PrimitiveStringMultiline, RandomNoise, ReferenceLatent, ResolutionSelector, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/工作流系列22-Klein模型工作流集合_2084996811659501570.json, 图片生成/图生图/工作流系列22-Klein模型工作流集合_2092624297952108546.json, 图片生成/文生图/Klein模型+Krea2模型工作流集合-养老院级解说_2096611076698890242.json, 图片生成/文生图/Klein模型工作流集合_2092442362462167041.json, 图片生成/文生图/工作流系列22-Klein模型工作流集合_2082269935987941378.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/工作流系列22-Klein模型工作流集合_2084996811659501570.json、图片生成/图生图/工作流系列22-Klein模型工作流集合_2092624297952108546.json、图片生成/文生图/Klein模型+Krea2模型工作流集合-养老院级解说_2096611076698890242.json、图片生成/文生图/Klein模型工作流集合_2092442362462167041.json、图片生成/文生图/工作流系列22-Klein模型工作流集合_2082269935987941378.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CR Text` —— 4/5 个有
- `CheckpointLoaderSimple` —— 4/5 个有
- `FastCanvas` —— 4/5 个有
- `GetImageSize+` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `INPAINT_ExpandMask` —— 4/5 个有
- `ImageAndMaskPreview` —— 4/5 个有
- `ImageCompositeMasked` —— 4/5 个有
- `MaskPreview` —— 4/5 个有
- `SAM3_Detect` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `easy positive` —— 4/5 个有
- `easy promptLine` —— 4/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Krea2EditGroundedEncode` —— 1/5 个有
- `Krea2EditModelPatch` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有
- `easy bookmark` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 40/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（40/5 个样本）：Steps较低可能导致细节不足
