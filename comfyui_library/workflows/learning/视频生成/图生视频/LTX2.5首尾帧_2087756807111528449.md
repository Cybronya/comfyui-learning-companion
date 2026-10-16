---
key: 视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json
name: LTX2.5首尾帧_2087756807111528449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json
hash: cd1f6a48323b500e
coverage: 0.911765
learned_at: 2026-10-16 21:27:37
nodes: [ManualSigmas, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, ComfyMathExpression, UNETLoader, VAELoader, VAELoader, CLIPLoader, LTXVAudioVAEDecode, CLIPTextEncode, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, VAEDecodeTiled, LoadImage, LTXVAddGuide, LoadImage, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, LTXVPreprocess, EmptyLTXVLatentVideo, GetImageSize, LTXVPreprocess, PrimitiveStringMultiline, LTXVAddGuide, VHS_VideoCombine, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧_2087756807111528449.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（34 个）：
- `ManualSigmas`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `LTXVAddGuide`
- `LoadImage`
- `ComfyMathExpression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `LTXVAddGuide`
- `VHS_VideoCombine`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`ManualSigmas`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`ComfyMathExpression`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVCropGuides`、`VAEDecodeTiled`、`LoadImage`、`LTXVAddGuide`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`GetImageSize`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider
