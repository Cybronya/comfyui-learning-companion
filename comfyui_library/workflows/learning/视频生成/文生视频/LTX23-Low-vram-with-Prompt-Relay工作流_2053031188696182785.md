---
key: 视频生成/文生视频/LTX23-Low-vram-with-Prompt-Relay工作流_2053031188696182785.json
name: LTX23-Low-vram-with-Prompt-Relay工作流_2053031188696182785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX23-Low-vram-with-Prompt-Relay工作流_2053031188696182785.json
hash: f387981539a616a4
coverage: 0.54717
learned_at: 2026-10-10 23:00:26
nodes: [SetNode, SetNode, SimpleCalculatorKJ, GetNode, GetNode, SetNode, CM_FloatToInt, SetNode, GetNode, GetNode, LTXVAddGuide, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, SetNode, Any Switch (rgthree), SetNode, LTXVEmptyLatentAudio, GetNode, VHS_VideoCombine, LTXVPreprocess, LTX2AttentionTunerPatch, PathchSageAttentionKJ, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, CLIPTextEncode, PrimitiveFloat, Fast Groups Bypasser (rgthree), EmptyLTXVLatentVideo, INTConstant, Note, SetNode, Any Switch (rgthree), LTX2_NAG, RandomNoise, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, RandomNoise, LTX2AudioLatentNormalizingSampling, LTXVAddGuide, LTXVCropGuides, VAEDecode, LTXVSeparateAVLatent, GetNode, LTXVAudioVAEDecode, GetNode, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, VAEDecodeTiled, RandomNoise, GetNode, GetNode, LTXVLatentUpsampler, LTXVConcatAVLatent, GetNode, CFGGuider, KSamplerSelect, GetNode, GetNode, VAEDecode, SetNode, SetNode, GetNode, ManualSigmas, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTX2AudioLatentNormalizingSampling, SamplerCustomAdvanced, SetNode, CLIPTextEncode, SetNode, Note, UnetLoaderGGUF, DualCLIPLoaderGGUF, Note, VAELoaderKJ, VAELoaderKJ, PromptRelayEncode, LatentUpscaleModelLoader, VHS_VideoCombine, VHS_VideoCombine, ResizeImageMaskNode, SetNode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 49}
---

# 视频生成/文生视频/LTX23-Low-vram-with-Prompt-Relay工作流_2053031188696182785.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX23-Low-vram-with-Prompt-Relay工作流_2053031188696182785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（106 个）：
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `CM_FloatToInt`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAddGuide`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `LTXVPreprocess`
- `LTX2AttentionTunerPatch`
- `PathchSageAttentionKJ`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `Note`
- `SetNode`
- `Any Switch (rgthree)`
- `LTX2_NAG`
- `RandomNoise`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTX2AudioLatentNormalizingSampling`
- `LTXVAddGuide`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTX2AudioLatentNormalizingSampling`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `Note`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoaderGGUF`
- `Note`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `PromptRelayEncode`
- `LatentUpscaleModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ResizeImageMaskNode`
- `SetNode`
- `LoadImage`

## 关键参数

- `width` = `49`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（58/106）

**有卡**：`SimpleCalculatorKJ`、`CM_FloatToInt`、`LTXVAddGuide`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`LTXVPreprocess`、`LTX2AttentionTunerPatch`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`INTConstant`、`LTX2_NAG`、`RandomNoise`、`LTX2AudioLatentNormalizingSampling`、`LTXVCropGuides`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`UnetLoaderGGUF`、`DualCLIPLoaderGGUF`、`VAELoaderKJ`、`PromptRelayEncode`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`LoadImage`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
