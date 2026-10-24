---
name: unknown_workflow_video_lora_sampler_623
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.822333
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, DWPreprocessor, DrawMaskOnImage, GetImageRangeFromBatch, KSampler, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/SAM3+ANIMATE_1992216241626566658.json, 视频生成/图生视频/wan2.2+SAM3+ANIMATE模仿任意视频跳舞工作流_1992282953344503810.json, 视频生成/图生视频/动作迁移3多人选择一人替换（点编辑器）_2028161116790071297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_623

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/SAM3+ANIMATE_1992216241626566658.json、视频生成/图生视频/wan2.2+SAM3+ANIMATE模仿任意视频跳舞工作流_1992282953344503810.json、视频生成/图生视频/动作迁移3多人选择一人替换（点编辑器）_2028161116790071297.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `GetImageRangeFromBatch`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ACE_TextGoogleTranslate` —— 2/3 个有
- `ImageUpscaleWithModelBatched` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `ImpactImageBatchToImageList` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoadSAM3Model` —— 1/3 个有
- `MaskListToMaskBatch` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `PointsEditor` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SAM3Segmentation` —— 1/3 个有
- `SeCModelLoader` —— 1/3 个有
- `SeCVideoSegmentation` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy sam3ModelLoader` —— 1/3 个有
- `easy sam3VideoSegmentation` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
