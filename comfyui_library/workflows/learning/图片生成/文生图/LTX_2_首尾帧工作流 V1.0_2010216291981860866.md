---
key: 图片生成/文生图/LTX_2_首尾帧工作流 V1.0_2010216291981860866.json
name: LTX_2_首尾帧工作流 V1.0_2010216291981860866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX_2_首尾帧工作流 V1.0_2010216291981860866.json
hash: 27ae6aee0dcd0082
coverage: 0.890909
learned_at: 2026-10-19 22:00:35
nodes: [KSamplerSelect, LTXVCropGuides, CFGGuider, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, LTXVAudioVAELoader, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CFGGuider, LTXVPreprocess, RandomNoise, LatentUpscaleModelLoader, LTXVScheduler, BetaSamplingScheduler, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, LTXVFirstLastFrameControl_TTP, LoraLoaderModelOnly, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, CheckpointLoaderSimple, MarkdownNote, VAEDecode, LTXVAudioVAEDecode, PrimitiveNode, MarkdownNote, MarkdownNote, GetImageSize, EmptyImage, ImageScaleBy, GetImageSize, PrimitiveInt, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVFirstLastFrameControl_TTP, LTXVLatentUpsampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, MemoryCleaner, MemoryCleaner, CLIPTextEncode, RH_LLMAPI_Pro_Node, PreviewAny, VHS_VideoCombine, LoadImage, LoadImage, AILab_QwenVL, CR Multiline Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 图片生成/文生图/LTX_2_首尾帧工作流 V1.0_2010216291981860866.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX_2_首尾帧工作流 V1.0_2010216291981860866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVPreprocess`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVScheduler`
- `BetaSamplingScheduler`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `LTXVFirstLastFrameControl_TTP`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveNode`
- `MarkdownNote`
- `MarkdownNote`
- `GetImageSize`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `MemoryCleaner`
- `MemoryCleaner`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `AILab_QwenVL`
- `CR Multiline Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`RandomNoise`、`LatentUpscaleModelLoader`、`LTXVScheduler`、`BetaSamplingScheduler`、`LTXVFirstLastFrameControl_TTP`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`ManualSigmas`、`CheckpointLoaderSimple`、`VAEDecode`、`LTXVAudioVAEDecode`、`GetImageSize`、`EmptyImage`、`ImageScaleBy`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXAVTextEncoderLoader`、`MemoryCleaner`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LoadImage`、`AILab_QwenVL`、`CR Multiline Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
