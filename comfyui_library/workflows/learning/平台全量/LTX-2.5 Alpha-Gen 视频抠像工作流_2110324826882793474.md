---
key: 平台全量/LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474.json
name: LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474.json
hash: 2eabe552ae7e22b0
coverage: 0.829268
learned_at: 2026-11-14 00:37:12
nodes: [LTXAddVideoICLoRAGuide, ManualSigmas, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, EmptyLTXVLatentVideo, MarkdownNote, KSamplerSelect, XB_CanvasLabel, PrimitiveInt, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, PrimitiveStringMultiline, RandomNoise, CreateVideo, LoadVideo, LTXICLoRALoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, VAELoader, LTXVEmptyLatentAudio, SaveVideo, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5 Alpha-Gen 视频抠像工作流_2110324826882793474.json`

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
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `XB_CanvasLabel`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `CreateVideo`
- `LoadVideo`
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `SaveVideo`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`XB_CanvasLabel`、`RandomNoise`、`CreateVideo`、`LoadVideo`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LTXVEmptyLatentAudio`、`SaveVideo`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
