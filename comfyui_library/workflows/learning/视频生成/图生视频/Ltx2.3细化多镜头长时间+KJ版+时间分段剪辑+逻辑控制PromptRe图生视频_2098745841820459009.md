---
key: 视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098745841820459009.json
name: Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098745841820459009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098745841820459009.json
hash: 7596fabdc4437e26
coverage: 0.8
learned_at: 2026-10-17 01:44:30
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, LTXVConcatAVLatent, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, SetNode, PreviewImage, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, PromptRelayEncode, UNETLoader, PathchSageAttentionKJ, LTXVConditioning, SamplerCustom, LoraLoaderModelOnly, GetNode, VisualizeSigmasKJ, LTXVEmptyLatentAudio, GetNode, BasicScheduler, GetNode, LTXVImgToVideoInplaceKJ, ConditioningZeroOut, LTXVPreprocess, VHS_VideoCombine, JWInteger, LoadImage, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098745841820459009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098745841820459009.json`

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
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`VAELoaderKJ`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`PromptRelayEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVConditioning`、`SamplerCustom`、`LoraLoaderModelOnly`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`LTXVImgToVideoInplaceKJ`、`ConditioningZeroOut`、`LTXVPreprocess`、`VHS_VideoCombine`、`JWInteger`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
