---
key: 平台全量/ltx2.5-放大_2087764640519516162.json
name: ltx2.5-放大_2087764640519516162
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ltx2.5-放大_2087764640519516162.json
hash: 04563250e6555c68
coverage: 0.862069
learned_at: 2026-11-14 01:14:39
nodes: [LTXVAudioVAEEncode, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, ResizeImageMaskNode, LTXVPreprocess, VAEEncode, LTXVLatentUpsampler, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVImgToVideoInplace, LoadImage, PreviewImage, Fast Groups Bypasser (rgthree), VHS_LoadVideo, PrimitiveBoolean, VHS_LoadVideo, PrimitiveFloat, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 489876348635579, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/ltx2.5-放大_2087764640519516162.json

> 来源文件 `comfyui_library/workflows/平台全量/ltx2.5-放大_2087764640519516162.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `LTXVAudioVAEEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `VAEEncode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `VHS_LoadVideo`
- `PrimitiveBoolean`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `489876348635579`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`LTXVAudioVAEEncode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVConditioning`、`ResizeImageMaskNode`、`LTXVPreprocess`、`VAEEncode`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`KSampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LTXVImgToVideoInplace`、`LoadImage`、`VHS_LoadVideo`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、LTXVLatentUpsampler、LatentUpscaleModelLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
