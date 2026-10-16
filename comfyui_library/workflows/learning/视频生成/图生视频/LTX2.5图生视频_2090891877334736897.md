---
key: 视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json
name: LTX2.5图生视频_2090891877334736897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json
hash: 0825441ac2c80635
coverage: 0.796296
learned_at: 2026-10-16 22:30:33
nodes: [MarkdownNote, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, MarkdownNote, RandomNoise, PrimitiveInt, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, MarkdownNote, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, PrimitiveStringMultiline, SaveVideo, ResolutionSelector, LoadImage, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, PreviewAny, PrimitiveBoolean, CLIPLoader, TextGenerateLTX2Prompt, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频_2090891877334736897.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（54 个）：
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
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
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `RandomNoise`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `SaveVideo`
- `ResolutionSelector`
- `LoadImage`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `PreviewAny`
- `PrimitiveBoolean`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（43/54）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SaveVideo`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
