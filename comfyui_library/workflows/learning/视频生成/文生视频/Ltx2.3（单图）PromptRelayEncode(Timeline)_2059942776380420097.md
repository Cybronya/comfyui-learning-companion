---
key: 视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json
name: Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json
hash: 0bee4bc4dd00c680
coverage: 0.54
learned_at: 2026-10-11 19:49:40
nodes: [SetNode, SetNode, LTXVAudioVAEDecode, easy getNode, easy getNode, easy getNode, LoraLoaderModelOnly, LTXVPreprocess, Int, GetNode, DualCLIPLoader, GetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, GetNode, easy setNode, EmptyLTXVLatentVideo, Float, easy setNode, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, SetNode, UNETLoader, easy getNode, GetNode, LTXVSeparateAVLatent, GetNode, VAEDecode, easy setNode, easy setNode, LTXVConditioning, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, GetNode, LTXVImgToVideoInplaceKJ, LTX2SamplingPreviewOverride, PreviewImage, Int, ConditioningZeroOut, VHS_VideoCombine, VisualizeSigmasKJ, SamplerCustom, Float to Int, LTXVEmptyLatentAudio, GetNode, LoadImage, PromptRelayEncodeTimeline]
patterns: []
missing: [Float to Int, LayerUtility: ImageScaleByAspectRatio V2, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy setNode]
parameters: {"batch_size": 1, "height": 25, "width": 489}
discoveries: [次要节点 `Float to Int` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识, 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVPreprocess`
- `Int`
- `GetNode`
- `DualCLIPLoader`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy setNode`
- `EmptyLTXVLatentVideo`
- `Float`
- `easy setNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader` ★核心
- `easy getNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `easy setNode`
- `easy setNode`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `Int`
- `ConditioningZeroOut`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `SamplerCustom` ★核心
- `Float to Int`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LoadImage`
- `PromptRelayEncodeTimeline`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（27/50）

**有卡**：`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`LTXVPreprocess`、`Int`、`DualCLIPLoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`Float`、`PathchSageAttentionKJ`、`UNETLoader`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConditioning`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`LTX2SamplingPreviewOverride`、`ConditioningZeroOut`、`VHS_VideoCombine`、`VisualizeSigmasKJ`、`SamplerCustom`、`LTXVEmptyLatentAudio`、`LoadImage`、`PromptRelayEncodeTimeline`

**缺卡**（10）：`Float to Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy getNode`、`easy getNode`、`easy getNode`、`easy getNode`、`easy setNode`、`easy setNode`、`easy setNode`、`easy setNode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent

## 学习发现

- 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy getNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
- 次要节点 `easy setNode` 知识库中没有该节点类型的任何知识
