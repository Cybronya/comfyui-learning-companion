---
key: 视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json
name: LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json
hash: 01e2cbc135adc44a
coverage: 0.824561
learned_at: 2026-10-16 21:27:36
nodes: [MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, KSamplerSelect, ManualSigmas, LTXVConditioning, KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, MarkdownNote, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, CLIPLoader, SaveVideo, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, VAEDecodeTiled, CreateVideo, LTXVAudioVAEDecode, CR Text, TextGenerateLTX2Prompt, LTXVImgToVideoInplace, VHS_VideoCombine, LTXVImgToVideoInplace, LTXVDualCFGGuider, UNETLoader, LTXVDualCFGGuider, ManualSigmas, CR Text, PreviewAny, easy showAnything, RH_LLMAPI_Pro_Node, LoadImage, ResolutionSelector, PrimitiveInt, MarkdownNote, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（57 个）：
- `MarkdownNote`
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
- `SaveVideo`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `CR Text`
- `TextGenerateLTX2Prompt`
- `LTXVImgToVideoInplace`
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `LTXVDualCFGGuider`
- `UNETLoader` ★核心
- `LTXVDualCFGGuider`
- `ManualSigmas`
- `CR Text`
- `PreviewAny`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveInt`
- `MarkdownNote`
- `PrimitiveBoolean`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（47/57）

**有卡**：`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`PrimitiveBoolean`、`CLIPLoader`、`SaveVideo`、`VAELoader`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`CR Text`、`TextGenerateLTX2Prompt`、`LTXVImgToVideoInplace`、`VHS_VideoCombine`、`LTXVDualCFGGuider`、`UNETLoader`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
