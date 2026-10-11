---
key: 视频生成/文生视频/LTX2.5 视频生成 I 提示词强化_2087468290628214785.json
name: LTX2.5 视频生成 I 提示词强化_2087468290628214785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 视频生成 I 提示词强化_2087468290628214785.json
hash: 640c4dc8c6f4a6b0
coverage: 0.836735
learned_at: 2026-10-11 20:53:38
nodes: [UNETLoader, LTXVConditioning, VAELoader, VAELoader, CLIPTextEncode, KSamplerSelect, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, LTXVSeparateAVLatent, PrimitiveInt, CLIPTextEncode, LTXVPreprocess, PreviewAny, LTXVAudioVAEDecode, RandomNoise, ManualSigmas, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, ComfySwitchNode, PrimitiveBoolean, MarkdownNote, TextGenerateLTX2Prompt, VAEDecodeTiled, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, PrimitiveBoolean, CLIPLoader, CLIPLoader, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5 视频生成 I 提示词强化_2087468290628214785.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 视频生成 I 提示词强化_2087468290628214785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（49 个）：
- `UNETLoader` ★核心
- `LTXVConditioning`
- `VAELoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `PreviewAny`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `MarkdownNote`
- `TextGenerateLTX2Prompt`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（41/49）

**有卡**：`UNETLoader`、`LTXVConditioning`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`RandomNoise`、`ManualSigmas`、`LTXVPreprocess`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LoadImage`、`CLIPLoader`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
