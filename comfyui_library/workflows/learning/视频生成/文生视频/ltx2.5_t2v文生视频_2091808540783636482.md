---
key: 视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json
name: ltx2.5_t2v文生视频_2091808540783636482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json
hash: 32d8511f3272b6ec
coverage: 0.77551
learned_at: 2026-10-11 21:19:51
nodes: [MarkdownNote, MarkdownNote, CreateVideo, LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, LTXVAudioVAEDecode, KSamplerSelect, LTXVDualCFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, RandomNoise, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewAny, ComfySwitchNode, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, PrimitiveBoolean, TextGenerateLTX2Prompt, ResolutionSelector, MarkdownNote, CLIPLoader, MarkdownNote, LoadImage, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.5_t2v文生视频_2091808540783636482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `MarkdownNote`
- `MarkdownNote`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `PreviewAny`
- `ComfySwitchNode`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`CreateVideo`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`LoadImage`、`SaveVideo`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
