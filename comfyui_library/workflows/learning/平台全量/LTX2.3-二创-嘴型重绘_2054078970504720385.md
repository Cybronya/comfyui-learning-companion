---
key: 平台全量/LTX2.3-二创-嘴型重绘_2054078970504720385.json
name: LTX2.3-二创-嘴型重绘_2054078970504720385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3-二创-嘴型重绘_2054078970504720385.json
hash: aea8ace87586395d
coverage: 0.94
learned_at: 2026-11-14 00:38:07
nodes: [VAELoaderKJ, easy getNode, DualCLIPLoader, VAELoaderKJ, MarkdownNote, LoadImage, SamplerCustom, easy getNode, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, LTXVCropGuides, VHS_VideoCombine, KSamplerSelect, easy getNode, ConditioningZeroOut, easy getNode, easy showAnything, ComfyMathExpression, easy showAnything, DF_Int_to_Float, CLIPTextEncode, VAELoader, VHS_VideoInfoLoaded, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, UNETLoader, easy setNode, VRAMReserver, LTXVAudioVAEEncode, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVConcatAVLatent, LTX2SamplingPreviewOverride, ModelSamplingSD3, BasicScheduler, VisualizeSigmasKJ, VHS_LoadVideo, EmptyLTXVLatentVideo, LTXICLoRALoaderModelOnly, Int, Int, Int, CR Text, LTXVSetAudioRefTokens, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 平台全量/LTX2.3-二创-嘴型重绘_2054078970504720385.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3-二创-嘴型重绘_2054078970504720385.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（50 个）：
- `VAELoaderKJ`
- `easy getNode`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `MarkdownNote`
- `LoadImage`
- `SamplerCustom` ★核心
- `easy getNode`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `easy getNode`
- `ConditioningZeroOut`
- `easy getNode`
- `easy showAnything`
- `ComfyMathExpression`
- `easy showAnything`
- `DF_Int_to_Float`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VHS_VideoInfoLoaded`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `UNETLoader` ★核心
- `easy setNode`
- `VRAMReserver`
- `LTXVAudioVAEEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTX2SamplingPreviewOverride`
- `ModelSamplingSD3`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `VHS_LoadVideo`
- `EmptyLTXVLatentVideo`
- `LTXICLoRALoaderModelOnly` ★核心
- `Int`
- `Int`
- `Int`
- `CR Text`
- `LTXVSetAudioRefTokens`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（47/50）

**有卡**：`VAELoaderKJ`、`easy getNode`、`DualCLIPLoader`、`LoadImage`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`VHS_VideoCombine`、`KSamplerSelect`、`ConditioningZeroOut`、`ComfyMathExpression`、`DF_Int_to_Float`、`CLIPTextEncode`、`VAELoader`、`VHS_VideoInfoLoaded`、`easy setNode`、`UNETLoader`、`VRAMReserver`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTX2SamplingPreviewOverride`、`ModelSamplingSD3`、`BasicScheduler`、`VisualizeSigmasKJ`、`VHS_LoadVideo`、`EmptyLTXVLatentVideo`、`LTXICLoRALoaderModelOnly`、`Int`、`CR Text`、`LTXVSetAudioRefTokens`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
