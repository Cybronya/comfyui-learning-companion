---
key: 视频生成/图生视频/LTX2.3-PromptRelay-图生视频_2084829161968984065.json
name: LTX2.3-PromptRelay-图生视频_2084829161968984065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-PromptRelay-图生视频_2084829161968984065.json
hash: 2a3e9a297f9b835e
coverage: 0.820513
learned_at: 2026-10-16 20:35:31
nodes: [CheckpointLoaderSimple, PromptRelayEncodeTimeline, easy mathInt, easy mathInt, easy showAnything, EmptyLTXVLatentVideo, ComfyNumberConvert, ConditioningZeroOut, LTX2SamplingPreviewOverride, KSamplerSelect, LTXVConditioning, BasicScheduler, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, LoadImage, DualCLIPLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SamplerCustom, GetNode, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LTXVPreprocess, GetNode, LTXVEmptyLatentAudio, INTConstant, INTConstant, INTConstant, INTConstant, TSVideoCombineNoMetadata, VAEDecode, VisualizeSigmasKJ, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1_transformer_only_bf16.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-PromptRelay-图生视频_2084829161968984065.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-PromptRelay-图生视频_2084829161968984065.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `CheckpointLoaderSimple` ★核心
- `PromptRelayEncodeTimeline`
- `easy mathInt`
- `easy mathInt`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LoadImage`
- `DualCLIPLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SamplerCustom` ★核心
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `TSVideoCombineNoMetadata`
- `VAEDecode` ★核心
- `VisualizeSigmasKJ`
- `SaveImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1_transformer_only_bf16.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`CheckpointLoaderSimple`、`PromptRelayEncodeTimeline`、`easy mathInt`、`EmptyLTXVLatentVideo`、`ComfyNumberConvert`、`ConditioningZeroOut`、`LTX2SamplingPreviewOverride`、`KSamplerSelect`、`LTXVConditioning`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LoadImage`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`SamplerCustom`、`LTXVImgToVideoInplaceKJ`、`LTXVConcatAVLatent`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`INTConstant`、`TSVideoCombineNoMetadata`、`VAEDecode`、`VisualizeSigmasKJ`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
