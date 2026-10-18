---
key: 视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json
name: LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json
hash: a9f4044631fe630f
coverage: 0.825
learned_at: 2026-10-18 00:23:06
nodes: [ManualSigmas, GetImageSize, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, CFGGuider, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, MarkdownNote, KSamplerSelect, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoadImage, SaveVideo, CreateVideo, PrimitiveInt, PrimitiveFloat, PrimitiveFloat, PrimitiveInt, ComfyMathExpression, RandomNoise, LTXVEmptyLatentAudio, LTXVPreprocess, PrimitiveStringMultiline, PrimitiveStringMultiline, LoraLoaderModelOnly, XB_CanvasLabel]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5 Cinemagraph 局部动态 图像到视频 ComfyUI 工作流_2110222043215130625.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ManualSigmas`
- `GetImageSize`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVConditioning`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `SaveVideo`
- `CreateVideo`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveInt`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `XB_CanvasLabel`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`ManualSigmas`、`GetImageSize`、`ResizeImageMaskNode`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveVideo`、`CreateVideo`、`RandomNoise`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`XB_CanvasLabel`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
