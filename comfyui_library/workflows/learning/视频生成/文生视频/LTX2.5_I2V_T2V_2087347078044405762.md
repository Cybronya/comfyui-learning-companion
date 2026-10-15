---
key: 视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json
name: LTX2.5_I2V_T2V_2087347078044405762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json
hash: 2238f07c7a431d70
coverage: 0.8
learned_at: 2026-10-15 22:45:16
nodes: [CLIPTextEncode, UNETLoader, LTXVConditioning, VAELoader, VAELoader, PrimitiveInt, CLIPTextEncode, CLIPLoader, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LatentUpscaleModelLoader, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, LTXVPreprocess, SaveVideo, PrimitiveBoolean, LoadImage, PrimitiveInt, PrimitiveStringMultiline, ResolutionSelector, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5_I2V_T2V_2087347078044405762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
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
- `LTXVPreprocess`
- `SaveVideo`
- `PrimitiveBoolean`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（40/50）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`LTXVConditioning`、`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVPreprocess`、`SaveVideo`、`PrimitiveBoolean`、`LoadImage`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
