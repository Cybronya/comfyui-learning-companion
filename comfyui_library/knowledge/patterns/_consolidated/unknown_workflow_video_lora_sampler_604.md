---
name: unknown_workflow_video_lora_sampler_604
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.957667
common_nodes: [BasicScheduler, CLIPTextEncode, ComfyNumberConvert, EmptyLTXVLatentVideo, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SimpleCalculatorKJ, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5多参视频生成MSR2+BFS_2087556124504584194.json, 视频生成/图生视频/2079557300314005506.json, 视频生成/图生视频/2081015691444047873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_604

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5多参视频生成MSR2+BFS_2087556124504584194.json、视频生成/图生视频/2079557300314005506.json、视频生成/图生视频/2081015691444047873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `LiconMSR` —— 2/3 个有
- `PromptRelayEncode` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CLIPLoader` —— 1/3 个有
- `LTXVDualCFGGuider` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `YuanCLIPTimeline` —— 1/3 个有
- `YuanTool` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 241 | 3 | 100% |
| 高度 | 24 | 24 - 24 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 241，3 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
