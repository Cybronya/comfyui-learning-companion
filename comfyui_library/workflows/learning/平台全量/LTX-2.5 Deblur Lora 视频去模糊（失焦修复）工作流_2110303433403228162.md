---
key: 平台全量/LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162.json
name: LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162.json
hash: 4307cfe8c8775196
coverage: 0.85
learned_at: 2026-11-14 00:37:13
nodes: [CLIPLoader, LTXAddVideoICLoRAGuide, ManualSigmas, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, EmptyLTXVLatentVideo, MarkdownNote, XB_CanvasLabel, LTXICLoRALoaderModelOnly, UNETLoader, VAELoader, VAELoader, LoadVideo, SaveVideo, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, PrimitiveInt, RandomNoise, KSamplerSelect, LTXVEmptyLatentAudio, CreateVideo, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5 Deblur Lora 视频去模糊（失焦修复）工作流_2110303433403228162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `CLIPLoader`
- `LTXAddVideoICLoRAGuide`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `Video Slice`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetVideoComponents`
- `GetImageSize`
- `LTXVConditioning`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageFromBatch`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageScale`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `XB_CanvasLabel`
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LoadVideo`
- `SaveVideo`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `CreateVideo`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`EmptyLTXVLatentVideo`、`XB_CanvasLabel`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`VAELoader`、`LoadVideo`、`SaveVideo`、`RandomNoise`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`CreateVideo`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
