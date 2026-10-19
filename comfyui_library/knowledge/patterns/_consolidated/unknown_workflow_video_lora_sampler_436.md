---
name: unknown_workflow_video_lora_sampler_436
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9306
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJ, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, String Literal, TrimVideoLatent, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ, easy int]
problems: []
missing: [String Literal, easy int, Image Blank, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM V2, GetImageSize+, easy seed]
members: [视频生成/图生视频/1950455319556218882.json, 视频生成/图生视频/1950519561194033153.json, 视频生成/文生视频/1950435330224775169.json, 视频生成/文生视频/1950526542499729410.json, 视频生成/文生视频/Wan2.2-VACE-文生视频_2072999663609094144.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_436

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1950455319556218882.json、视频生成/图生视频/1950519561194033153.json、视频生成/文生视频/1950435330224775169.json、视频生成/文生视频/1950526542499729410.json、视频生成/文生视频/Wan2.2-VACE-文生视频_2072999663609094144.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJ`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `String Literal`
- `TrimVideoLatent`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 4/5 个有
- `easy seed` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `Image Blank` —— 3/5 个有
- `ImageCompositeMasked` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `LayerMask: LoadFlorence2Model` —— 3/5 个有
- `LayerMask: ObjectDetectorFL2` —— 3/5 个有
- `LayerMask: SAM2Ultra` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `GetImageSize+` —— 2/5 个有
- `GrowMaskWithBlur` —— 2/5 个有
- `ImagePadKJ` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `InpaintPreprocessor` —— 2/5 个有
- `JWImageExtractFromBatch` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 100% |
| 重绘幅度 | beta | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 100%
- 重绘幅度 最常用 beta，5 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy int、Image Blank、LayerMask: LoadFlorence2Model、LayerMask: ObjectDetectorFL2
