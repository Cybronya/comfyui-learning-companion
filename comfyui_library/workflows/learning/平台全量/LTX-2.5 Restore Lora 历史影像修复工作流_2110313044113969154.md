---
key: 平台全量/LTX-2.5 Restore Lora 历史影像修复工作流_2110313044113969154.json
name: LTX-2.5 Restore Lora 历史影像修复工作流_2110313044113969154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5 Restore Lora 历史影像修复工作流_2110313044113969154.json
hash: 30d5cfb8014eaac7
coverage: 0.85
learned_at: 2026-11-14 00:37:14
nodes: [LTXAddVideoICLoRAGuide, ManualSigmas, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, EmptyLTXVLatentVideo, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoadVideo, SaveVideo, CreateVideo, KSamplerSelect, LTXICLoRALoaderModelOnly, LTXVEmptyLatentAudio, GetImageSize, GetVideoComponents, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveInt, PrimitiveFloat, PrimitiveInt, RandomNoise, XB_CanvasLabel]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5 Restore Lora 历史影像修复工作流_2110313044113969154.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5 Restore Lora 历史影像修复工作流_2110313044113969154.json`

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
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadVideo`
- `SaveVideo`
- `CreateVideo`
- `KSamplerSelect` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `GetVideoComponents`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `XB_CanvasLabel`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`EmptyLTXVLatentVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadVideo`、`SaveVideo`、`CreateVideo`、`KSamplerSelect`、`LTXICLoRALoaderModelOnly`、`LTXVEmptyLatentAudio`、`GetImageSize`、`GetVideoComponents`、`RandomNoise`、`XB_CanvasLabel`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
