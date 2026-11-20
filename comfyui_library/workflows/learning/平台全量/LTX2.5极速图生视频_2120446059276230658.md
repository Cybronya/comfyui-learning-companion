---
key: 平台全量/LTX2.5极速图生视频_2120446059276230658.json
name: LTX2.5极速图生视频_2120446059276230658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.5极速图生视频_2120446059276230658.json
hash: 2c367f3a0638c5dd
coverage: 0.843137
learned_at: 2026-11-14 00:39:10
nodes: [PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ComfySwitchNode, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, PrimitiveInt, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, TextGenerateLTX2Prompt, ComfyMathExpression, ComfyMathExpression, MarkdownNote, PreviewAny, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, PrimitiveBoolean, CLIPLoader, SaveVideo, ResolutionSelector, LoadImage, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.5极速图生视频_2120446059276230658.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.5极速图生视频_2120446059276230658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ComfySwitchNode`
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `PreviewAny`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `CLIPLoader`
- `SaveVideo`
- `ResolutionSelector`
- `LoadImage`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`TextGenerateLTX2Prompt`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`SaveVideo`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、LTXVDualCFGGuider
