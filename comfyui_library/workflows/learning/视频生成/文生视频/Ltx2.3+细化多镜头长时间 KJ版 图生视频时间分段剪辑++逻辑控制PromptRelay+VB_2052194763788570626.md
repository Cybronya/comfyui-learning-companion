---
key: 视频生成/文生视频/Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626.json
name: Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626.json
hash: 5d3fff4e408f5040
coverage: 0.714286
learned_at: 2026-10-11 19:49:40
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, LTXVConcatAVLatent, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, PreviewImage, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncode, UNETLoader, PathchSageAttentionKJ, LTXVConditioning, SamplerCustom, LoraLoaderModelOnly, GetNode, VisualizeSigmasKJ, LTXVEmptyLatentAudio, GetNode, BasicScheduler, GetNode, LTXVImgToVideoInplaceKJ, ConditioningZeroOut, LTXVPreprocess, VHS_VideoCombine, LoadImage, CR Prompt Text, CR Prompt Text, JWInteger]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "height": 25, "width": 489}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3+细化多镜头长时间 KJ版 图生视频时间分段剪辑++逻辑控制PromptRelay+VB_2052194763788570626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `PreviewImage`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PromptRelayEncode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `ConditioningZeroOut`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `JWInteger`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`VAELoaderKJ`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`PromptRelayEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVConditioning`、`SamplerCustom`、`LoraLoaderModelOnly`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`LTXVImgToVideoInplaceKJ`、`ConditioningZeroOut`、`LTXVPreprocess`、`VHS_VideoCombine`、`LoadImage`、`JWInteger`

**缺卡**（3）：`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
