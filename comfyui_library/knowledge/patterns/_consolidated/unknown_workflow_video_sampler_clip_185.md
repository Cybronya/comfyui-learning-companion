---
name: unknown_workflow_video_sampler_clip_185
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.948667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, INTConstant, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1970170134423871490.json, 视频生成/图生视频/1972197412775391234.json, 视频生成/文生视频/1969276766730809345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1970170134423871490.json、视频生成/图生视频/1972197412775391234.json、视频生成/文生视频/1969276766730809345.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | ipndm | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
