---
key: 平台全量/ltx2.5-放大_2088501406817935361.json
name: ltx2.5-放大_2088501406817935361
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ltx2.5-放大_2088501406817935361.json
hash: c580586a133bbcfc
coverage: 0.866667
learned_at: 2026-11-14 01:14:40
nodes: [UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, CLIPTextEncode, VAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, PreviewImage, Fast Groups Bypasser (rgthree), PrimitiveBoolean, VHS_LoadVideo, PrimitiveFloat, MarkdownNote, LoadImage, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, SaveVideo, CreateVideo, LTXVLatentUpsampler, LTXVAudioVAEEncode, LTXVConditioning, VHS_LoadVideo, VHS_VideoCombine, CLIPTextEncode, KSampler, VAEDecodeTiled]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 933910523266679, "steps": 2}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/ltx2.5-放大_2088501406817935361.json

> 来源文件 `comfyui_library/workflows/平台全量/ltx2.5-放大_2088501406817935361.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `MarkdownNote`
- `LoadImage`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `SaveVideo`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVConditioning`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `933910523266679`
- `steps` = `2`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`VAEEncode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`VHS_LoadVideo`、`LoadImage`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`SaveVideo`、`CreateVideo`、`LTXVLatentUpsampler`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`VHS_VideoCombine`、`KSampler`、`VAEDecodeTiled`

**用到的条目**：KSampler、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、LTXVLatentUpsampler、LatentUpscaleModelLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
