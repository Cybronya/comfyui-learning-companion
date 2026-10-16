---
key: 视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json
name: LTX 2.5 图生视频_2093915637625212929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json
hash: 9efed98697d39c44
coverage: 0.796296
learned_at: 2026-10-16 23:42:02
nodes: [UNETLoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, ResizeImageMaskNode, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVAudioVAEDecode, CreateVideo, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ResolutionSelector, CLIPTextEncode, CLIPTextEncode, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PreviewAny, PrimitiveBoolean, PrimitiveBoolean, TextGenerateLTX2Prompt, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, CLIPLoader, PrimitiveStringMultiline, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, VAEDecodeTiled, SaveVideo, LTXVSeparateAVLatent, LTXVConditioning, ComfySwitchNode, RandomNoise, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX 2.5 图生视频_2093915637625212929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（54 个）：
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `ComfySwitchNode`
- `RandomNoise`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（43/54）

**有卡**：`UNETLoader`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`ResizeImageMaskNode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`CreateVideo`、`ResolutionSelector`、`CLIPTextEncode`、`ComfyMathExpression`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`VAEDecodeTiled`、`SaveVideo`、`LTXVConditioning`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
