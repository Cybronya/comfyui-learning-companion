---
name: unknown_workflow_upscale_latent_upscale_lora_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7775
common_nodes: [Any Switch (rgthree), Audio Duration (mtb), CFGGuider, CLIPTextEncode, CR Float To Integer, CreateVideo, Display Int (rgthree), DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetImageSize, INTConstant, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LTXVTiledVAEDecode, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514.json, 视频生成/文生视频/Sulphur_bf16无限制极速版（10s 2min））_2054475235839234050.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514.json、视频生成/文生视频/Sulphur_bf16无限制极速版（10s 2min））_2054475235839234050.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Duration (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `CreateVideo`
- `Display Int (rgthree)`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `INTConstant`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LTXVTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DuckHideNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LTX2_NAG` —— 1/2 个有
- `LTXVAddGuide` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `LTXVImgToVideoInplace` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `ResizeImageMaskNode` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `VisionLLMNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
