---
key: 平台全量/LTX2.5-Refine-Details 视频细节精修工作流_2110321013971054594.json
name: LTX2.5-Refine-Details 视频细节精修工作流_2110321013971054594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.5-Refine-Details 视频细节精修工作流_2110321013971054594.json
hash: 4b64b6693064df2d
coverage: 0.85
learned_at: 2026-11-14 00:39:09
nodes: [RandomNoise, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, MarkdownNote, ManualSigmas, KSamplerSelect, ImageFromBatch, VAELoader, VAELoader, CLIPLoader, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ImageScale, LTXVConditioning, PrimitiveInt, PrimitiveFloat, UNETLoader, CreateVideo, PrimitiveInt, LoadVideo, XB_CanvasLabel, LTXICLoRALoaderModelOnly, PrimitiveStringMultiline, PrimitiveStringMultiline, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.5-Refine-Details 视频细节精修工作流_2110321013971054594.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.5-Refine-Details 视频细节精修工作流_2110321013971054594.json`

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
- `UNETLoader` ★核心
- `CreateVideo`
- `PrimitiveInt`
- `LoadVideo`
- `XB_CanvasLabel`
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`ComfyMathExpression`、`ManualSigmas`、`KSamplerSelect`、`ImageFromBatch`、`VAELoader`、`CLIPLoader`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ImageScale`、`LTXVConditioning`、`UNETLoader`、`CreateVideo`、`LoadVideo`、`XB_CanvasLabel`、`LTXICLoRALoaderModelOnly`、`SaveVideo`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
