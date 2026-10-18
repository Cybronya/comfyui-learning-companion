---
key: 视频生成/图生视频/Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054525634252165121.json
name: Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054525634252165121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054525634252165121.json
hash: 1b59c374e6a103e2
coverage: 0.74359
learned_at: 2026-10-15 22:37:48
nodes: [LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVConcatAVLatent, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, SetNode, UNETLoader, SetNode, VHS_VideoCombine, CR Prompt Text, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVImgToVideoInplaceKJ, LTXVPreprocess, GetNode, PreviewImage, VHS_VideoCombine, SamplerCustom, KSamplerSelect, JWInteger, LoadImage, Note, Note, Note, LoraLoaderModelOnly, PathchSageAttentionKJ, PromptRelaySmartEncode, LTXVConditioning, ConditioningZeroOut, BasicScheduler, VisualizeSigmasKJ, LTX2SamplingPreviewOverride]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 Dasiwa V2+Prompt Relay精准图生视频_2054525634252165121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054525634252165121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `JWInteger`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PromptRelaySmartEncode`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`UNETLoader`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`、`SamplerCustom`、`KSamplerSelect`、`JWInteger`、`LoadImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`PromptRelaySmartEncode`、`LTXVConditioning`、`ConditioningZeroOut`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
