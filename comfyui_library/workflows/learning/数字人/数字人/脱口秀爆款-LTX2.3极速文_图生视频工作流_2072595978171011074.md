---
key: 数字人/数字人/脱口秀爆款-LTX2.3极速文_图生视频工作流_2072595978171011074.json
name: 脱口秀爆款-LTX2.3极速文_图生视频工作流_2072595978171011074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/脱口秀爆款-LTX2.3极速文_图生视频工作流_2072595978171011074.json
hash: 797ce9721a4e576f
coverage: 0.945205
learned_at: 2026-10-26 02:04:24
nodes: [DualCLIPLoader, easy setNode, Int, easy setNode, easy setNode, easy setNode, Int, Int, VAELoaderKJ, VAELoaderKJ, ImageResizeKJv2, PrimitiveBoolean, PrimitiveInt, LTXVPreprocess, VRAMReserver, easy setNode, UNETLoader, PathchSageAttentionKJ, EmptyLTXVLatentVideo, SimpleMath+, ModelSamplingSD3, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, VisualizeSigmasKJ, LTXVEmptyLatentAudio, easy getNode, LTXVImgToVideoConditionOnly, easy getNode, easy getNode, ConditioningZeroOut, VAELoader, LTXVConcatAVLatent, KSamplerSelect, easy getNode, LTXVSeparateAVLatent, DF_Int_to_Float, easy getNode, VAEDecode, LTXVAudioVAEDecode, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, easy getNode, LTXVLatentUpsampler, ManualSigmas, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy getNode, easy getNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, Reroute, SamplerCustomAdvanced, VHS_VideoCombine, CLIPTextEncode, Fast Groups Bypasser (rgthree), CLIPTextEncode, CLIPTextEncode, easy getNode, easy getNode, PrimitiveInt, CLIPTextEncode, LoadImage, RandomNoise, CFGGuider, LatentUpscaleModelLoader, LTXVCropGuides, VHS_VideoCombine, easy getNode, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/脱口秀爆款-LTX2.3极速文_图生视频工作流_2072595978171011074.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/脱口秀爆款-LTX2.3极速文_图生视频工作流_2072595978171011074.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（73 个）：
- `DualCLIPLoader`
- `easy setNode`
- `Int`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `Int`
- `Int`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `LTXVPreprocess`
- `VRAMReserver`
- `easy setNode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `ModelSamplingSD3`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `easy getNode`
- `LTXVImgToVideoConditionOnly`
- `easy getNode`
- `easy getNode`
- `ConditioningZeroOut`
- `VAELoader`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `easy getNode`
- `LTXVSeparateAVLatent`
- `DF_Int_to_Float`
- `easy getNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `easy getNode`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `easy getNode`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `RandomNoise`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `VHS_VideoCombine`
- `easy getNode`
- `VAEDecode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（69/73）

**有卡**：`DualCLIPLoader`、`easy setNode`、`Int`、`VAELoaderKJ`、`ImageResizeKJv2`、`PrimitiveBoolean`、`LTXVPreprocess`、`VRAMReserver`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`ModelSamplingSD3`、`BasicScheduler`、`LoraLoaderModelOnly`、`LTX2_NAG`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`easy getNode`、`LTXVImgToVideoConditionOnly`、`ConditioningZeroOut`、`VAELoader`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`DF_Int_to_Float`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`RandomNoise`、`CFGGuider`、`LatentUpscaleModelLoader`、`LTXVCropGuides`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
