---
key: 视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json
name: LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json
hash: ecbff7346bb64cce
coverage: 0.742857
learned_at: 2026-10-15 22:37:20
nodes: [SetNode, GetNode, SetNode, VisualizeSigmasKJ, GetNode, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustom, GetNode, BasicScheduler, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, VAEDecode, LTXVAudioVAEDecode, LTXVPreprocess, LTXVEmptyLatentAudio, Int, Int, EmptyLTXVLatentVideo, PrimitiveNode, UNETLoader, LoraLoaderModelOnly, LTXVImgToVideoInplaceKJ, LTXVConditioning, PathchSageAttentionKJ, ConditioningZeroOut, LoadImage, VHS_VideoCombine, GetNode, KSamplerSelect, PromptRelayEncode, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/LTX2.3 Prompt时间戳控制视频生成_2050810161220071425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050810161220071425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（35 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `VisualizeSigmasKJ`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `GetNode`
- `BasicScheduler`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `LTXVEmptyLatentAudio` ★核心
- `Int`
- `Int`
- `EmptyLTXVLatentVideo`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `ConditioningZeroOut`
- `LoadImage`
- `VHS_VideoCombine`
- `GetNode`
- `KSamplerSelect` ★核心
- `PromptRelayEncode`
- `Note`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（26/35）

**有卡**：`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`SamplerCustom`、`BasicScheduler`、`VAELoaderKJ`、`DualCLIPLoader`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`Int`、`EmptyLTXVLatentVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplaceKJ`、`LTXVConditioning`、`PathchSageAttentionKJ`、`ConditioningZeroOut`、`LoadImage`、`VHS_VideoCombine`、`KSamplerSelect`、`PromptRelayEncode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
