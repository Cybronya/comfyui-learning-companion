---
name: text_to_image_inpaint_upscale_lora_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.5615
common_nodes: [BlendInpaint, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CR Set Value On Boolean, CR Text Concatenate, CR Text Input Switch (4 way), ConditioningZeroOut, CutForInpaint, DeepTranslatorTextNode, DifferentialDiffusion, Display Any (rgthree), DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GrowMaskWithBlur, Image Comparer (rgthree), ImageGenResolutionFromImage, ImageScale, ImageToMask, ImpactCompare, ImpactFloat, InpaintModelConditioning, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoader, MaskToImage, PreviewImage, Primitive integer [Crystools], RepeatLatentBatch, SaveImage, Seed (rgthree), ShowText|pysssss, SimpleMath+, Text Multiline, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy float, easy ifElse, easy imageChooser]
problems: []
missing: [CR Set Value On Boolean, CR Text Concatenate, CR Text Input Switch (4 way), Display Any (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Primitive integer [Crystools], SimpleMath+, Text Multiline, easy float, easy imageChooser, Seed (rgthree)]
members: [图片生成/文生图/1934770233473474562.json, 图片生成/文生图/小说推文  短视频分镜配图（内含详尽使用说明）_2011012377889742850.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1934770233473474562.json、图片生成/文生图/小说推文  短视频分镜配图（内含详尽使用说明）_2011012377889742850.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `BlendInpaint`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CR Set Value On Boolean`
- `CR Text Concatenate`
- `CR Text Input Switch (4 way)`
- `ConditioningZeroOut`
- `CutForInpaint`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageGenResolutionFromImage`
- `ImageScale`
- `ImageToMask`
- `ImpactCompare`
- `ImpactFloat`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RepeatLatentBatch`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`
- `easy ifElse`
- `easy imageChooser`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 720 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Set Value On Boolean、CR Text Concatenate、CR Text Input Switch (4 way)、Display Any (rgthree)、LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
