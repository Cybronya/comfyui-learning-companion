---
key: 视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json
name: LTX2.5-图生视频_2087412034005725185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json
hash: 27d69c003e85b81c
coverage: 0.792453
learned_at: 2026-10-16 21:27:36
nodes: [MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVConcatAVLatent, MarkdownNote, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, MarkdownNote, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, SaveVideo, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, ManualSigmas, ComfyMathExpression, ComfyMathExpression, ResolutionSelector, PrimitiveInt, RandomNoise, RandomNoise, LTXVConditioning, CLIPTextEncode, MarkdownNote, ResizeImageMaskNode, LTXVPreprocess, ComfyMathExpression, LoadImage, PrimitiveStringMultiline, CLIPLoader, easy showAnything, TextGenerateLTX2Prompt, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5-图生视频_2087412034005725185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveInt`
- `RandomNoise`
- `RandomNoise`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（42/53）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`ComfyMathExpression`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SaveVideo`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`CLIPLoader`、`ResolutionSelector`、`RandomNoise`、`LTXVConditioning`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LoadImage`、`TextGenerateLTX2Prompt`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
