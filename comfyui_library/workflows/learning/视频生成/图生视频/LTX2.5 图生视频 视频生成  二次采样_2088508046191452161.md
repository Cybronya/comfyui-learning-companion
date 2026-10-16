---
key: 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508046191452161.json
name: LTX2.5 图生视频 视频生成  二次采样_2088508046191452161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508046191452161.json
hash: 5a6e40131ccb8f72
coverage: 0.877551
learned_at: 2026-10-16 21:43:22
nodes: [LTXVDualCFGGuider, CLIPTextEncode, PrimitiveInt, ManualSigmas, KSamplerSelect, PrimitiveInt, ResolutionSelector, PrimitiveInt, UNETLoader, VAELoader, VAELoader, PrimitiveInt, PrimitiveBoolean, CLIPLoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, LTXVPreprocess, TextGenerateLTX2Prompt, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVLatentUpsampler, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, CLIPTextEncode, PrimitiveStringMultiline, LTXVConditioning, RandomNoise, LatentUpscaleModelLoader, SamplerCustomAdvanced, ManualSigmas, LTXVSeparateAVLatent, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, RandomNoise, LTXVAudioVAEDecode, CreateVideo, SaveVideo, CLIPLoader, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508046191452161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2088508046191452161.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `LTXVDualCFGGuider`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
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
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `LTXVConditioning`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `PurgeVRAM_UTK`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`LTXVDualCFGGuider`、`CLIPTextEncode`、`ManualSigmas`、`KSamplerSelect`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`PrimitiveBoolean`、`CLIPLoader`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`LTXVConditioning`、`RandomNoise`、`LatentUpscaleModelLoader`、`PurgeVRAM_UTK`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
