---
key: 视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json
name: ltx2.3参考图+参考音色_2041020461265457154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json
hash: bac5e324db845ce1
coverage: 0.892857
learned_at: 2026-10-15 22:36:17
nodes: [KSamplerSelect, ComfyMathExpression, Reroute, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTX2_NAG, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVConcatAVLatent, CFGGuider, VAEDecodeTiled, LTXVCropGuides, LTXVAudioVAEDecode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, CFGGuider, LTXVReferenceAudio, LTXVEnhanceAVideoKJ, LTXVEnhanceAVideoKJ, LTX2SamplingPreviewOverride, PrimitiveInt, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, PrimitiveBoolean, VHS_VideoCombine, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, ImageSharpen, VHS_VideoCombine, PrimitiveInt, LoraLoaderModelOnly, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, PrimitiveInt, CheckpointLoaderSimple, LoraLoaderModelOnly, ConditioningZeroOut, LTXVAudioVAELoader, ManualSigmas, LTXVConditioning, LTXVReferenceAudio, CLIPTextEncode, ResizeImageMaskNode, ResizeImagesByLongerEdge, CLIPTextEncode, PrimitiveStringMultiline, LoadImage, VHS_LoadAudioUpload]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8mixed.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041020461265457154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTX2_NAG`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `LTXVReferenceAudio`
- `LTXVEnhanceAVideoKJ`
- `LTXVEnhanceAVideoKJ`
- `LTX2SamplingPreviewOverride`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `ImageSharpen`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `LTXVAudioVAELoader`
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVReferenceAudio`
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_LoadAudioUpload`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8mixed.safetensors`

## 知识

覆盖率 **89%**（50/56）

**有卡**：`KSamplerSelect`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTX2_NAG`、`RandomNoise`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`CFGGuider`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVReferenceAudio`、`LTXVEnhanceAVideoKJ`、`LTX2SamplingPreviewOverride`、`PrimitiveBoolean`、`VHS_VideoCombine`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`ImageSharpen`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`ConditioningZeroOut`、`LTXVAudioVAELoader`、`LTXVConditioning`、`CLIPTextEncode`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LoadImage`、`VHS_LoadAudioUpload`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
