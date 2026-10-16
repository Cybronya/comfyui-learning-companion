---
key: 视频生成/图生视频/LTX2.5_i2v_2092791658453753857.json
name: LTX2.5_i2v_2092791658453753857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5_i2v_2092791658453753857.json
hash: 3fff20cd42d3fba1
coverage: 0.785714
learned_at: 2026-10-16 22:59:05
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, ResolutionSelector, MarkdownNote, TextGenerateLTX2Prompt, PrimitiveBoolean, CLIPTextEncode, PrimitiveStringMultiline, ComfySwitchNode, UNETLoader, PreviewAny, PrimitiveInt, PrimitiveBoolean, LTXVConditioning, VAELoader, VAELoader, PrimitiveInt, CLIPTextEncode, CLIPLoader, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LoadImage, CLIPLoader, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5_i2v_2092791658453753857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5_i2v_2092791658453753857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
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
- `SaveVideo`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（44/56）

**有卡**：`ResolutionSelector`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`CLIPTextEncode`、`UNETLoader`、`LTXVConditioning`、`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
