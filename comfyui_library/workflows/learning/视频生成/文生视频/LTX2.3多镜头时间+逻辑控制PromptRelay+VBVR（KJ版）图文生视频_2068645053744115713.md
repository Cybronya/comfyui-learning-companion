---
key: 视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713.json
name: LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713.json
hash: f8d090cbc6624c40
coverage: 0.736842
learned_at: 2026-10-15 22:45:08
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTXVPreprocess, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVConcatAVLatent, LTXVConditioning, GetNode, BasicScheduler, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SamplerCustom, SetNode, PreviewImage, ConditioningZeroOut, GetNode, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, JWInteger, LTXVImgToVideoInplaceKJ, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, Note, PromptRelayEncode, Note, Note, CR Prompt Text, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2068645053744115713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `VisualizeSigmasKJ`
- `LTXVPreprocess`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SamplerCustom` ★核心
- `SetNode`
- `PreviewImage`
- `ConditioningZeroOut`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `JWInteger`
- `LTXVImgToVideoInplaceKJ`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `PromptRelayEncode`
- `Note`
- `Note`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVConditioning`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`DualCLIPLoader`、`SamplerCustom`、`ConditioningZeroOut`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`JWInteger`、`LTXVImgToVideoInplaceKJ`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`PromptRelayEncode`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
