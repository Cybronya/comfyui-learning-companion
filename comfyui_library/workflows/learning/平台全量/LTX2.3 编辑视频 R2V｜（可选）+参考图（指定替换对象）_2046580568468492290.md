---
key: 平台全量/LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290.json
name: LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290.json
hash: aa442d18d2876adf
coverage: 0.774775
learned_at: 2026-11-14 00:37:46
nodes: [LTXVConditioning, VAEEncode, easy cleanGpuUsed, CFGGuider, KSamplerSelect, BasicScheduler, ManualSigmas, SolidMask, ImageConcanate, CFGGuider, KSamplerSelect, ManualSigmas, LTXVCropGuides, VAEDecodeTiled, LTXVPreprocess, easy cleanGpuUsed, ReservedRegionFrameComposer, easy cleanGpuUsed, ReservedRegionFrameComposer, ImageCompositeFromMaskBatch+, VHS_VideoCombine, MaskToImage, SetNode, LTXVConcatAVLatent, PrimitiveFloat, LTXVLatentUpsampler, ImageConcanate, RMBG, SAM3Segment, MaskToImage, ImageScaleBy, RandomNoise, GetImageSize, LTXVEmptyLatentAudio, SetLatentNoiseMask, LTXVAudioVAEEncode, ImageScaleBy, LTXVSeparateAVLatent, VAEDecode, LTXVCropGuides, LTXVSeparateAVLatent, ImageConcanate, ImageConcanate, ImageScaleBy, LTXVConcatAVLatent, LTXVAudioVAEDecode, SimpleCalculatorKJ, PreviewAudio, VHS_VideoCombine, ResizeImageMaskNode, VHS_VideoCombine, VHS_VideoCombine, SAM3Segment, ImageScaleBy, CLIPTextEncode, LoadImage, GrowMaskWithBlur, BlockifyMask, PreviewImage, ImageCompositeFromMaskBatch+, LatentUpscaleModelLoader, RandomNoise, ttN seed, Note, Note, Note, EmptyImage, GetImageSize+, Note, EmptyImage, GetImageSize+, BlockifyMask, GrowMaskWithBlur, Note, Note, Note, Note, Note, TrimAudioDuration, Note, Note, LoadAudio, easy showAnything, SimpleCalculatorKJ, Note, Note, PrimitiveFloat, PrimitiveInt, Note, Note, VHS_LoadVideo, CLIPTextEncode, PrimitiveString, Note, CheckpointLoaderSimple, LTXVAudioVAELoader, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, easy cleanGpuUsed, SamplerCustomAdvanced, easy cleanGpuUsed, SamplerCustomAdvanced, VHS_VideoCombine, Note, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, LTXVAddGuideMulti, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 平台全量/LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 编辑视频 R2V｜（可选）+参考图（指定替换对象）_2046580568468492290.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
- `LTXVConditioning`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ManualSigmas`
- `SolidMask`
- `ImageConcanate`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `easy cleanGpuUsed`
- `ReservedRegionFrameComposer`
- `easy cleanGpuUsed`
- `ReservedRegionFrameComposer`
- `ImageCompositeFromMaskBatch+`
- `VHS_VideoCombine`
- `MaskToImage`
- `SetNode`
- `LTXVConcatAVLatent`
- `PrimitiveFloat`
- `LTXVLatentUpsampler` ★核心
- `ImageConcanate`
- `RMBG`
- `SAM3Segment`
- `MaskToImage`
- `ImageScaleBy`
- `RandomNoise`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `ImageScaleBy`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `ImageConcanate`
- `ImageConcanate`
- `ImageScaleBy`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SimpleCalculatorKJ`
- `PreviewAudio`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SAM3Segment`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `PreviewImage`
- `ImageCompositeFromMaskBatch+`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `ttN seed`
- `Note`
- `Note`
- `Note`
- `EmptyImage`
- `GetImageSize+`
- `Note`
- `EmptyImage`
- `GetImageSize+`
- `BlockifyMask`
- `GrowMaskWithBlur`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `TrimAudioDuration`
- `Note`
- `Note`
- `LoadAudio`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `Note`
- `Note`
- `PrimitiveFloat`
- `PrimitiveInt`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `PrimitiveString`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Note`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **77%**（86/111）

**有卡**：`LTXVConditioning`、`VAEEncode`、`easy cleanGpuUsed`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`ManualSigmas`、`SolidMask`、`ImageConcanate`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVPreprocess`、`ReservedRegionFrameComposer`、`ImageCompositeFromMaskBatch+`、`VHS_VideoCombine`、`MaskToImage`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`RMBG`、`SAM3Segment`、`ImageScaleBy`、`RandomNoise`、`GetImageSize`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`SimpleCalculatorKJ`、`PreviewAudio`、`ResizeImageMaskNode`、`CLIPTextEncode`、`LoadImage`、`GrowMaskWithBlur`、`BlockifyMask`、`LatentUpscaleModelLoader`、`ttN seed`、`EmptyImage`、`GetImageSize+`、`TrimAudioDuration`、`LoadAudio`、`VHS_LoadVideo`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`LTXVAddGuideMulti`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、LTXVLatentUpsampler
