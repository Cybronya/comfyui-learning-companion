---
key: 视频生成/图生视频/【运镜+自动脚本】图生视频 LTXV 2.0-19B 测试版_2008778999371145217.json
name: 【运镜+自动脚本】图生视频 LTXV 2.0-19B 测试版_2008778999371145217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【运镜+自动脚本】图生视频 LTXV 2.0-19B 测试版_2008778999371145217.json
hash: a0ac889e9d7ac8bb
coverage: 0.8375
learned_at: 2026-10-15 22:34:09
nodes: [LTXVScheduler, KSamplerSelect, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewImage, intToFloat _O, VAEDecode, LTXVAudioVAELoader, LTXVAudioVAEDecode, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, Int, Int, Int, Int, Int, Int, CLIPTextEncode, LoraLoaderModelOnly, ImpactSwitch, LTXAVTextEncoderLoader, CLIPTextEncode, easy showAnything, LoraLoaderModelOnly, CR Text Replace, MarkdownNote, CheckpointLoaderSimple, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVLatentUpsampler, LatentUpscaleModelLoader, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, SaveVideo, Textbox, LTXVCropGuides, MarkdownNote, LoraLoaderModelOnly, LTXVConditioning, easy cleanGpuUsed, RH_Captioner, easy cleanGpuUsed, LTXVPreprocess, VAEDecode, easy showAnything, SaveVideo, easy showAnything, LoraLoaderModelOnly, easy promptLine, Textbox, LoadImage, MarkdownNote, MarkdownNote, MathExpression|pysssss, Int, PreviewImage, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy showAnything, MarkdownNote, MarkdownNote, Int, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustom]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/【运镜+自动脚本】图生视频 LTXV 2.0-19B 测试版_2008778999371145217.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008778999371145217.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PreviewImage`
- `intToFloat _O`
- `VAEDecode` ★核心
- `LTXVAudioVAELoader`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactSwitch`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `CR Text Replace`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `Textbox`
- `LTXVCropGuides`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `LTXVPreprocess`
- `VAEDecode` ★核心
- `easy showAnything`
- `SaveVideo`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `easy promptLine`
- `Textbox`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MathExpression|pysssss`
- `Int`
- `PreviewImage`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `easy showAnything`
- `MarkdownNote`
- `MarkdownNote`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustom` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **84%**（67/80）

**有卡**：`LTXVScheduler`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`intToFloat _O`、`VAEDecode`、`LTXVAudioVAELoader`、`LTXVAudioVAEDecode`、`CreateVideo`、`LoraLoaderModelOnly`、`Int`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`CR Text Replace`、`CheckpointLoaderSimple`、`ManualSigmas`、`LTXVSeparateAVLatent`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`SaveVideo`、`Textbox`、`LTXVCropGuides`、`LTXVConditioning`、`easy cleanGpuUsed`、`RH_Captioner`、`LTXVPreprocess`、`easy promptLine`、`LoadImage`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustom`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
