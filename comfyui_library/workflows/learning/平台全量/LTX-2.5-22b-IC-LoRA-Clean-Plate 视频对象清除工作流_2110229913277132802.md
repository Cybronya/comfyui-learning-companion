---
key: 平台全量/LTX-2.5-22b-IC-LoRA-Clean-Plate 视频对象清除工作流_2110229913277132802.json
name: LTX-2.5-22b-IC-LoRA-Clean-Plate 视频对象清除工作流_2110229913277132802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX-2.5-22b-IC-LoRA-Clean-Plate 视频对象清除工作流_2110229913277132802.json
hash: 4b15f93c10caece1
coverage: 0.85
learned_at: 2026-11-14 00:37:16
nodes: [ManualSigmas, LTXVConcatAVLatent, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, Video Slice, CLIPTextEncode, CLIPTextEncode, GetVideoComponents, GetImageSize, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageFromBatch, ComfyMathExpression, ComfyMathExpression, ImageScale, MarkdownNote, XB_CanvasLabel, UNETLoader, CLIPLoader, VAELoader, VAELoader, LTXICLoRALoaderModelOnly, PrimitiveInt, PrimitiveFloat, PrimitiveInt, RandomNoise, LTXAddVideoICLoRAGuide, LoadVideo, SaveVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, KSamplerSelect, CreateVideo, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX-2.5-22b-IC-LoRA-Clean-Plate 视频对象清除工作流_2110229913277132802.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX-2.5-22b-IC-LoRA-Clean-Plate 视频对象清除工作流_2110229913277132802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
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
- `XB_CanvasLabel`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `LTXAddVideoICLoRAGuide`
- `LoadVideo`
- `SaveVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `KSamplerSelect` ★核心
- `CreateVideo`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`Video Slice`、`CLIPTextEncode`、`GetVideoComponents`、`GetImageSize`、`LTXVConditioning`、`ComfyMathExpression`、`ImageFromBatch`、`ImageScale`、`XB_CanvasLabel`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LTXICLoRALoaderModelOnly`、`RandomNoise`、`LTXAddVideoICLoRAGuide`、`LoadVideo`、`SaveVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`KSamplerSelect`、`CreateVideo`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyLTXVLatentVideo
