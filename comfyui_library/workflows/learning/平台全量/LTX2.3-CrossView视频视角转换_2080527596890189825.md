---
key: 平台全量/LTX2.3-CrossView视频视角转换_2080527596890189825.json
name: LTX2.3-CrossView视频视角转换_2080527596890189825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3-CrossView视频视角转换_2080527596890189825.json
hash: 87026ad411a7866b
coverage: 0.656566
learned_at: 2026-11-14 00:37:58
nodes: [LTX2MemoryEfficientSageAttentionPatch, ModelPatchTorchSettings, LTXVChunkFeedForward, FloatConstant, LTXVConditioning, LTX2_NAG, LTX2SamplingPreviewOverride, SetNode, PathchSageAttentionKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, FL_FloatToInt, SetNode, SetNode, SetNode, CLIPTextEncode, SetNode, SetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, AddLabel, AddLabel, GetNode, StringConcatenate, GetNode, GetNode, SetNode, Seed (rgthree), TextBox1, INTConstant, GetImageSizeAndCount, SetNode, ReverseImageBatch, MarkdownNote, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecode, SamplerCustomAdvanced, LTXVPreprocess, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LatentUpscaleModelLoader, LTXVLatentUpsampler, RandomNoise, LTXVImgToVideoConditionOnly, LTXVAudioVAEDecode, KSamplerSelect, LTXVConcatAVLatent, CFGGuider, RandomNoise, VAEDecode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXAddVideoICLoRAGuide, ManualSigmas, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, VAELoader, LTXICLoRALoaderModelOnly, VHS_VideoCombine, INTConstant, INTConstant, AddLabel, easy convertAnything, ImageConcanate, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3-CrossView视频视角转换_2080527596890189825.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3-CrossView视频视角转换_2080527596890189825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（99 个）：
- `LTX2MemoryEfficientSageAttentionPatch`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `FloatConstant`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `FL_FloatToInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `AddLabel`
- `AddLabel`
- `GetNode`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `SetNode`
- `Seed (rgthree)`
- `TextBox1`
- `INTConstant`
- `GetImageSizeAndCount`
- `SetNode`
- `ReverseImageBatch`
- `MarkdownNote`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `LTXVImgToVideoConditionOnly`
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXAddVideoICLoRAGuide`
- `ManualSigmas`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `VAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `AddLabel`
- `easy convertAnything`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（65/99）

**有卡**：`LTX2MemoryEfficientSageAttentionPatch`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`FloatConstant`、`LTXVConditioning`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`PathchSageAttentionKJ`、`FL_FloatToInt`、`CLIPTextEncode`、`ImageResizeKJv2`、`AddLabel`、`StringConcatenate`、`Seed (rgthree)`、`TextBox1`、`INTConstant`、`GetImageSizeAndCount`、`ReverseImageBatch`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecode`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXAddVideoICLoRAGuide`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`LTXICLoRALoaderModelOnly`、`VHS_VideoCombine`、`easy convertAnything`、`ImageConcanate`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler
