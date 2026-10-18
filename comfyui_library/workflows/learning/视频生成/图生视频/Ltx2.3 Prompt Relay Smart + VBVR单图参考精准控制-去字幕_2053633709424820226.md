---
key: 视频生成/图生视频/Ltx2.3 Prompt Relay Smart + VBVR单图参考精准控制-去字幕_2053633709424820226.json
name: Ltx2.3 Prompt Relay Smart + VBVR单图参考精准控制-去字幕_2053633709424820226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 Prompt Relay Smart + VBVR单图参考精准控制-去字幕_2053633709424820226.json
hash: e93efc83a706d056
coverage: 0.826087
learned_at: 2026-10-15 22:37:40
nodes: [GetNode, LTXVSeparateAVLatent, GetNode, LTXVAudioVAEDecode, Int, SimpleMath+, Int, LTXVEmptyLatentAudio, VAEDecode, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, KSamplerSelect, PromptRelaySmartEncode, LTXVConditioning, GetNode, SamplerCustom, BasicScheduler, LTX2SamplingPreviewOverride, CR Prompt Text, LoadImage, Float, VHS_VideoCombine, VHS_VideoCombine, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, DualCLIPLoader, LTX2SamplingPreviewOverride, VAELoaderKJ, CheckpointLoaderSimple, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVPreprocess, GetNode, VisualizeSigmasKJ, CLIPTextEncode, PreviewImage, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, easy seed, CR Prompt Text, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3 Prompt Relay Smart + VBVR单图参考精准控制-去字幕_2053633709424820226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053633709424820226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `Int`
- `SimpleMath+`
- `Int`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecode` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `PromptRelaySmartEncode`
- `LTXVConditioning`
- `GetNode`
- `SamplerCustom` ★核心
- `BasicScheduler`
- `LTX2SamplingPreviewOverride`
- `CR Prompt Text`
- `LoadImage`
- `Float`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVPreprocess`
- `GetNode`
- `VisualizeSigmasKJ`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy seed`
- `CR Prompt Text`
- `MarkdownNote`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（38/46）

**有卡**：`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`Int`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`VAEDecode`、`LTXVImgToVideoInplaceKJ`、`LTXVConcatAVLatent`、`KSamplerSelect`、`PromptRelaySmartEncode`、`LTXVConditioning`、`SamplerCustom`、`BasicScheduler`、`LTX2SamplingPreviewOverride`、`CR Prompt Text`、`LoadImage`、`Float`、`VHS_VideoCombine`、`VAELoaderKJ`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LTXVPreprocess`、`VisualizeSigmasKJ`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、easy seed
