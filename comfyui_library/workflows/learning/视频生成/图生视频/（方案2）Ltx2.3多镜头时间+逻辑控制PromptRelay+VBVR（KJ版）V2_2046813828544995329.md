---
key: 视频生成/图生视频/（方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json
name: （方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046813828544995329.json
hash: a3d9a1d14ad9d7a5
coverage: 0.736842
learned_at: 2026-10-15 22:37:01
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTXVPreprocess, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVConcatAVLatent, GetNode, BasicScheduler, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, PreviewImage, ConditioningZeroOut, GetNode, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, PromptRelayEncode, CR Prompt Text, JWInteger, Note, Note, Note, LTXVImgToVideoInplaceKJ, LoadImage, UNETLoader, CR Prompt Text, PathchSageAttentionKJ, LTXVConditioning, SamplerCustom, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/（方案2）Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）V2_2046813828544995329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046813828544995329.json`

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
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `PreviewImage`
- `ConditioningZeroOut`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `CR Prompt Text`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `PathchSageAttentionKJ`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`DualCLIPLoader`、`ConditioningZeroOut`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`PromptRelayEncode`、`CR Prompt Text`、`JWInteger`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVConditioning`、`SamplerCustom`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
