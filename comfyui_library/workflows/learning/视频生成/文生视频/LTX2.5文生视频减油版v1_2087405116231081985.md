---
key: 视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json
name: LTX2.5文生视频减油版v1_2087405116231081985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json
hash: 523c22fba11b062a
coverage: 0.795918
learned_at: 2026-10-11 20:53:38
nodes: [LTXVConditioning, RandomNoise, PrimitiveInt, LTXVDualCFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, RandomNoise, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, PrimitiveInt, MarkdownNote, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, ResolutionSelector, UNETLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, LatentUpscaleModelLoader, SamplerCustomAdvanced, VHS_VideoCombine, SaveVideo, CreateVideo, PreviewAny, CR Text, ComfySwitchNode, TextGenerateLTX2Prompt, easy showAnything, RH_LLMAPI_Pro_Node, PrimitiveStringMultiline, ManualSigmas, ManualSigmas]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5文生视频减油版v1_2087405116231081985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `LTXVConditioning`
- `RandomNoise`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `SaveVideo`
- `CreateVideo`
- `PreviewAny`
- `CR Text`
- `ComfySwitchNode`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveStringMultiline`
- `ManualSigmas`
- `ManualSigmas`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（39/49）

**有卡**：`LTXVConditioning`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`ResolutionSelector`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`SaveVideo`、`CreateVideo`、`TextGenerateLTX2Prompt`、`RH_LLMAPI_Pro_Node`

**缺卡**（1）：`CR Text`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
