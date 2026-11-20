---
name: unknown_workflow_upscale_latent_upscale_lora_70
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.902
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json, 视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json, 视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json, 视频生成/文生视频/图生视频极速版LTX2.3  数字人话 唱歌对口型_2044214545626963970.json, 视频生成/文生视频/🐱LTX2.3图生视频工作流_2030298909729361921.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_70

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json、视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json、视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json、视频生成/文生视频/图生视频极速版LTX2.3  数字人话 唱歌对口型_2044214545626963970.json、视频生成/文生视频/🐱LTX2.3图生视频工作流_2030298909729361921.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `LTX2_NAG` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `PrimitiveBoolean` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `BasicScheduler` —— 1/5 个有
- `CM_FloatToInt` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LTX2SamplingPreviewOverride` —— 1/5 个有
- `LTXVChunkFeedForward` —— 1/5 个有
- `LTXVImgToVideoConditionOnly` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 4 | 100% |
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
