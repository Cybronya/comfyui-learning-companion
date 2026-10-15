---
key: 视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json
name: LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json
hash: 383e5e9362b0cfe7
coverage: 0.872727
learned_at: 2026-10-15 22:44:48
nodes: [ResizeImagesByLongerEdge, KSamplerSelect, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ResizeImageMaskNode, LTXVPreprocess, ComfyMathExpression, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoInplace, CLIPTextEncode, CFGGuider, PrimitiveInt, VHS_VideoCombine, CFGGuider, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, RandomNoise, SamplerCustomAdvanced, LTXVLatentUpsampler, VAEDecodeTiled, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, ImageSharpen, FastFilmGrain, VHS_VideoCombine, VHS_VideoCombine, Reroute, LTXVCropGuides, LTXVEnhanceAVideoKJ, LTXVConditioning, ManualSigmas, LTX2SamplingPreviewOverride, LTXVImgToVideoInplace, LTXVEnhanceAVideoKJ, LTXVConcatAVLatent, PrimitiveBoolean, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, CLIPTextEncode, Fast Groups Muter (rgthree), LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `ResizeImagesByLongerEdge`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `ImageSharpen`
- `FastFilmGrain`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `LTXVCropGuides`
- `LTXVEnhanceAVideoKJ`
- `LTXVConditioning`
- `ManualSigmas`
- `LTX2SamplingPreviewOverride`
- `LTXVImgToVideoInplace`
- `LTXVEnhanceAVideoKJ`
- `LTXVConcatAVLatent`
- `PrimitiveBoolean`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **87%**（48/55）

**有卡**：`ResizeImagesByLongerEdge`、`KSamplerSelect`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImageMaskNode`、`LTXVPreprocess`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`CFGGuider`、`VHS_VideoCombine`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageSharpen`、`FastFilmGrain`、`LTXVCropGuides`、`LTXVEnhanceAVideoKJ`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
