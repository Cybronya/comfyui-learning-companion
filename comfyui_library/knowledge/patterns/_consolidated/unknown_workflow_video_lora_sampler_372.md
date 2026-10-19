---
name: unknown_workflow_video_lora_sampler_372
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.451167
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, GetNode, GrowMask, ImageBatch, ImageFromBatch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, PreviewImage, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: [easy forLoopEnd, easy forLoopStart, SimpleMath+]
members: [视频生成/图生视频/1976471239042666497.json, 视频生成/图生视频/1973951383147819010.json, 视频生成/文生视频/1971749907403108354.json, 视频生成/文生视频/1975828769351012354.json, 视频生成/文生视频/Wan-Animate原生无限流（修正）_2072999547389124608.json, 视频生成/文生视频/角色参考-原生无限流-补帧_2072999523758415872.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_372

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1976471239042666497.json、视频生成/图生视频/1973951383147819010.json、视频生成/文生视频/1971749907403108354.json、视频生成/文生视频/1975828769351012354.json、视频生成/文生视频/Wan-Animate原生无限流（修正）_2072999547389124608.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：45%

## 共有节点

全部 6 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageBatch`
- `ImageFromBatch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `PreviewImage`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 4/6 个有
- `Float` —— 4/6 个有
- `GetImageSizeAndCount` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `Int` —— 4/6 个有
- `MaskPreview` —— 4/6 个有
- `PointsEditor` —— 4/6 个有
- `Sam2Segmentation` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `AILab_MaskPreview` —— 2/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/6 个有
- `GIMMVFI_interpolate` —— 2/6 个有
- `ImageScale` —— 2/6 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/6 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/6 个有
- `Setter` —— 2/6 个有
- `VHS_VideoInfo` —— 2/6 个有
- `easy showAnything` —— 2/6 个有

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
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy forLoopEnd、easy forLoopStart、SimpleMath+
