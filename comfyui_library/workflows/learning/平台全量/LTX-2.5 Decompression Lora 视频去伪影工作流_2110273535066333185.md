---
key: 平台全量/LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185.json
name: LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185.json
hash: 37bc06278d259446
coverage: 0.85
learned_at: 2026-11-14 00:37:13
nodes: [LTXAddVideoICLoRAGuide, ManualSigmas, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, EmptyLTXVLatentVideo, MarkdownNote, XB_CanvasLabel, UNETLoader, CLIPLoader, VAELoader, VAELoader, KSamplerSelect, CreateVideo, LTXVEmptyLatentAudio, RandomNoise, LoadVideo, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, PrimitiveFloat, PrimitiveStringMultiline, LTXICLoRALoaderModelOnly, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5 Decompression Lora 视频去伪影工作流_2110273535066333185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
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
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `LoadVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LTXICLoRALoaderModelOnly` ★核心
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`EmptyLTXVLatentVideo`、`XB_CanvasLabel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`CreateVideo`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LoadVideo`、`LTXICLoRALoaderModelOnly`、`SaveVideo`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
