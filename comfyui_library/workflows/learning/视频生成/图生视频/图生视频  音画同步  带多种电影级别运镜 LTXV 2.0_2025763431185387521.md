---
key: 视频生成/图生视频/图生视频  音画同步  带多种电影级别运镜 LTXV 2.0_2025763431185387521.json
name: 图生视频  音画同步  带多种电影级别运镜 LTXV 2.0_2025763431185387521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频  音画同步  带多种电影级别运镜 LTXV 2.0_2025763431185387521.json
hash: 10065420a097f86c
coverage: 0.848485
learned_at: 2026-10-15 22:35:12
nodes: [LTXVScheduler, KSamplerSelect, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewImage, intToFloat _O, VAEDecode, LTXVAudioVAELoader, LTXVAudioVAEDecode, CreateVideo, Int, Int, Int, Int, Int, Int, Int, LTXAVTextEncoderLoader, CLIPTextEncode, easy showAnything, LoraLoaderModelOnly, CR Text Replace, CheckpointLoaderSimple, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, RandomNoise, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVLatentUpsampler, LatentUpscaleModelLoader, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, SaveVideo, Textbox, LTXVCropGuides, LTXVConditioning, easy cleanGpuUsed, RH_Captioner, easy cleanGpuUsed, LTXVPreprocess, VAEDecode, easy showAnything, SaveVideo, LoraLoaderModelOnly, MathExpression|pysssss, Int, PreviewImage, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy showAnything, Int, SamplerCustom, easy promptLine, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, CLIPTextEncode, ImpactSwitch, LoadImage, Textbox, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/图生视频  音画同步  带多种电影级别运镜 LTXV 2.0_2025763431185387521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2025763431185387521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
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
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `CR Text Replace`
- `CheckpointLoaderSimple` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
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
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `LTXVPreprocess`
- `VAEDecode` ★核心
- `easy showAnything`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `MathExpression|pysssss`
- `Int`
- `PreviewImage`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `easy showAnything`
- `Int`
- `SamplerCustom` ★核心
- `easy promptLine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `ImpactSwitch`
- `LoadImage`
- `Textbox`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（56/66）

**有卡**：`LTXVScheduler`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`intToFloat _O`、`VAEDecode`、`LTXVAudioVAELoader`、`LTXVAudioVAEDecode`、`CreateVideo`、`Int`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CR Text Replace`、`CheckpointLoaderSimple`、`ManualSigmas`、`LTXVSeparateAVLatent`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`SaveVideo`、`Textbox`、`LTXVCropGuides`、`LTXVConditioning`、`easy cleanGpuUsed`、`RH_Captioner`、`LTXVPreprocess`、`MathExpression|pysssss`、`SamplerCustom`、`easy promptLine`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
