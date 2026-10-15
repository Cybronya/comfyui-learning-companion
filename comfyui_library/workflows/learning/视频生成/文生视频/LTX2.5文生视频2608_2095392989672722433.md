---
key: 视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json
name: LTX2.5文生视频2608_2095392989672722433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json
hash: 95082a1642c44c26
coverage: 0.77551
learned_at: 2026-10-15 22:45:17
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, KSamplerSelect, LTXVDualCFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, RandomNoise, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewAny, ComfySwitchNode, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, TextGenerateLTX2Prompt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, CLIPLoader, PrimitiveBoolean, CLIPLoader, ResolutionSelector, MarkdownNote, LTXVSeparateAVLatent, VHS_VideoCombine, LTXVAudioVAEDecode, FlashVSRNode, VHS_VideoCombine, VAEDecodeTiled, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频2608_2095392989672722433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（49 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
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
- `TextGenerateLTX2Prompt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `PrimitiveBoolean`
- `CLIPLoader`
- `ResolutionSelector`
- `MarkdownNote`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `FlashVSRNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`KSamplerSelect`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`CLIPLoader`、`PrimitiveBoolean`、`ResolutionSelector`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`FlashVSRNode`、`VAEDecodeTiled`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
