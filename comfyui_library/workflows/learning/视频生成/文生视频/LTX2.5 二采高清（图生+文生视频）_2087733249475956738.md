---
key: 视频生成/文生视频/LTX2.5 二采高清（图生+文生视频）_2087733249475956738.json
name: LTX2.5 二采高清（图生+文生视频）_2087733249475956738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 二采高清（图生+文生视频）_2087733249475956738.json
hash: 7af974e18b1c4fbf
coverage: 0.8
learned_at: 2026-10-11 20:53:37
nodes: [ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, PrimitiveInt, MarkdownNote, LTXVConcatAVLatent, LTXVAudioVAEDecode, SamplerCustomAdvanced, RandomNoise, PreviewAny, CLIPLoader, TextGenerateLTX2Prompt, ComfySwitchNode, MarkdownNote, MarkdownNote, VAELoader, VAELoader, LTXVPreprocess, UNETLoader, CLIPLoader, PrimitiveBoolean, PrimitiveInt, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVDualCFGGuider, LTXVConditioning, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, SaveVideo, CreateVideo, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, MarkdownNote, CLIPTextEncode, PrimitiveStringMultiline, ResolutionSelector, PrimitiveInt, LoadImage, ResizeImageMaskNode, PrimitiveBoolean, VAEDecodeTiled, KSamplerSelect, RandomNoise, ManualSigmas, KSamplerSelect, PurgeVRAM_UTK, LTXVLatentUpsampler, ManualSigmas, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5 二采高清（图生+文生视频）_2087733249475956738.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 二采高清（图生+文生视频）_2087733249475956738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（55 个）：
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `PreviewAny`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `LTXVPreprocess`
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `CreateVideo`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveInt`
- `LoadImage`
- `ResizeImageMaskNode`
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `PurgeVRAM_UTK`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（44/55）

**有卡**：`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`VAELoader`、`LTXVPreprocess`、`UNETLoader`、`PrimitiveBoolean`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`LTXVConditioning`、`SaveVideo`、`CreateVideo`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ResolutionSelector`、`LoadImage`、`ResizeImageMaskNode`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`PurgeVRAM_UTK`、`LTXVLatentUpsampler`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
