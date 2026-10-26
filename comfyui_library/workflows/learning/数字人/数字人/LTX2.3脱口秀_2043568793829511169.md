---
key: 数字人/数字人/LTX2.3脱口秀_2043568793829511169.json
name: LTX2.3脱口秀_2043568793829511169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3脱口秀_2043568793829511169.json
hash: feb0336a6043e508
coverage: 0.932432
learned_at: 2026-10-26 01:56:09
nodes: [VAELoaderKJ, PrimitiveInt, ImageResizeKJv2, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVCropGuides, easy getNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy getNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, easy getNode, LTXVSeparateAVLatent, easy getNode, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, LTX2_NAG, VisualizeSigmasKJ, VAELoader, LTX2SamplingPreviewOverride, KSamplerSelect, LTXVConditioning, easy getNode, LTXVSeparateAVLatent, easy getNode, LTXVAudioVAEDecode, VAEDecode, DualCLIPLoader, easy setNode, easy setNode, easy setNode, easy setNode, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, EmptyLTXVLatentVideo, easy getNode, easy getNode, LTXVEmptyLatentAudio, easy getNode, SimpleMath+, easy setNode, LTXVPreprocess, Fast Groups Bypasser (rgthree), CLIPTextEncode, ConditioningZeroOut, easy getNode, BasicScheduler, ModelSamplingSD3, PathchSageAttentionKJ, easy getNode, VRAMReserver, SamplerCustom, CLIPTextEncode, MuyeTextEditOutput, MarkdownNote, VAELoaderKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, PrimitiveInt, Int, Int, PrimitiveBoolean, Int, VHS_VideoCombine, Reroute, DF_Int_to_Float, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3脱口秀_2043568793829511169.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3脱口秀_2043568793829511169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（74 个）：
- `VAELoaderKJ`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `easy getNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `easy getNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `easy getNode`
- `LTXVSeparateAVLatent`
- `easy getNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LTX2_NAG`
- `VisualizeSigmasKJ`
- `VAELoader`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `easy getNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `easy getNode`
- `easy getNode`
- `LTXVEmptyLatentAudio` ★核心
- `easy getNode`
- `SimpleMath+`
- `easy setNode`
- `LTXVPreprocess`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `easy getNode`
- `BasicScheduler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `easy getNode`
- `VRAMReserver`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `MuyeTextEditOutput`
- `MarkdownNote`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PrimitiveInt`
- `Int`
- `Int`
- `PrimitiveBoolean`
- `Int`
- `VHS_VideoCombine`
- `Reroute`
- `DF_Int_to_Float`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（69/74）

**有卡**：`VAELoaderKJ`、`ImageResizeKJv2`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`easy getNode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LTX2_NAG`、`VisualizeSigmasKJ`、`VAELoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`DualCLIPLoader`、`easy setNode`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`LTXVPreprocess`、`CLIPTextEncode`、`ConditioningZeroOut`、`BasicScheduler`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VRAMReserver`、`SamplerCustom`、`MuyeTextEditOutput`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`Int`、`PrimitiveBoolean`、`DF_Int_to_Float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
