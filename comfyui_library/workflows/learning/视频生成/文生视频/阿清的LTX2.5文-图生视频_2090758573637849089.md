---
key: 视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json
name: 阿清的LTX2.5文-图生视频_2090758573637849089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json
hash: c14e29e7a528dafc
coverage: 0.87234
learned_at: 2026-10-11 21:20:00
nodes: [LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPLoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, ManualSigmas, LTXVImgToVideoInplace, PrimitiveInt, PrimitiveInt, PrimitiveInt, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, MuyeTextEditOutput, MarkdownNote, VAELoader, VAELoader, CLIPTextEncode, CLIPTextEncode, SaveVideo, CreateVideo, LoadImage, PrimitiveBoolean, UNETLoader, PrimitiveStringMultiline, LTXVConcatAVLatent, ResolutionSelector, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/阿清的LTX2.5文-图生视频_2090758573637849089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（47 个）：
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `MuyeTextEditOutput`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `CreateVideo`
- `LoadImage`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`CLIPLoader`、`LatentUpscaleModelLoader`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`MuyeTextEditOutput`、`VAELoader`、`CLIPTextEncode`、`SaveVideo`、`CreateVideo`、`LoadImage`、`PrimitiveBoolean`、`UNETLoader`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
