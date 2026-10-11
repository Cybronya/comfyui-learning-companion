---
key: 视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json
name: LTX-2.5文生视频（提示词指南）_2087564051504263169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json
hash: 41b5c8559c889e7b
coverage: 0.75
learned_at: 2026-10-11 20:53:37
nodes: [PrimitiveFloat, PrimitiveFloat, LTXVAudioVAEDecode, CreateVideo, SaveVideo, ComfyMathExpression, PrimitiveFloat, PrimitiveFloat, CLIPTextEncode, CLIPTextEncode, VAELoader, LTXFloatToInt, CLIPLoader, VAEDecodeTiled, RandomNoise, PrimitiveStringMultiline, PrimitiveInt, KSamplerSelect, SamplerCustomAdvanced, UNETLoader, PrimitiveStringMultiline, LTXVConditioning, LTXVSeparateAVLatent, VAELoader, ManualSigmas, CFGGuider, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, Int, Int, LTXVConcatAVLatent, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.5文生视频（提示词指南）_2087564051504263169.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LTXFloatToInt`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `VAELoader`
- `ManualSigmas`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `Int`
- `Int`
- `LTXVConcatAVLatent`
- `MarkdownNote`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（24/32）

**有卡**：`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`CLIPTextEncode`、`VAELoader`、`LTXFloatToInt`、`CLIPLoader`、`VAEDecodeTiled`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`UNETLoader`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`ManualSigmas`、`CFGGuider`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`Int`、`LTXVConcatAVLatent`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
