---
key: 平台全量/LTX-2.5 Water Lora 视频到视频 水特效添加工作流_2110249425766535170.json
name: LTX-2.5 Water Lora 视频到视频 水特效添加工作流_2110249425766535170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5 Water Lora 视频到视频 水特效添加工作流_2110249425766535170.json
hash: 7390e7c3a1ab0c99
coverage: 0.85
learned_at: 2026-11-14 00:37:15
nodes: [LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, EmptyLTXVLatentVideo, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoadVideo, SaveVideo, RandomNoise, PrimitiveInt, PrimitiveStringMultiline, Video Slice, LTXVEmptyLatentAudio, KSamplerSelect, ManualSigmas, PrimitiveFloat, PrimitiveInt, XB_CanvasLabel, LTXICLoRALoaderModelOnly, PrimitiveStringMultiline, LTXVCropGuides]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5 Water Lora 视频到视频 水特效添加工作流_2110249425766535170.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5 Water Lora 视频到视频 水特效添加工作流_2110249425766535170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
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
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadVideo`
- `SaveVideo`
- `RandomNoise`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `Video Slice`
- `LTXVEmptyLatentAudio` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `XB_CanvasLabel`
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LTXVCropGuides`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`CreateVideo`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`EmptyLTXVLatentVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadVideo`、`SaveVideo`、`RandomNoise`、`Video Slice`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`ManualSigmas`、`XB_CanvasLabel`、`LTXICLoRALoaderModelOnly`、`LTXVCropGuides`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
