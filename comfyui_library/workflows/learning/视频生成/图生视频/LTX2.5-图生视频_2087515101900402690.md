---
key: 视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json
name: LTX2.5-图生视频_2087515101900402690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json
hash: 50b049e5102c11d5
coverage: 0.789474
learned_at: 2026-10-16 21:27:36
nodes: [MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, KSamplerSelect, ManualSigmas, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, MarkdownNote, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, CLIPLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVImgToVideoInplace, LTXVImgToVideoInplace, LTXVDualCFGGuider, UNETLoader, LTXVDualCFGGuider, ManualSigmas, ResolutionSelector, MarkdownNote, LoadImage, Note, Note, Note, VHS_VideoCombine, MarkdownNote, RH_LLMAPI_Pro_Node, TextGenerateLTX2Prompt, CR Text, PrimitiveInt, PrimitiveBoolean, CR Text, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（57 个）：
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `LTXVDualCFGGuider`
- `UNETLoader` ★核心
- `LTXVDualCFGGuider`
- `ManualSigmas`
- `ResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `TextGenerateLTX2Prompt`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `CR Text`
- `easy showAnything`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（45/57）

**有卡**：`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`PrimitiveBoolean`、`CLIPLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVImgToVideoInplace`、`LTXVDualCFGGuider`、`UNETLoader`、`ResolutionSelector`、`LoadImage`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`TextGenerateLTX2Prompt`、`CR Text`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
