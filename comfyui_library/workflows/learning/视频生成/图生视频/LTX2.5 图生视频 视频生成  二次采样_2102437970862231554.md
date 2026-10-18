---
key: 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2102437970862231554.json
name: LTX2.5 图生视频 视频生成  二次采样_2102437970862231554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2102437970862231554.json
hash: fde8ae0b8d6bb52d
coverage: 0.877551
learned_at: 2026-10-17 02:28:53
nodes: [CLIPTextEncode, KSamplerSelect, PrimitiveInt, UNETLoader, VAELoader, PrimitiveInt, CLIPLoader, ResizeImageMaskNode, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVConditioning, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, CreateVideo, SaveVideo, CLIPTextEncode, LTXVDualCFGGuider, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, ResolutionSelector, VAELoader, CLIPLoader, PrimitiveBoolean, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, RandomNoise, TextGenerateLTX2Prompt, LTXVImgToVideoInplace, LatentUpscaleModelLoader, ManualSigmas, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2102437970862231554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2102437970862231554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveInt`
- `CLIPLoader`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `ComfySwitchNode`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
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
- `LTXVDualCFGGuider`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResolutionSelector`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveBoolean`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `TextGenerateLTX2Prompt`
- `LTXVImgToVideoInplace`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`CLIPTextEncode`、`KSamplerSelect`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PurgeVRAM_UTK`、`RandomNoise`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`PrimitiveBoolean`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`TextGenerateLTX2Prompt`、`LatentUpscaleModelLoader`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
