---
key: 平台全量/LTX2.3 ic lipdub_嘴型控制_2067897379860336642.json
name: LTX2.3 ic lipdub_嘴型控制_2067897379860336642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 ic lipdub_嘴型控制_2067897379860336642.json
hash: ccd429f6c7258023
coverage: 0.885714
learned_at: 2026-11-14 00:37:35
nodes: [Reroute, Note, Note, Note, Note, RandomNoise, PlaySound|pysssss, Note, Label (rgthree), Fast Groups Muter (rgthree), LTXVLatentUpsampler, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, VHS_VideoCombine, LTXVCropGuides, LTXVAudioVAEDecode, VAEDecodeTiled, Note, ModelPatchTorchSettings, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSetAudioRefTokens, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVSetAudioRefTokens, LTXVCropGuides, LTXVAudioVAEDecode, PlaySound|pysssss, LTXAddVideoICLoRAGuide, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, VHS_VideoCombine, RandomNoise, UNETLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, VAELoaderKJ, DualCLIPLoaderGGUF, LatentUpscaleModelLoader, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, VAELoaderKJ, VHS_LoadVideo, ComfyMathExpression, VHS_VideoInfo, ResizeImageMaskNode, ResizeImageMaskNode, ComfyMathExpression, ImageScaleToMaxDimension, PromptRelayEncodeTimeline, LTXVConcatAVLatent, LTXVTiledVAEDecode, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVEnhanceAVideoKJ, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVChunkFeedForward, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3 ic lipdub_嘴型控制_2067897379860336642.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 ic lipdub_嘴型控制_2067897379860336642.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（70 个）：
- `Reroute`
- `Note`
- `Note`
- `Note`
- `Note`
- `RandomNoise`
- `PlaySound|pysssss`
- `Note`
- `Label (rgthree)`
- `Fast Groups Muter (rgthree)`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VHS_VideoCombine`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `ModelPatchTorchSettings`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSetAudioRefTokens`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `LTXVSetAudioRefTokens`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `PlaySound|pysssss`
- `LTXAddVideoICLoRAGuide`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `RandomNoise`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAELoaderKJ`
- `DualCLIPLoaderGGUF`
- `LatentUpscaleModelLoader`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `ComfyMathExpression`
- `VHS_VideoInfo`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ImageScaleToMaxDimension`
- `PromptRelayEncodeTimeline`
- `LTXVConcatAVLatent`
- `LTXVTiledVAEDecode` ★核心
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVEnhanceAVideoKJ`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（62/70）

**有卡**：`RandomNoise`、`PlaySound|pysssss`、`Label (rgthree)`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`VHS_VideoCombine`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ModelPatchTorchSettings`、`CFGGuider`、`LTXVSetAudioRefTokens`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoaderGGUF`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`VHS_LoadVideo`、`VHS_VideoInfo`、`ResizeImageMaskNode`、`ImageScaleToMaxDimension`、`PromptRelayEncodeTimeline`、`LTXVTiledVAEDecode`、`LTXVEnhanceAVideoKJ`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、SamplerCustomAdvanced、EmptyLTXVLatentVideo
