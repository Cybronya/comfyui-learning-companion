---
key: 视频生成/文生视频/A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970.json
name: A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970.json
hash: 16861eb9ea9014db
coverage: 0.82
learned_at: 2026-10-15 22:43:57
nodes: [SaveVideo, ResolutionSelector, CreateVideo, LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, LTXVAudioVAEDecode, KSamplerSelect, LTXVDualCFGGuider, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, SamplerCustomAdvanced, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, RandomNoise, LTXVConditioning, LTXVConcatAVLatent, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, PreviewAny, ComfySwitchNode, LatentUpscaleModelLoader, UNETLoader, VAELoader, VAELoader, CLIPLoader, TextGenerateLTX2Prompt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, CLIPLoader, PrimitiveBoolean, ImageFromBatch, SaveImage, SaveAudio, VHS_VideoCombine, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/A-8 LTX-2.5 文生视频（T2V）· 音画同步生成_2087369134014291970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `SaveVideo`
- `ResolutionSelector`
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
- `ImageFromBatch`
- `SaveImage`
- `SaveAudio`
- `VHS_VideoCombine`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（41/50）

**有卡**：`SaveVideo`、`ResolutionSelector`、`CreateVideo`、`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`PrimitiveBoolean`、`ImageFromBatch`、`SaveImage`、`SaveAudio`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
