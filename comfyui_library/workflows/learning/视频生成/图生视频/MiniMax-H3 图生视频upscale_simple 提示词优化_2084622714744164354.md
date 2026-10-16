---
key: 视频生成/图生视频/MiniMax-H3 图生视频upscale_simple 提示词优化_2084622714744164354.json
name: MiniMax-H3 图生视频upscale_simple 提示词优化_2084622714744164354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3 图生视频upscale_simple 提示词优化_2084622714744164354.json
hash: a4ca4d6cd987c655
coverage: 0.756757
learned_at: 2026-10-16 20:35:35
nodes: [VAELoader, MarkdownNote, MarkdownNote, VAEDecode, ComfyMathExpression, MarkdownNote, Reroute, ConditioningZeroOut, VAEDecodeAudio, ImageScaleToTotalPixels, ResolutionSelector, PreviewImage, KSamplerAdvanced, MiniMaxH3SigmaShift, ImageUpscaleWithModel, UNETLoader, UNETLoader, PrimitiveFloat, UpscaleModelLoader, CreateVideo, CLIPLoader, VAELoader, ImageResizeKJv2, LoadImage, StringConcatenate, PrimitiveStringMultiline, Text Multiline, Fast Groups Bypasser (rgthree), AILab_QwenVL, Fast Bypasser (rgthree), GetImageSize, TTP_text_mix, AnySwitch, SaveVideo, PreviewAny, TTP_text_mix, MiniMaxH3ImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "sgm_uniform", "sampler_name": 1, "scheduler": "dpmpp_2m", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/MiniMax-H3 图生视频upscale_simple 提示词优化_2084622714744164354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3 图生视频upscale_simple 提示词优化_2084622714744164354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAELoader`
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `MarkdownNote`
- `Reroute`
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `ImageScaleToTotalPixels`
- `ResolutionSelector`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `MiniMaxH3SigmaShift`
- `ImageUpscaleWithModel`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `UpscaleModelLoader`
- `CreateVideo`
- `CLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `LoadImage`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `AILab_QwenVL`
- `Fast Bypasser (rgthree)`
- `GetImageSize`
- `TTP_text_mix`
- `AnySwitch`
- `SaveVideo`
- `PreviewAny`
- `TTP_text_mix`
- `MiniMaxH3ImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_2m`
- `denoise` = `sgm_uniform`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`VAELoader`、`VAEDecode`、`ComfyMathExpression`、`ConditioningZeroOut`、`VAEDecodeAudio`、`ImageScaleToTotalPixels`、`ResolutionSelector`、`KSamplerAdvanced`、`MiniMaxH3SigmaShift`、`ImageUpscaleWithModel`、`UNETLoader`、`UpscaleModelLoader`、`CreateVideo`、`CLIPLoader`、`ImageResizeKJv2`、`LoadImage`、`StringConcatenate`、`Text Multiline`、`AILab_QwenVL`、`Fast Bypasser (rgthree)`、`GetImageSize`、`TTP_text_mix`、`AnySwitch`、`SaveVideo`、`MiniMaxH3ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerAdvanced
