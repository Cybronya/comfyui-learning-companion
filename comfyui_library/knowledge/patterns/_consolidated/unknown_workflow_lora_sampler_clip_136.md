---
name: unknown_workflow_lora_sampler_clip_136
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.437
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetNode, GrowMask, ImageBatch, ImageFromBatch, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, PointsEditor, PrimitiveInt, Sam2Segmentation, SaveVideo, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2058456295702876162.json, 视频生成/图生视频/1971010678985265154.json, 视频生成/图生视频/1970998862133530625.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_136

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2058456295702876162.json、视频生成/图生视频/1971010678985265154.json、视频生成/图生视频/1970998862133530625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetNode`
- `GrowMask`
- `ImageBatch`
- `ImageFromBatch`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `PointsEditor`
- `PrimitiveInt`
- `Sam2Segmentation`
- `SaveVideo`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `MaskPreview` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ForLoopClose` —— 1/3 个有
- `ForLoopOpen` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResizeAdvanced` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `VHS_LoadVideoFFmpeg` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `VHS_VideoInfoLoaded` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
