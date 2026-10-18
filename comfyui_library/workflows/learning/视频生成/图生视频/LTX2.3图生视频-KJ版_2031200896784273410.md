---
key: 视频生成/图生视频/LTX2.3图生视频-KJ版_2031200896784273410.json
name: LTX2.3图生视频-KJ版_2031200896784273410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频-KJ版_2031200896784273410.json
hash: c21b16021d9524dd
coverage: 0.830189
learned_at: 2026-10-15 22:35:29
nodes: [TextListSplit, DualCLIPLoader, EmptyImage, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplace, UNETLoader, LTXVPreprocess, LTXVConcatAVLatent, LoraLoaderModelOnly, LTXVScheduler, RandomNoise, CFGGuider, LTXVConditioning, KSamplerSelect, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSampler, VAELoaderKJ, VAELoaderKJ, LTXVImgToVideoInplace, VAEDecode, Reroute, LayerUtility: PurgeVRAM V2, LayerUtility: ImageScaleByAspectRatio V2, ImpactSwitch, LTXVConcatAVLatent, TextGenerateLTX2Prompt, RH_Translator, ShowText|pysssss, ShowText|pysssss, EmptyLTXVLatentVideo, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, MathExpression|pysssss, ShowText|pysssss, ShowText|pysssss, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VHS_VideoCombine, LatentUpscaleModelLoader, LoadImage, PrimitiveInt, PrimitiveInt, easy positive, Qwen3_VQA, LTXVSeparateAVLatent, Reroute, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.3500000000000001, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 581264938593513, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频-KJ版_2031200896784273410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031200896784273410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `TextListSplit`
- `DualCLIPLoader`
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `UNETLoader` ★核心
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `CFGGuider`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSampler` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVImgToVideoInplace`
- `VAEDecode` ★核心
- `Reroute`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactSwitch`
- `LTXVConcatAVLatent`
- `TextGenerateLTX2Prompt`
- `RH_Translator`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `EmptyLTXVLatentVideo`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `MathExpression|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy positive`
- `Qwen3_VQA`
- `LTXVSeparateAVLatent`
- `Reroute`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `581264938593513`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3500000000000001`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`TextListSplit`、`DualCLIPLoader`、`EmptyImage`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`UNETLoader`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVScheduler`、`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`KSampler`、`VAELoaderKJ`、`VAEDecode`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextGenerateLTX2Prompt`、`RH_Translator`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`MathExpression|pysssss`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`LoadImage`、`easy positive`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
