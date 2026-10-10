---
key: 视频生成/图生视频/【MINIMAX-H3】9图3音多参二采.json
name: 【MINIMAX-H3】9图3音多参二采
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【MINIMAX-H3】9图3音多参二采.json
hash: f2088ff7f57c6e7c
coverage: 0.386139
learned_at: 2026-10-10 22:54:43
nodes: [SolAttnMiniMax, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, SetNode, VAELoader, SetNode, CLIPLoader, CLIPLoader, SetNode, MarkdownNote, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ModelAttentionBackend, GetNode, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, SetNode, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, SetNode, MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, LayerUtility: ImageScaleByAspectRatio V2, ModelAttentionBackend, GetNode, SetNode, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderBypassModelOnly, 忽略多组孤海, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3LearnedLatentUpscaleT8Advanced, ComfyMathExpression, PrimitiveFloat, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, LoadAudio, GetNode, RandomNoise, 忽略多组孤海, LoadImage, MiniMaxH3AudioConditioningT8, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Prompt Text]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, 忽略多组孤海, 忽略多组孤海, CR Prompt Text]
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/【MINIMAX-H3】9图3音多参二采.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【MINIMAX-H3】9图3音多参二采.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（101 个）：
- `SolAttnMiniMax`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `SetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelAttentionBackend`
- `GetNode`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `SetNode`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelAttentionBackend`
- `GetNode`
- `SetNode`
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `忽略多组孤海`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `GetNode`
- `RandomNoise`
- `忽略多组孤海`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **39%**（39/101）

**有卡**：`SolAttnMiniMax`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAELoader`、`CLIPLoader`、`ModelAttentionBackend`、`BasicGuider`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`ComfyMathExpression`、`LoadImage`、`LoadAudio`、`RandomNoise`、`ResolutionSelector`

**缺卡**（12）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`忽略多组孤海`、`忽略多组孤海`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
