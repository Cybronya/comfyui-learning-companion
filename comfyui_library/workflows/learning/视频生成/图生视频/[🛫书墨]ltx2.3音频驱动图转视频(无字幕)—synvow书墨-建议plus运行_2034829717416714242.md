---
key: 视频生成/图生视频/[🛫书墨]ltx2.3音频驱动图转视频(无字幕)—synvow书墨-建议plus运行_2034829717416714242.json
name: [🛫书墨]ltx2.3音频驱动图转视频(无字幕)—synvow书墨-建议plus运行_2034829717416714242.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034829717416714242.json
hash: 4a1f3aae22810ad5
coverage: 0.862745
learned_at: 2026-10-15 22:35:45
nodes: [CFGGuider, KSamplerSelect, EmptyLTXVLatentVideo, LTXVConditioning, CLIPTextEncode, LTXVConcatAVLatent, CLIPTextEncode, RandomNoise, LTXVAudioVAEEncode, LTXVSeparateAVLatent, SetLatentNoiseMask, SolidMask, PathchSageAttentionKJ, LTXVCropGuides, LTXVSeparateAVLatent, LTXVImgToVideoInplace, LTX2SamplingPreviewOverride, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, MathExpression|pysssss, VHS_VideoCombine, LoadImage, SamplerCustomAdvanced, LTXVConcatAVLatent, VAEDecodeTiled, KSampler, AudioTrim, PreviewAudio, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, RHHiddenNodes, LoraLoaderModelOnly, LoadAudio, PrimitiveStringMultiline, MarkdownNote, RunningHub Deepcleaner, BasicScheduler, RunningHub Deepcleaner, Note, ttN text7BOX_concat, LoadImage, AILab_QwenVL, ImpactInt, PrimitiveStringMultiline, PrimitiveStringMultiline, ShowText|pysssss]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 744256708110229, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/[🛫书墨]ltx2.3音频驱动图转视频(无字幕)—synvow书墨-建议plus运行_2034829717416714242.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034829717416714242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVAudioVAEEncode` ★核心
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `SolidMask`
- `PathchSageAttentionKJ`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `LTX2SamplingPreviewOverride`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `AudioTrim`
- `PreviewAudio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `RunningHub Deepcleaner`
- `BasicScheduler`
- `RunningHub Deepcleaner`
- `Note`
- `ttN text7BOX_concat`
- `LoadImage`
- `AILab_QwenVL`
- `ImpactInt`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`

## 关键参数

- `seed` = `744256708110229`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **86%**（44/51）

**有卡**：`CFGGuider`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXVAudioVAEEncode`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`SolidMask`、`PathchSageAttentionKJ`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`MathExpression|pysssss`、`VHS_VideoCombine`、`LoadImage`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`KSampler`、`AudioTrim`、`PreviewAudio`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`LoadAudio`、`RunningHub Deepcleaner`、`BasicScheduler`、`ttN text7BOX_concat`、`AILab_QwenVL`、`ImpactInt`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
