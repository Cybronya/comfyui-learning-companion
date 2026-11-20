---
key: 平台全量/ltx2.5-disttilled 文生视频_2117862405958098946.json
name: ltx2.5-disttilled 文生视频_2117862405958098946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ltx2.5-disttilled 文生视频_2117862405958098946.json
hash: 608a0f6bb554b430
coverage: 0.804348
learned_at: 2026-11-14 01:14:39
nodes: [SaveVideo, MarkdownNote, ResolutionSelector, MarkdownNote, CreateVideo, LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, LTXVAudioVAEDecode, KSamplerSelect, LTXVDualCFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, RandomNoise, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewAny, ComfySwitchNode, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, CLIPLoader, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/ltx2.5-disttilled 文生视频_2117862405958098946.json

> 来源文件 `comfyui_library/workflows/平台全量/ltx2.5-disttilled 文生视频_2117862405958098946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `SaveVideo`
- `MarkdownNote`
- `ResolutionSelector`
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
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `PrimitiveBoolean`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（37/46）

**有卡**：`SaveVideo`、`ResolutionSelector`、`CreateVideo`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`PrimitiveBoolean`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、ResolutionSelector、UNETLoader、KSamplerSelect、LTXVDualCFGGuider、LTXVLatentUpsampler
