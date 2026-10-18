---
key: 视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json
name: LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json
hash: e15cd48f97afa88b
coverage: 0.569767
learned_at: 2026-10-15 22:34:42
nodes: [KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVScheduler, Fast Groups Bypasser (rgthree), MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, EmptyImage, ImageScaleBy, GetImageSize, EmptyLTXVLatentVideo, LayerUtility: PurgeVRAM V2, RandomNoise, CFGGuider, KSamplerSelect, Int, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, Reroute, CheckpointLoaderSimple, Reroute, LTXVConcatAVLatent, Reroute, LTXVAudioVAELoader, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVConditioning, Reroute, Reroute, LTXVPreprocess, Reroute, LatentUpscaleModelLoader, Reroute, Reroute, LoraLoaderModelOnly, CLIPTextEncode, CFGGuider, Reroute, Reroute, LoraLoaderModelOnly, Reroute, Reroute, Reroute, LTXVSeparateAVLatent, Reroute, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, Qwen3_VQA, Reroute, ManualSigmas, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, Reroute, ShowText|pysssss, LTXAVTextEncoderLoader, PrimitiveNode, easy showAnything, JoinStrings, CLIPTextEncode, TextInput_, TextInput_, Int, JoinStrings, easy cleanGpuUsed, TextInput_, VAEDecodeTiled, easy cleanGpuUsed, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 121}
---

# 视频生成/图生视频/LH-DMT-LTX2.0-007.LTX2.0-图生视频（优化版）全自动反推提示词_2016324555433840641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016324555433840641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（86 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVScheduler`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LayerUtility: PurgeVRAM V2`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Int`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVAudioVAELoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `Reroute`
- `LatentUpscaleModelLoader`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `Qwen3_VQA`
- `Reroute`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `ShowText|pysssss`
- `LTXAVTextEncoderLoader`
- `PrimitiveNode`
- `easy showAnything`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `TextInput_`
- `TextInput_`
- `Int`
- `JoinStrings`
- `easy cleanGpuUsed`
- `TextInput_`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **57%**（49/86）

**有卡**：`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVScheduler`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LayerUtility: PurgeVRAM V2`、`CFGGuider`、`Int`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`CheckpointLoaderSimple`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`LTXVCropGuides`、`LTXVConditioning`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`Qwen3_VQA`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`JoinStrings`、`TextInput_`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
