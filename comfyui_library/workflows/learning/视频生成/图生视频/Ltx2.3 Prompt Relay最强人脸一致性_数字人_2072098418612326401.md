---
key: 视频生成/图生视频/Ltx2.3 Prompt Relay最强人脸一致性_数字人_2072098418612326401.json
name: Ltx2.3 Prompt Relay最强人脸一致性_数字人_2072098418612326401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2072098418612326401.json
hash: 9a425655af3e0875
coverage: 0.736842
learned_at: 2026-10-15 22:40:51
nodes: [VAELoaderKJ, DualCLIPLoader, Note, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, GetNode, GetNode, LTXVImgToVideoInplaceKJ, BasicScheduler, SetNode, VAELoaderKJ, PromptRelaySmartEncode, KSamplerSelect, LTXVConditioning, ConditioningZeroOut, VAEDecode, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LoadImage, CR Prompt Text, SamplerCustom, LTXVConcatAVLatent, VisualizeSigmasKJ, PreviewImage, LTXVEmptyLatentAudio, Note, SetNode, Note, LTX2SamplingPreviewOverride, CR Prompt Text, VHS_VideoCombine, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 Prompt Relay最强人脸一致性_数字人_2072098418612326401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072098418612326401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `VAELoaderKJ`
- `DualCLIPLoader`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `BasicScheduler`
- `SetNode`
- `VAELoaderKJ`
- `PromptRelaySmartEncode`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `SamplerCustom` ★核心
- `LTXVConcatAVLatent`
- `VisualizeSigmasKJ`
- `PreviewImage`
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `SetNode`
- `Note`
- `LTX2SamplingPreviewOverride`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `JWInteger`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`BasicScheduler`、`PromptRelaySmartEncode`、`KSamplerSelect`、`LTXVConditioning`、`ConditioningZeroOut`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LoadImage`、`CR Prompt Text`、`SamplerCustom`、`LTXVConcatAVLatent`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTX2SamplingPreviewOverride`、`VHS_VideoCombine`、`JWInteger`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
