---
name: unknown_workflow_upscale_latent_upscale_lora_42
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.885429
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2046078723471974401.json, 视频生成/图生视频/2033079847349653505.json, 视频生成/图生视频/2081705419873017857.json, 视频生成/图生视频/LTX2.3高质量图生视频_2083082295870840833.json, 视频生成/图生视频/2053382276368609281.json, 视频生成/图生视频/2052311443516739586.json, 视频生成/文生视频/CG少女风格文生视频_图生视频2合1自由切换版-LTX2.3_2038339473397784578.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2046078723471974401.json、视频生成/图生视频/2033079847349653505.json、视频生成/图生视频/2081705419873017857.json、视频生成/图生视频/LTX2.3高质量图生视频_2083082295870840833.json、视频生成/图生视频/2053382276368609281.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/7 个有
- `KSampler` —— 6/7 个有
- `LTXVScheduler` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `DualCLIPLoader` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `PreviewAny` —— 4/7 个有
- `TextGenerateLTX2Prompt` —— 4/7 个有
- `easy showAnything` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `ManualSigmas` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `PrimitiveBoolean` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `BasicScheduler` —— 1/7 个有
- `DapaoImageAspectRatioResizeNode` —— 1/7 个有
- `HAIGC_LoadImagesFromZip` —— 1/7 个有
- `HAIGC_SaveImagesToZip` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `Int` —— 1/7 个有
- `LTX2SamplingPreviewOverride` —— 1/7 个有
- `LTX2_NAG` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PromptBatchQueue` —— 1/7 个有
- `RHBatchImages:` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Text` —— 1/7 个有
- `easy ifElse` —— 1/7 个有
- `easy positive` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 24 - 25 | 7 | 99% |
| 采样步数 | 4 | 4 - 6 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.4 | 6 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 99%）
- 采样步数 中位数 4，观测区间 4 - 6，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.4，6 个样本，取值集中（一致性 95%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
