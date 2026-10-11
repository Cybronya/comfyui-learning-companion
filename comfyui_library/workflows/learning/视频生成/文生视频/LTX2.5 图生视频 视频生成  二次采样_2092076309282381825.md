---
key: 视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092076309282381825.json
name: LTX2.5 图生视频 视频生成  二次采样_2092076309282381825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092076309282381825.json
hash: 08b788345f880c1d
coverage: 0.843137
learned_at: 2026-10-11 21:19:42
nodes: [KSamplerSelect, PrimitiveInt, UNETLoader, VAELoader, PrimitiveInt, CLIPLoader, ResizeImageMaskNode, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVConditioning, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SamplerCustomAdvanced, CreateVideo, SaveVideo, CLIPTextEncode, LTXVDualCFGGuider, PrimitiveInt, VAELoader, CLIPLoader, PrimitiveBoolean, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, RandomNoise, TextGenerateLTX2Prompt, LTXVImgToVideoInplace, LatentUpscaleModelLoader, ManualSigmas, LoadImage, CLIPTextEncode, PrimitiveStringMultiline, ResolutionSelector, PrimitiveInt, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092076309282381825.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 图生视频 视频生成  二次采样_2092076309282381825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
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
- `PrimitiveInt`
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
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveInt`
- `孤海注释`
- `孤海注释`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`KSamplerSelect`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PurgeVRAM_UTK`、`RandomNoise`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`TextGenerateLTX2Prompt`、`LatentUpscaleModelLoader`、`LoadImage`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
