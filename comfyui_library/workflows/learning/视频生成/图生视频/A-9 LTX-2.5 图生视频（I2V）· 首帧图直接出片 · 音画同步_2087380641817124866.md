---
key: 视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json
name: A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json
hash: e5a7eebb47c26c31
coverage: 0.836364
learned_at: 2026-10-16 21:27:26
nodes: [SaveVideo, ResolutionSelector, CLIPLoader, TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPTextEncode, PrimitiveStringMultiline, ComfySwitchNode, UNETLoader, PreviewAny, PrimitiveInt, PrimitiveBoolean, LTXVConditioning, VAELoader, VAELoader, PrimitiveInt, CLIPTextEncode, CLIPLoader, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ImageFromBatch, SaveImage, SaveAudio, MarkdownNote, MarkdownNote, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/A-9 LTX-2.5 图生视频（I2V）· 首帧图直接出片 · 音画同步_2087380641817124866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `SaveVideo`
- `ResolutionSelector`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `PreviewAny`
- `PrimitiveInt`
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
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
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
- `ImageFromBatch`
- `SaveImage`
- `SaveAudio`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（46/55）

**有卡**：`SaveVideo`、`ResolutionSelector`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`CLIPTextEncode`、`UNETLoader`、`LTXVConditioning`、`VAELoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`ImageFromBatch`、`SaveImage`、`SaveAudio`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
