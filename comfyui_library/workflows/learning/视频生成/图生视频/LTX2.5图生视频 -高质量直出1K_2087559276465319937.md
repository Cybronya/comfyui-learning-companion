---
key: 视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json
name: LTX2.5图生视频 -高质量直出1K_2087559276465319937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json
hash: 98d2c8c5c10ff55b
coverage: 0.851064
learned_at: 2026-10-16 21:27:36
nodes: [PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, UNETLoader, VAELoader, VAELoader, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, SaveVideo, MarkdownNote, CreateVideo, CLIPTextEncode, CLIPTextEncode, LoadImage, LatentUpscaleModelLoader, CLIPLoader, MarkdownNote, PrimitiveStringMultiline, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（47 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `MarkdownNote`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `ResolutionSelector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（40/47）

**有卡**：`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`UNETLoader`、`VAELoader`、`PrimitiveBoolean`、`SaveVideo`、`CreateVideo`、`CLIPTextEncode`、`LoadImage`、`LatentUpscaleModelLoader`、`CLIPLoader`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
