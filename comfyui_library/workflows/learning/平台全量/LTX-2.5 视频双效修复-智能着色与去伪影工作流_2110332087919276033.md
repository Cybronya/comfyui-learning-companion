---
key: 平台全量/LTX-2.5 视频双效修复-智能着色与去伪影工作流_2110332087919276033.json
name: LTX-2.5 视频双效修复-智能着色与去伪影工作流_2110332087919276033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5 视频双效修复-智能着色与去伪影工作流_2110332087919276033.json
hash: 91ffb01fb02e1a89
coverage: 0.853659
learned_at: 2026-11-14 00:37:15
nodes: [LTXAddVideoICLoRAGuide, ManualSigmas, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, VAELoader, PrimitiveFloat, PrimitiveInt, RandomNoise, PrimitiveStringMultiline, PrimitiveInt, KSamplerSelect, CreateVideo, LoadVideo, SaveVideo, PrimitiveStringMultiline, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, XB_CanvasLabel]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5 视频双效修复-智能着色与去伪影工作流_2110332087919276033.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5 视频双效修复-智能着色与去伪影工作流_2110332087919276033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
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
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `CreateVideo`
- `LoadVideo`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `XB_CanvasLabel`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`CreateVideo`、`LoadVideo`、`SaveVideo`、`LTXICLoRALoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`XB_CanvasLabel`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
