---
key: 视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json
name: LTX2.3 自用版 T2V_2063969490962042881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json
hash: 95386739a1dfe5e9
coverage: 0.78
learned_at: 2026-10-11 20:21:26
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, EmptyLTXVLatentVideo, PrimitiveInt, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, MarkdownNote, ComfyMathExpression, LTXVConcatAVLatent, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, LatentUpscaleModelLoader, CFGGuider, BasicScheduler, CLIPTextEncode, CFGGuider, ManualSigmas, LatentUpscaleModelLoader, Reroute, LTXVLatentUpsampler, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, KSamplerSelect, VAEDecodeTiled, SimpleMath+, LTXVAudioVAEDecode, PrimitiveInt, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PromptRelayEncode, Note, LTXTiledSampler, ManualSigmas, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LTX2_NAG, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, PrimitiveStringMultiline, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 自用版 T2V_2063969490962042881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（50 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `VAEDecodeTiled` ★核心
- `SimpleMath+`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `Note`
- `LTXTiledSampler` ★核心
- `ManualSigmas`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LTX2_NAG`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（39/50）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`ComfyMathExpression`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`CFGGuider`、`BasicScheduler`、`CLIPTextEncode`、`ManualSigmas`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`PromptRelayEncode`、`LTXTiledSampler`、`LTX2_NAG`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`UNETLoader`

**缺卡**（3）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXTiledSampler

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
