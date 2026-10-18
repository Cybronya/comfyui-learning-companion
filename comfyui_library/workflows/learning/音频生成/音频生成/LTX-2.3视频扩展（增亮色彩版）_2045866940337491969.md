---
key: 音频生成/音频生成/LTX-2.3视频扩展（增亮色彩版）_2045866940337491969.json
name: LTX-2.3视频扩展（增亮色彩版）_2045866940337491969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX-2.3视频扩展（增亮色彩版）_2045866940337491969.json
hash: 540e73126119fe35
coverage: 0.406015
learned_at: 2026-10-18 03:04:51
nodes: [LTXVConditioning, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXAddVideoICLoRAGuide, LTXVCropGuides, ManualSigmas, ResizeImageMaskNode, VHS_VideoInfo, ImagePadKJ, SetNode, SetNode, SetNode, VAELoader, SetNode, LTX2AttentionTunerPatch, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2SamplingPreviewOverride, GetNode, ComfyMathExpression, SetNode, INTConstant, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, PreviewAny, GetImageRangeFromBatch, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, PreviewImage, GetImageRangeFromBatch, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, MarkdownNote, ComfySwitchNode, GetNode, SetNode, GetNode, SetNode, GetNode, Color Correct (mtb), ResizeImageMaskNode, GetImageSizeAndCount, PrimitiveStringMultiline, LazySwitchKJ, TextGenerateLTX2Prompt, Reroute, StringConcatenate, Color Correct (mtb), SetNode, GetNode, SimpleMath+, INTConstant, LTXICLoRALoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, SetNode, DualCLIPLoader, VAELoader, VAELoaderKJ, GetNode, PrimitiveBoolean, easy showAnything, PrimitiveBoolean, INTConstant, INTConstant, PrimitiveStringMultiline, VHS_VideoCombine, INTConstant, VHS_LoadVideoFFmpeg, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 音频生成/音频生成/LTX-2.3视频扩展（增亮色彩版）_2045866940337491969.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX-2.3视频扩展（增亮色彩版）_2045866940337491969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（133 个）：
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVCropGuides`
- `ManualSigmas`
- `ResizeImageMaskNode`
- `VHS_VideoInfo`
- `ImagePadKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `LTX2AttentionTunerPatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `INTConstant`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Color Correct (mtb)`
- `ResizeImageMaskNode`
- `GetImageSizeAndCount`
- `PrimitiveStringMultiline`
- `LazySwitchKJ`
- `TextGenerateLTX2Prompt`
- `Reroute`
- `StringConcatenate`
- `Color Correct (mtb)`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `GetNode`
- `PrimitiveBoolean`
- `easy showAnything`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `INTConstant`
- `VHS_LoadVideoFFmpeg`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **41%**（54/133）

**有卡**：`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`LTXVCropGuides`、`ManualSigmas`、`ResizeImageMaskNode`、`VHS_VideoInfo`、`ImagePadKJ`、`VAELoader`、`LTX2AttentionTunerPatch`、`LTX2SamplingPreviewOverride`、`ComfyMathExpression`、`INTConstant`、`LTX2_NAG`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`Color Correct (mtb)`、`GetImageSizeAndCount`、`LazySwitchKJ`、`TextGenerateLTX2Prompt`、`StringConcatenate`、`SimpleMath+`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`PrimitiveBoolean`、`VHS_VideoCombine`、`VHS_LoadVideoFFmpeg`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
