---
name: unknown_workflow_video_lora_sampler_369
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.605333
common_nodes: [AV_VAELoader, BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, Display Int (rgthree), DownloadAndLoadGIMMVFIModel, DownloadAndLoadSAM2Model, DrawMaskOnImage, EmptyImage, GIMMVFI_interpolate, GetNode, GrowMask, INTConstant, ImageBatch, ImageFromBatch, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, OnnxDetectionModelLoader, PixelPerfectResolution, PointsEditor, PoseDetectionOneToAllAnimation, Sam2Segmentation, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1999382397340839937.json, 视频生成/图生视频/2042618078990704642.json, 视频生成/图生视频/2057269921096232961.json, 视频生成/图生视频/2059070496771239938.json, 视频生成/图生视频/2039883987727949826.json, 视频生成/图生视频/1998717600895000577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_369

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1999382397340839937.json、视频生成/图生视频/2042618078990704642.json、视频生成/图生视频/2057269921096232961.json、视频生成/图生视频/2059070496771239938.json、视频生成/图生视频/2039883987727949826.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 6 个 workflow 都包含：
- `AV_VAELoader`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `Display Int (rgthree)`
- `DownloadAndLoadGIMMVFIModel`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `EmptyImage`
- `GIMMVFI_interpolate`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `PointsEditor`
- `PoseDetectionOneToAllAnimation`
- `Sam2Segmentation`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `DF_Float` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（18/6 个样本）：Steps较低可能导致细节不足
