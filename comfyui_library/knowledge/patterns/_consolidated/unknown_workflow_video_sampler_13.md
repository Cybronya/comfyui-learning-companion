---
name: unknown_workflow_video_sampler_13
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.877333
common_nodes: [CreateVideo, DiffuEraserLoader, DiffuEraserSampler, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetVideoComponents, ImageConcanate, ImageFromBatch+, ImageResizeKJv2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, MathExpression|pysssss, PreviewImage, RepeatImageBatch, SaveImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2045784226385104897.json, 视频生成/图生视频/2043949321623707650.json, 视频生成/图生视频/2020315533945606146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2045784226385104897.json、视频生成/图生视频/2043949321623707650.json、视频生成/图生视频/2020315533945606146.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateVideo`
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RepeatImageBatch`
- `SaveImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RunningHub Deepcleaner` —— 1/3 个有
- `SaveVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.75759e+09 | 9.13115e+08 - 1.84687e+09 | 3 | 72% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.75759e+09，观测区间 9.13115e+08 - 1.84687e+09，3 个样本
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.84687e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
