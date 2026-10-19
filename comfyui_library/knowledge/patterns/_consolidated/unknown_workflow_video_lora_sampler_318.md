---
name: unknown_workflow_video_lora_sampler_318
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.606571
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, DWPreprocessor, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1983610116006191105.json, 视频生成/图生视频/1975191732172230658.json, 视频生成/图生视频/1991499381406908418.json, 视频生成/图生视频/1973274759364521985.json, 视频生成/图生视频/1975411032183148546.json, 视频生成/图生视频/1988553294480064514.json, 视频生成/图生视频/2031979881122238466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_318

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1983610116006191105.json、视频生成/图生视频/1975191732172230658.json、视频生成/图生视频/1991499381406908418.json、视频生成/图生视频/1973274759364521985.json、视频生成/图生视频/1975411032183148546.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `DWPreprocessor`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PixelPerfectResolution` —— 6/7 个有
- `RHHiddenNodes` —— 6/7 个有
- `DrawMaskOnImage` —— 4/7 个有
- `FaceMaskFromPoseKeypoints` —— 4/7 个有
- `GrowMask` —— 4/7 个有
- `ImageCropByMaskAndResize` —— 4/7 个有
- `BlockifyMask` —— 3/7 个有
- `DownloadAndLoadSAM2Model` —— 3/7 个有
- `PointsEditor` —— 3/7 个有
- `Sam2Segmentation` —— 3/7 个有
- `CR Text` —— 1/7 个有
- `ImageAndMaskPreview` —— 1/7 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/7 个有
- `LayerMask: SegformerClothesPipelineLoader` —— 1/7 个有
- `LayerMask: SegformerUltraV2` —— 1/7 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（21/7 个样本）：Steps较低可能导致细节不足
