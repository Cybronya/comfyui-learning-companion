---
name: unknown_workflow_video_sampler_clip_140
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.763
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningCombine, DWPreprocessor, EmptyImage, ImageBatch, ImageBatchMultiple+, ImageConcanate, ImageConcatFromBatch, ImageResize+, ImageResizeKJv2, KSampler, LoadImage, ModelSamplingSD3, PreviewImage, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanPhantomSubjectToVideo, WanVaceToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1964540735016062978.json, 视频生成/图生视频/1955104991481511937.json, 视频生成/图生视频/2051908128723218434.json, 视频生成/图生视频/1986477403138650114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1964540735016062978.json、视频生成/图生视频/1955104991481511937.json、视频生成/图生视频/2051908128723218434.json、视频生成/图生视频/1986477403138650114.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningCombine`
- `DWPreprocessor`
- `EmptyImage`
- `ImageBatch`
- `ImageBatchMultiple+`
- `ImageConcanate`
- `ImageConcatFromBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanPhantomSubjectToVideo`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V_Advanced` —— 2/4 个有
- `CR Text Replace` —— 2/4 个有
- `TextBox` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 12 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 12，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
