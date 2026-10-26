---
key: 数字人/数字人/LTX2.3脱口秀_2051279560964096002.json
name: LTX2.3脱口秀_2051279560964096002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3脱口秀_2051279560964096002.json
hash: 2c152df0a2f94c8c
coverage: 0.944444
learned_at: 2026-10-26 01:56:10
nodes: [VAELoaderKJ, PrimitiveInt, LTXVLatentUpsampler, LTXVCropGuides, easy getNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy getNode, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, easy getNode, LTXVSeparateAVLatent, easy getNode, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, LTX2_NAG, VisualizeSigmasKJ, VAELoader, LTX2SamplingPreviewOverride, KSamplerSelect, LTXVConditioning, easy getNode, LTXVSeparateAVLatent, easy getNode, LTXVAudioVAEDecode, VAEDecode, DualCLIPLoader, easy setNode, easy setNode, easy setNode, easy setNode, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, EmptyLTXVLatentVideo, easy getNode, easy getNode, easy getNode, SimpleMath+, easy setNode, CLIPTextEncode, ConditioningZeroOut, easy getNode, BasicScheduler, ModelSamplingSD3, PathchSageAttentionKJ, easy getNode, VRAMReserver, SamplerCustom, MuyeTextEditOutput, VAELoaderKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, Int, PrimitiveBoolean, Int, VHS_VideoCombine, Reroute, DF_Int_to_Float, CLIPTextEncode, Int, LTXVEmptyLatentAudio, LoadImage, ImageResizeKJv2, LTXVPreprocess, LatentUpscaleModelLoader, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/LTX2.3脱口秀_2051279560964096002.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3脱口秀_2051279560964096002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（72 个）：
- `VAELoaderKJ`
- `PrimitiveInt`
- `LTXVLatentUpsampler` ★核心
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
- `easy getNode`
- `SimpleMath+`
- `easy setNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `easy getNode`
- `BasicScheduler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `easy getNode`
- `VRAMReserver`
- `SamplerCustom` ★核心
- `MuyeTextEditOutput`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `Int`
- `PrimitiveBoolean`
- `Int`
- `VHS_VideoCombine`
- `Reroute`
- `DF_Int_to_Float`
- `CLIPTextEncode` ★核心
- `Int`
- `LTXVEmptyLatentAudio` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LatentUpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（68/72）

**有卡**：`VAELoaderKJ`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`easy getNode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LTX2_NAG`、`VisualizeSigmasKJ`、`VAELoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`DualCLIPLoader`、`easy setNode`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`CLIPTextEncode`、`ConditioningZeroOut`、`BasicScheduler`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VRAMReserver`、`SamplerCustom`、`MuyeTextEditOutput`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`PrimitiveBoolean`、`DF_Int_to_Float`、`LTXVEmptyLatentAudio`、`LoadImage`、`ImageResizeKJv2`、`LTXVPreprocess`、`LatentUpscaleModelLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
