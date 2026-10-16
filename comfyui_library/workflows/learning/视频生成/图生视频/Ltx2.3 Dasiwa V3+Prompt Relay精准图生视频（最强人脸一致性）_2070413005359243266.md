---
key: 视频生成/图生视频/Ltx2.3 Dasiwa V3+Prompt Relay精准图生视频（最强人脸一致性）_2070413005359243266.json
name: Ltx2.3 Dasiwa V3+Prompt Relay精准图生视频（最强人脸一致性）_2070413005359243266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070413005359243266.json
hash: 6f5c7cb3a522726d
coverage: 0.75
learned_at: 2026-10-15 22:40:39
nodes: [LTXVAudioVAEDecode, GetNode, VisualizeSigmasKJ, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, GetNode, LTXVConditioning, KSamplerSelect, ConditioningZeroOut, BasicScheduler, LTXVConcatAVLatent, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LoadImage, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, PromptRelaySmartEncode, CR Prompt Text, Note, Note, Note, SetNode, PreviewImage, LTXVImgToVideoInplaceKJ, SamplerCustom, PathchSageAttentionKJ, VHS_VideoCombine, CR Prompt Text, JWInteger, SetNode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 Dasiwa V3+Prompt Relay精准图生视频（最强人脸一致性）_2070413005359243266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070413005359243266.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PromptRelaySmartEncode`
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `PreviewImage`
- `LTXVImgToVideoInplaceKJ`
- `SamplerCustom` ★核心
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `JWInteger`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（30/40）

**有卡**：`LTXVAudioVAEDecode`、`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VHS_VideoCombine`、`LTXVConditioning`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LoadImage`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`PromptRelaySmartEncode`、`CR Prompt Text`、`LTXVImgToVideoInplaceKJ`、`SamplerCustom`、`PathchSageAttentionKJ`、`JWInteger`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
