---
name: unknown_workflow_lora_sampler_unet_203
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.797333
common_nodes: [BasicScheduler, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewImage, PromptRelayEncode, SamplerCustom, SetNode, UNETLoader, VAEDecode, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/反推提示词/76tsspdjt_2052667532313669633.json, 图片生成/图生图/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2057109101624258561.json, 图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_203

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/76tsspdjt_2052667532313669633.json、图片生成/图生图/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2057109101624258561.json、图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PromptRelayEncode`
- `SamplerCustom`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `CM_IntBinaryOperation` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `Int` —— 1/3 个有
- `JWStringConcat` —— 1/3 个有
- `JWStringSplit` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `SomethingToString` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 489 - 489 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 489 - 489，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
