---
key: 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json
name: LTX2.5 图生视频 视频生成  二次采样_2088139583937662977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json
hash: 5a7c9ae552a0e61c
coverage: 0.877551
learned_at: 2026-10-16 21:27:36
nodes: [LTXVDualCFGGuider, CLIPTextEncode, PrimitiveInt, RandomNoise, ManualSigmas, KSamplerSelect, PrimitiveInt, ResolutionSelector, PrimitiveInt, UNETLoader, VAELoader, VAELoader, PrimitiveInt, CLIPLoader, PrimitiveBoolean, CLIPLoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, LTXVPreprocess, TextGenerateLTX2Prompt, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVImgToVideoInplace, LTXVConditioning, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, CreateVideo, SaveVideo, CLIPTextEncode, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088139583937662977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `LTXVDualCFGGuider`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
- `CLIPLoader`
- `PrimitiveBoolean`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfySwitchNode`
- `LTXVImgToVideoInplace`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `PurgeVRAM_UTK`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`LTXVDualCFGGuider`、`CLIPTextEncode`、`RandomNoise`、`ManualSigmas`、`KSamplerSelect`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`PrimitiveBoolean`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`PurgeVRAM_UTK`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
