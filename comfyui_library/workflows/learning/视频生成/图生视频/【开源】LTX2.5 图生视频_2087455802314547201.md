---
key: 视频生成/图生视频/【开源】LTX2.5 图生视频_2087455802314547201.json
name: 【开源】LTX2.5 图生视频_2087455802314547201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【开源】LTX2.5 图生视频_2087455802314547201.json
hash: 2295704eb4077640
coverage: 0.862745
learned_at: 2026-10-16 21:27:59
nodes: [LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, LTXVDualCFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVConditioning, RandomNoise, LTXVAudioVAEDecode, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, KSamplerSelect, UNETLoader, LatentUpscaleModelLoader, ManualSigmas, CreateVideo, SaveVideo, MarkdownNote, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, VAELoader, CLIPLoader, PrimitiveInt, ComfyMathExpression, VAEDecodeTiled, ResizeImageMaskNode, CLIPLoader, ComfySwitchNode, easy cleanGpuUsed, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVSeparateAVLatent, VAELoader, easy showAnything, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, PrimitiveBoolean, ResolutionSelector, TextGenerateLTX2Prompt, LTXVConcatAVLatent, PrimitiveInt, Text, LTXVPreprocess, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/【开源】LTX2.5 图生视频_2087455802314547201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【开源】LTX2.5 图生视频_2087455802314547201.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `VAEDecodeTiled` ★核心
- `ResizeImageMaskNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `easy cleanGpuUsed`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `VAELoader`
- `easy showAnything`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `Text`
- `LTXVPreprocess`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（44/51）

**有卡**：`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVConditioning`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`VAELoader`、`CLIPLoader`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`easy cleanGpuUsed`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`Text`、`LTXVPreprocess`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
