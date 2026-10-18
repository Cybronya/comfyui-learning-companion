---
key: 视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json
name: LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json
hash: 40548462918ac0e3
coverage: 0.851852
learned_at: 2026-10-18 00:23:07
nodes: [ManualSigmas, KSamplerSelect, ManualSigmas, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, ComfyMathExpression, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, LTXVDualCFGGuider, LTXVDualCFGGuider, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, MarkdownNote, KSamplerSelect, UNETLoader, CLIPLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, ResizeImageMaskNode, PrimitiveFloat, PrimitiveFloat, LTXVEmptyLatentAudio, ComfyMathExpression, RandomNoise, RandomNoise, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveInt, LoadImage, CreateVideo, XB_CanvasLabel, GetImageSize, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5 Slow Motion Control 慢动作视频生成工作流_2110054667488153602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `ComfyMathExpression`
- `LTXVConditioning`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVDualCFGGuider`
- `LTXVDualCFGGuider`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
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
- `LatentUpscaleModelLoader`
- `ResizeImageMaskNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `LoadImage`
- `CreateVideo`
- `XB_CanvasLabel`
- `GetImageSize`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXVConditioning`、`LTXVDualCFGGuider`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LoraLoaderModelOnly`、`LoadImage`、`CreateVideo`、`XB_CanvasLabel`、`GetImageSize`、`SaveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
