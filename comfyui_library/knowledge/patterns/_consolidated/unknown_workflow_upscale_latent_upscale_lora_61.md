---
name: unknown_workflow_upscale_latent_upscale_lora_61
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91375
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/LTX-2图_3图NVFP4首尾帧_2009643807456890881.json, 视频生成/文生视频/LTX-2图_3图首尾帧_2009549891193806850.json, 视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json, 视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/LTX-2图_3图NVFP4首尾帧_2009643807456890881.json、视频生成/文生视频/LTX-2图_3图首尾帧_2009549891193806850.json、视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json、视频生成/文生视频/LTX2.3文_图生视频_2031625412933062658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `ManualSigmas` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `FloatConstant` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LTXVMiddleFrame_TTP` —— 2/4 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `LTX2_NAG` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.35 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
