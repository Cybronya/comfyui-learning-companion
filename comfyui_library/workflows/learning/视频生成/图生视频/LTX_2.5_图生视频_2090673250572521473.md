---
key: 视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json
name: LTX_2.5_图生视频_2090673250572521473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json
hash: 86202ef8985d67fb
coverage: 0.849057
learned_at: 2026-10-16 22:30:33
nodes: [TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPTextEncode, ComfySwitchNode, UNETLoader, PrimitiveBoolean, LTXVConditioning, VAELoader, VAELoader, PrimitiveInt, CLIPTextEncode, CLIPLoader, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, PreviewAny, MarkdownNote, LTXVEmptyLatentAudio, ResolutionSelector, LoadImage, PrimitiveInt, CLIPLoader, PrimitiveStringMultiline, SaveVideo, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX_2.5_图生视频_2090673250572521473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `LTXVConditioning`
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `PrimitiveInt`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `PreviewAny`
- `MarkdownNote`
- `LTXVEmptyLatentAudio` ★核心
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveInt`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（45/53）

**有卡**：`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`CLIPTextEncode`、`UNETLoader`、`LTXVConditioning`、`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVEmptyLatentAudio`、`ResolutionSelector`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
