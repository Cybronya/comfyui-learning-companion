---
key: 视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json
name: LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json
hash: 25c1e8ded6c4846f
coverage: 0.864865
learned_at: 2026-10-16 21:27:37
nodes: [VAEDecodeTiled, LTXVAudioVAEDecode, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, UNETLoader, VAELoader, PrimitiveInt, MarkdownNote, CreateVideo, SaveVideo, CLIPLoader, VAELoader, ComfyMathExpression, ComfyMathExpression, LoadImage, LTXVAddGuide, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LTXVPreprocess, PrimitiveInt, EmptyLTXVLatentVideo, MarkdownNote, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频-高质量直出1K_2087559262871572481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveInt`
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadImage`
- `LTXVAddGuide`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`LTXVAddGuide`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`UNETLoader`、`VAELoader`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`ComfyMathExpression`、`LoadImage`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral
