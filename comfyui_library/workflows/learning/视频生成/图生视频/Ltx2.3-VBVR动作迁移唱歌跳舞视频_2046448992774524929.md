---
key: 视频生成/图生视频/Ltx2.3-VBVR动作迁移唱歌跳舞视频_2046448992774524929.json
name: Ltx2.3-VBVR动作迁移唱歌跳舞视频_2046448992774524929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3-VBVR动作迁移唱歌跳舞视频_2046448992774524929.json
hash: bf72f727de39c792
coverage: 0.425439
learned_at: 2026-10-15 22:36:58
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ManualSigmas, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, SetNode, SetNode, SetNode, PrimitiveFloat, SimpleCalculatorKJ, GetNode, SetNode, SetNode, GetNode, LTXVPreprocess, GetNode, GetNode, GetNode, GetNode, GetImageSize, SimpleMath+, SetNode, GetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, DualCLIPLoaderGGUF, UnetLoaderGGUF, MarkdownNote, PathchSageAttentionKJ, LTXVChunkFeedForward, GetNode, CLIPTextEncode, Reroute, Reroute, GetNode, SetNode, RandomNoise, KSamplerSelect, LTXVConditioning, RandomNoise, LTXVCropGuides, LTXVLatentUpsampler, LTXVConcatAVLatent, SamplerCustomAdvanced, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, PrimitiveBoolean, LTX2AttentionTunerPatch, MarkdownNote, SetNode, SetNode, GetNode, SimpleCalculatorKJ, GetNode, GetNode, EmptyLTXVLatentVideo, SimpleCalculatorKJ, GetNode, GetNode, GetNode, SetNode, GetNode, PrimitiveFloat, SetNode, INTConstant, SetNode, GetNode, SetNode, MarkdownNote, MarkdownNote, MarkdownNote, SetNode, DepthAnythingPreprocessor, PrimitiveBoolean, CLIPTextEncode, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, SDPoseKeypointExtractor, ResizeImageMaskNode, ResizeImageMaskNode, CheckpointLoaderSimple, ResizeImageMaskNode, GetImageSizeAndCount, ResizeImageMaskNode, GetNode, ImageBlend, GetNode, SDPoseDrawKeypoints, ComfySwitchNode, INTConstant, INTConstant, PrimitiveFloat, GetNode, easy convertAnything, PrimitiveStringMultiline, TextGenerateLTX2Prompt, GetNode, LazySwitchKJ, SamplerCustomAdvanced, SetNode, GetNode, ManualSigmas, SeedGenerator, SolidMask, GetNode, GetNode, ComfySwitchNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, VHS_LoadVideoFFmpeg, GetNode, GetNode, GetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, ComfySwitchNode, SimpleCalculatorKJ, EmptyAudio, GetNode, ComfySwitchNode, SetNode, GetNode, ComfySwitchNode, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, SetNode, PrimitiveBoolean, Color Correct (mtb), GetNode, GetNode, CFGGuider, GetNode, GetNode, LTX2_NAG, PrimitiveBoolean, LoadAudio, TrimAudioDuration, SetNode, ImageResizeKJv2, SetNode, GetImageSize, ImageResizeKJv2, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, easy showAnything, SetNode, LTXVChunkFeedForward, CFGGuider, GetNode, LTXVConcatAVLatent, GetNode, SetNode, GetNode, GetNode, SetNode, LTX2SamplingPreviewOverride, LTXVImgToVideoInplace, LTXVImgToVideoConditionOnly, StringConcatenate, SetNode, PrimitiveStringMultiline, LTXVChunkFeedForward, LTXICLoRALoaderModelOnly, LTXAddVideoICLoRAGuide, GetNode, VAEDecodeTiled, GetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVEmptyLatentAudio, Switch image [Crystools], ColorMatch, ImageConcatMulti, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, VHS_VideoCombine, SetNode, LoraLoaderModelOnly, UnetLoaderGGUF, LoraLoaderModelOnly, LoadImage, GetNode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/Ltx2.3-VBVR动作迁移唱歌跳舞视频_2046448992774524929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046448992774524929.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（228 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `DualCLIPLoaderGGUF`
- `UnetLoaderGGUF` ★核心
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `GetNode`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `GetNode`
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveBoolean`
- `LTX2AttentionTunerPatch`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `DepthAnythingPreprocessor`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `SDPoseKeypointExtractor`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `CheckpointLoaderSimple` ★核心
- `ResizeImageMaskNode`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `GetNode`
- `ImageBlend`
- `GetNode`
- `SDPoseDrawKeypoints`
- `ComfySwitchNode`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `GetNode`
- `easy convertAnything`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `LazySwitchKJ`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `SeedGenerator`
- `SolidMask`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideoFFmpeg`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `ComfySwitchNode`
- `SimpleCalculatorKJ`
- `EmptyAudio`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `PrimitiveBoolean`
- `Color Correct (mtb)`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `PrimitiveBoolean`
- `LoadAudio`
- `TrimAudioDuration`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetImageSize`
- `ImageResizeKJv2`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `easy showAnything`
- `SetNode`
- `LTXVChunkFeedForward`
- `CFGGuider`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoConditionOnly`
- `StringConcatenate`
- `SetNode`
- `PrimitiveStringMultiline`
- `LTXVChunkFeedForward`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `Switch image [Crystools]`
- `ColorMatch`
- `ImageConcatMulti`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **43%**（97/228）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`SimpleCalculatorKJ`、`LTXVPreprocess`、`GetImageSize`、`SimpleMath+`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`DualCLIPLoaderGGUF`、`UnetLoaderGGUF`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`CLIPTextEncode`、`RandomNoise`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`PrimitiveBoolean`、`LTX2AttentionTunerPatch`、`EmptyLTXVLatentVideo`、`INTConstant`、`DepthAnythingPreprocessor`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`SDPoseKeypointExtractor`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`GetImageSizeAndCount`、`ImageBlend`、`SDPoseDrawKeypoints`、`easy convertAnything`、`TextGenerateLTX2Prompt`、`LazySwitchKJ`、`SeedGenerator`、`SolidMask`、`VHS_LoadVideoFFmpeg`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`EmptyAudio`、`VHS_VideoCombine`、`Color Correct (mtb)`、`CFGGuider`、`LTX2_NAG`、`LoadAudio`、`TrimAudioDuration`、`ImageResizeKJv2`、`LTX2SamplingPreviewOverride`、`LTXVImgToVideoInplace`、`LTXVImgToVideoConditionOnly`、`StringConcatenate`、`LTXICLoRALoaderModelOnly`、`LTXAddVideoICLoRAGuide`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`Switch image [Crystools]`、`ColorMatch`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、DepthAnythingPreprocessor、CFGGuider、KSamplerSelect
