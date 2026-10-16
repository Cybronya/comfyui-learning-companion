---
key: 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2093745280222064641.json
name: LTX2.5 图生视频 视频生成  二次采样_2093745280222064641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2093745280222064641.json
hash: d30eac99a06e9f21
coverage: 0.877551
learned_at: 2026-10-16 23:42:08
nodes: [CLIPTextEncode, KSamplerSelect, PrimitiveInt, UNETLoader, VAELoader, CLIPLoader, ResizeImageMaskNode, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVConditioning, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, CreateVideo, SaveVideo, LTXVDualCFGGuider, ResolutionSelector, VAELoader, CLIPLoader, PrimitiveBoolean, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, RandomNoise, TextGenerateLTX2Prompt, LTXVImgToVideoInplace, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, PrimitiveInt, PrimitiveInt, CLIPTextEncode, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2093745280222064641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5 图生视频 视频生成  二次采样_2093745280222064641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
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
- `LTXVDualCFGGuider`
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
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`CLIPTextEncode`、`KSamplerSelect`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PurgeVRAM_UTK`、`RandomNoise`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`PrimitiveBoolean`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`TextGenerateLTX2Prompt`、`LatentUpscaleModelLoader`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
