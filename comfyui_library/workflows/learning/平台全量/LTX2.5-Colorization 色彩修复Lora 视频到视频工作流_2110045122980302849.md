---
key: 平台全量/LTX2.5-Colorization 色彩修复Lora 视频到视频工作流_2110045122980302849.json
name: LTX2.5-Colorization 色彩修复Lora 视频到视频工作流_2110045122980302849
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.5-Colorization 色彩修复Lora 视频到视频工作流_2110045122980302849.json
hash: c3a52574d2909b81
coverage: 0.85
learned_at: 2026-11-14 00:39:08
nodes: [RandomNoise, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, MarkdownNote, ManualSigmas, KSamplerSelect, ImageFromBatch, PrimitiveStringMultiline, VAELoader, VAELoader, CLIPLoader, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ImageScale, LTXVConditioning, PrimitiveInt, PrimitiveFloat, PrimitiveInt, UNETLoader, LTXICLoRALoaderModelOnly, LoadVideo, SaveVideo, CreateVideo, PrimitiveStringMultiline, XB_CanvasLabel]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.5-Colorization 色彩修复Lora 视频到视频工作流_2110045122980302849.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.5-Colorization 色彩修复Lora 视频到视频工作流_2110045122980302849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `RandomNoise`
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
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ImageFromBatch`
- `PrimitiveStringMultiline`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScale`
- `LTXVConditioning`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoadVideo`
- `SaveVideo`
- `CreateVideo`
- `PrimitiveStringMultiline`
- `XB_CanvasLabel`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`ComfyMathExpression`、`ManualSigmas`、`KSamplerSelect`、`ImageFromBatch`、`VAELoader`、`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ImageScale`、`LTXVConditioning`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`LoadVideo`、`SaveVideo`、`CreateVideo`、`XB_CanvasLabel`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
