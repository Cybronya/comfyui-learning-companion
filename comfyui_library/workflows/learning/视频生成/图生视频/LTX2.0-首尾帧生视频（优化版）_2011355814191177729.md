---
key: 视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）_2011355814191177729.json
name: LTX2.0-首尾帧生视频（优化版）_2011355814191177729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2011355814191177729.json
hash: c2d92a0cca95df94
coverage: 0.553191
learned_at: 2026-10-15 22:34:22
nodes: [CFGGuider, KSamplerSelect, ManualSigmas, RandomNoise, Qwen3_VQA, PrimitiveInt, KSamplerSelect, LTXVScheduler, EmptyLTXVLatentVideo, LTXVCropGuides, RandomNoise, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVPreprocess, Reroute, Reroute, Reroute, LTXVPreprocess, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, Reroute, Reroute, ShowText|pysssss, CFGGuider, Reroute, Reroute, LTXVConditioning, Reroute, LTXVSeparateAVLatent, PrimitiveNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, Reroute, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, MarkdownNote, Reroute, VRAMReserver, SamplerCustomAdvanced, VAEDecodeTiled, LTXVFirstLastFrameControl_TTP, LoraLoaderModelOnly, Reroute, Reroute, LatentUpscaleModelLoader, Reroute, MemoryCleaner, LoraLoaderModelOnly, MemoryCleaner, Reroute, Reroute, LTXVLatentUpsampler, Reroute, LTXVAudioVAELoader, Reroute, LTXVFirstLastFrameControl_TTP, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetImageSize, ImageScaleBy, ImageConcatMulti, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, LTXVEmptyLatentAudio, JoinStrings, easy showAnything, PreviewImage, CLIPTextEncode, VHS_VideoCombine, LoadImage, LoadImage, CLIPTextEncode, TextInput_, TextInput_, Fast Groups Bypasser (rgthree), Int, Int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.0-首尾帧生视频（优化版）_2011355814191177729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011355814191177729.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `Qwen3_VQA`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `EmptyLTXVLatentVideo`
- `LTXVCropGuides`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `ShowText|pysssss`
- `CFGGuider`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `LTXVSeparateAVLatent`
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `MarkdownNote`
- `Reroute`
- `VRAMReserver`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVFirstLastFrameControl_TTP`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `LatentUpscaleModelLoader`
- `Reroute`
- `MemoryCleaner`
- `LoraLoaderModelOnly` ★核心
- `MemoryCleaner`
- `Reroute`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `LTXVAudioVAELoader`
- `Reroute`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetImageSize`
- `ImageScaleBy`
- `ImageConcatMulti`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVEmptyLatentAudio` ★核心
- `JoinStrings`
- `easy showAnything`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `Int`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（52/94）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`Qwen3_VQA`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VRAMReserver`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVFirstLastFrameControl_TTP`、`LatentUpscaleModelLoader`、`MemoryCleaner`、`LTXVLatentUpsampler`、`LTXVAudioVAELoader`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`GetImageSize`、`ImageScaleBy`、`ImageConcatMulti`、`EmptyImage`、`LTXVEmptyLatentAudio`、`JoinStrings`、`CLIPTextEncode`、`VHS_VideoCombine`、`LoadImage`、`TextInput_`、`Int`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
