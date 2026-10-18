---
key: 视频生成/图生视频/Ltx2.3单图生视频精准运镜Prompt Relay Smart + VBVR_2053103007134429186.json
name: Ltx2.3单图生视频精准运镜Prompt Relay Smart + VBVR_2053103007134429186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3单图生视频精准运镜Prompt Relay Smart + VBVR_2053103007134429186.json
hash: 70f8388195f861ad
coverage: 0.769231
learned_at: 2026-10-15 22:37:36
nodes: [SetNode, SetNode, LTXVSeparateAVLatent, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, VAELoaderKJ, CR Prompt Text, CR Prompt Text, DualCLIPLoader, PromptRelaySmartEncode, ConditioningZeroOut, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, KSamplerSelect, VisualizeSigmasKJ, BasicScheduler, GetNode, LTXVAudioVAEDecode, GetNode, PreviewImage, LTXVConcatAVLatent, GetNode, LTXVEmptyLatentAudio, LTXVPreprocess, VAELoaderKJ, EmptyLTXVLatentVideo, GetNode, LTXVImgToVideoInplaceKJ, VAEDecode, JWInteger, JWInteger, VHS_VideoCombine, LoadImage, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3单图生视频精准运镜Prompt Relay Smart + VBVR_2053103007134429186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053103007134429186.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VAELoaderKJ`
- `CR Prompt Text`
- `CR Prompt Text`
- `DualCLIPLoader`
- `PromptRelaySmartEncode`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PreviewImage`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `VAEDecode` ★核心
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`CR Prompt Text`、`DualCLIPLoader`、`PromptRelaySmartEncode`、`ConditioningZeroOut`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`KSamplerSelect`、`VisualizeSigmasKJ`、`BasicScheduler`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`VAEDecode`、`JWInteger`、`VHS_VideoCombine`、`LoadImage`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
