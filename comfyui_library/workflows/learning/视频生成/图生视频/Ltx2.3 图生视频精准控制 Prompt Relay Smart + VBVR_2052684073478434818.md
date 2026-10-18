---
key: 视频生成/图生视频/Ltx2.3 图生视频精准控制 Prompt Relay Smart + VBVR_2052684073478434818.json
name: Ltx2.3 图生视频精准控制 Prompt Relay Smart + VBVR_2052684073478434818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 图生视频精准控制 Prompt Relay Smart + VBVR_2052684073478434818.json
hash: 5102c9ddabe805c8
coverage: 0.736842
learned_at: 2026-10-15 22:37:31
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, SetNode, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, GetNode, KSamplerSelect, ConditioningZeroOut, PathchSageAttentionKJ, LTXVConcatAVLatent, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, UNETLoader, DualCLIPLoader, LTXVImgToVideoInplaceKJ, EmptyLTXVLatentVideo, LTXVPreprocess, PromptRelaySmartEncode, Note, Note, CR Prompt Text, LTXVConditioning, SamplerCustom, BasicScheduler, VisualizeSigmasKJ, LTXVEmptyLatentAudio, Note, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, JWInteger, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 30, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 图生视频精准控制 Prompt Relay Smart + VBVR_2052684073478434818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052684073478434818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LTXVImgToVideoInplaceKJ`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `PromptRelaySmartEncode`
- `Note`
- `Note`
- `CR Prompt Text`
- `LTXVConditioning`
- `SamplerCustom` ★核心
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `JWInteger`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `489`
- `height` = `30`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VHS_VideoCombine`、`KSamplerSelect`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`UNETLoader`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`PromptRelaySmartEncode`、`CR Prompt Text`、`LTXVConditioning`、`SamplerCustom`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
