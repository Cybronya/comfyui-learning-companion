---
key: 视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json
name: LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json
hash: c3bfa5a8c87e2bc9
coverage: 0.938776
learned_at: 2026-10-15 22:44:34
nodes: [LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVPreprocess, DownloadAndLoadDepthCrafterModel, easy showAnything, easy showAnything, CM_FloatToInt, VHS_VideoInfoLoaded, CannyEdgePreprocessor, DepthCrafter, EmptyLTXVLatentVideo, PreviewImage, SimpleMath+, PrimitiveBoolean, PreviewImage, RandomNoise, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVCropGuides, DualCLIPLoader, VAELoader, UNETLoader, VAELoaderKJ, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, KSamplerSelect, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CFGGuider, VAEDecodeTiled, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVImgToVideoConditionOnly, ImageResizeKJv2, LTXAddVideoICLoRAGuide, CheckpointLoaderSimple, LTXVConditioning, LTX2_NAG, LTXVSeparateAVLatent, CreateVideo, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, MelBandRoFormerSampler, MelBandRoFormerModelLoader, SimpleCalculatorKJ, PrimitiveInt, Float to Int, GetImageSize, SolidMask, PrimitiveFloat, GetLatentSizeAndCount, SolidMask, SetLatentNoiseMask, LTXVLatentUpsampler, GetLatentSizeAndCount, SolidMask, SetLatentNoiseMask, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVAudioVAEEncode, Audio Duration (mtb), SamplerCustomAdvanced, DWPreprocessor, DisTorchPurgeVRAMV2, LTXVConcatAVLatent, VRAMReserver, RandomNoise, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, TrimAudioDuration, LoadAudio, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, ManualSigmas, ImageResizeKJv2, LTXVLatentUpsampler, ManualSigmas, VHS_VideoCombine, LatentUpscaleModelLoader, LatentUpscaleModelLoader, LTXVImgToVideoConditionOnly, ManualSigmas, SaveVideo, VHS_VideoCombine, VHS_LoadVideo, LoadImage, ImageResizeKJv2, SetLatentNoiseMask]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 音频驱动参考角色伪替换工作流_2040718940661354497.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `DownloadAndLoadDepthCrafterModel`
- `easy showAnything`
- `easy showAnything`
- `CM_FloatToInt`
- `VHS_VideoInfoLoaded`
- `CannyEdgePreprocessor`
- `DepthCrafter`
- `EmptyLTXVLatentVideo`
- `PreviewImage`
- `SimpleMath+`
- `PrimitiveBoolean`
- `PreviewImage`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoConditionOnly`
- `ImageResizeKJv2`
- `LTXAddVideoICLoRAGuide`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `SimpleCalculatorKJ`
- `PrimitiveInt`
- `Float to Int`
- `GetImageSize`
- `SolidMask`
- `PrimitiveFloat`
- `GetLatentSizeAndCount`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVAudioVAEEncode` ★核心
- `Audio Duration (mtb)`
- `SamplerCustomAdvanced` ★核心
- `DWPreprocessor`
- `DisTorchPurgeVRAMV2`
- `LTXVConcatAVLatent`
- `VRAMReserver`
- `RandomNoise`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TrimAudioDuration`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ManualSigmas`
- `ImageResizeKJv2`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoConditionOnly`
- `ManualSigmas`
- `SaveVideo`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJv2`
- `SetLatentNoiseMask`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **94%**（92/98）

**有卡**：`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`DownloadAndLoadDepthCrafterModel`、`CM_FloatToInt`、`VHS_VideoInfoLoaded`、`CannyEdgePreprocessor`、`DepthCrafter`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`PrimitiveBoolean`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVCropGuides`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`VAELoaderKJ`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`LTXAddVideoICLoRAGuide`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTX2_NAG`、`CreateVideo`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`SimpleCalculatorKJ`、`Float to Int`、`GetImageSize`、`SolidMask`、`GetLatentSizeAndCount`、`SetLatentNoiseMask`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXVAudioVAEEncode`、`Audio Duration (mtb)`、`DWPreprocessor`、`DisTorchPurgeVRAMV2`、`VRAMReserver`、`TrimAudioDuration`、`LoadAudio`、`CLIPTextEncode`、`VHS_VideoCombine`、`ManualSigmas`、`LatentUpscaleModelLoader`、`SaveVideo`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、DepthCrafter
