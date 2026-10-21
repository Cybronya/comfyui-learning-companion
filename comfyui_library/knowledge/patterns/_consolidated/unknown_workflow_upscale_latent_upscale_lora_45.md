---
name: unknown_workflow_upscale_latent_upscale_lora_45
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.866714
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2046078723471974401.json, 视频生成/图生视频/2033079847349653505.json, 视频生成/图生视频/2081705419873017857.json, 视频生成/图生视频/LTX2.3音画同步随机动作提示词版 图生视频_2082783625594105858.json, 视频生成/图生视频/2068601277344477186.json, 视频生成/图生视频/2052091652172468226.json, 视频生成/图生视频/2052083920916762625.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_45

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2046078723471974401.json、视频生成/图生视频/2033079847349653505.json、视频生成/图生视频/2081705419873017857.json、视频生成/图生视频/LTX2.3音画同步随机动作提示词版 图生视频_2082783625594105858.json、视频生成/图生视频/2068601277344477186.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 6/7 个有
- `KSampler` —— 6/7 个有
- `LTXVScheduler` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `TextGenerateLTX2Prompt` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `Text` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `Int` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `CR Text Replace` —— 2/7 个有
- `DF_Int_to_Float` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `MultiTextConcatenate` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `RH_Utils` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `DapaoImageAspectRatioResizeNode` —— 1/7 个有
- `HAIGC_LoadImagesFromZip` —— 1/7 个有
- `HAIGC_SaveImagesToZip` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `ManualSigmas` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PromptBatchQueue` —— 1/7 个有
- `RHBatchImages:` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 24 - 25 | 7 | 99% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，6 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
