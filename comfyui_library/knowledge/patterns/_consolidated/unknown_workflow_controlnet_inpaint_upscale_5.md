---
name: unknown_workflow_controlnet_inpaint_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.67
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, BiRefNet_Hugo, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text Concatenate, ControlNetApplySD3, ControlNetLoader, DF_Image_scale_to_side, DifferentialDiffusion, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Muter (rgthree), FluxGuidance, GrowMask, Image Overlay, Image To Mask, ImageCrop+, ImageResize+, ImageResizeKJ, ImageUpscaleWithModel, InpaintModelConditioning, InvertMask, JjkText, KSampler, KSamplerSelect, Label (rgthree), LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: ImageBlendAdvance V2, LoadImage, LoraLoader, MaskBlur+, MaskPreview+, MaskToImage, Note Plus (mtb), PortraitMasterBaseCharacter, PreviewImage, RH_Captioner, RandomNoise, ReActorRestoreFace, SamplerCustomAdvanced, SaveImage, Seed (rgthree), ShowText|pysssss, StyleModelApply, StyleModelLoader, TextCombinerSix, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageConcat, easy imageInsetCrop, easy imageSize, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商服装自定义pose一致性模_2042976998145921026.json, 图片生成/文生图/电商服装自定义pose一致性模特生成_1949743598805934082.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商服装自定义pose一致性模_2042976998145921026.json、图片生成/文生图/电商服装自定义pose一致性模特生成_1949743598805934082.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `BiRefNet_Hugo`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text Concatenate`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DF_Image_scale_to_side`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `GrowMask`
- `Image Overlay`
- `Image To Mask`
- `ImageCrop+`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InvertMask`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadImage`
- `LoraLoader`
- `MaskBlur+`
- `MaskPreview+`
- `MaskToImage`
- `Note Plus (mtb)`
- `PortraitMasterBaseCharacter`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `ReActorRestoreFace`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `TextCombinerSix`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`
- `easy imageInsetCrop`
- `easy imageSize`
- `easy positive`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（8/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
