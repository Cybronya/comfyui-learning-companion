---
key: 视频生成/文生视频/LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514.json
name: LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514.json
hash: 2da16e70763589df
coverage: 0.802469
learned_at: 2026-10-15 22:45:02
nodes: [Any Switch (rgthree), LoraLoaderModelOnly, UnetLoaderGGUF, LoraLoaderModelOnly, RandomNoise, MelBandRoFormerSampler, Audio Duration (mtb), SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, KSamplerSelect, ImageScaleBy, SamplerCustomAdvanced, CFGGuider, RandomNoise, ManualSigmas, LTXVScheduler, SamplerCustomAdvanced, KSamplerSelect, LTXVSpatioTemporalTiledVAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVAudioVAEDecode, LTXVTiledVAEDecode, CreateVideo, Any Switch (rgthree), CFGGuider, Any Switch (rgthree), Any Switch (rgthree), LTXVCropGuides, LTXVSeparateAVLatent, LTXVCropGuides, Any Switch (rgthree), EmptyImage, LoadAudio, TrimAudioDuration, MarkdownNote, UNETLoader, LoraLoaderModelOnly, MarkdownNote, SaveVideo, INTConstant, INTConstant, DualCLIPLoader, LTXVConcatAVLatent, Display Int (rgthree), LTXVEmptyLatentAudio, LTXVConcatAVLatent, CLIPTextEncode, LTX2_NAG, LTXVConditioning, GetImageSize, MathExpression|pysssss, PrimitiveFloat, EmptyLTXVLatentVideo, ResizeImagesByLongerEdge, ImageResizeKJv2, CR Float To Integer, SimpleCalculatorKJ, Any Switch (rgthree), INTConstant, LTXVPreprocess, LoadImage, LTX2_NAG, PrimitiveFloat, Any Switch (rgthree), Any Switch (rgthree), LTXVAddGuide, INTConstant, Fast Groups Bypasser (rgthree), MelBandRoFormerModelLoader, Fast Groups Bypasser (rgthree), LTXVAudioVAELoader, MarkdownNote, LatentUpscaleModelLoader, VAEDecode, LTXVLatentUpsampler, VAELoader, Fast Groups Bypasser (rgthree), LTXVAddGuide, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-IC-LORA-Dual-Character超强一致性（20s）_2049456418725568514.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `Any Switch (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `MelBandRoFormerSampler` ★核心
- `Audio Duration (mtb)`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `KSamplerSelect` ★核心
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `ManualSigmas`
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `CreateVideo`
- `Any Switch (rgthree)`
- `CFGGuider`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Any Switch (rgthree)`
- `EmptyImage`
- `LoadAudio`
- `TrimAudioDuration`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `SaveVideo`
- `INTConstant`
- `INTConstant`
- `DualCLIPLoader`
- `LTXVConcatAVLatent`
- `Display Int (rgthree)`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVConditioning`
- `GetImageSize`
- `MathExpression|pysssss`
- `PrimitiveFloat`
- `EmptyLTXVLatentVideo`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `CR Float To Integer`
- `SimpleCalculatorKJ`
- `Any Switch (rgthree)`
- `INTConstant`
- `LTXVPreprocess`
- `LoadImage`
- `LTX2_NAG`
- `PrimitiveFloat`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `LTXVAddGuide`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `MelBandRoFormerModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `LTXVAudioVAELoader`
- `MarkdownNote`
- `LatentUpscaleModelLoader`
- `VAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `LTXVAddGuide`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（65/81）

**有卡**：`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`RandomNoise`、`MelBandRoFormerSampler`、`Audio Duration (mtb)`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`KSamplerSelect`、`ImageScaleBy`、`SamplerCustomAdvanced`、`CFGGuider`、`ManualSigmas`、`LTXVScheduler`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVTiledVAEDecode`、`CreateVideo`、`LTXVCropGuides`、`EmptyImage`、`LoadAudio`、`TrimAudioDuration`、`UNETLoader`、`SaveVideo`、`INTConstant`、`DualCLIPLoader`、`LTXVConcatAVLatent`、`Display Int (rgthree)`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVConditioning`、`GetImageSize`、`MathExpression|pysssss`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`CR Float To Integer`、`SimpleCalculatorKJ`、`LTXVPreprocess`、`LoadImage`、`LTXVAddGuide`、`MelBandRoFormerModelLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`VAEDecode`、`LTXVLatentUpsampler`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
