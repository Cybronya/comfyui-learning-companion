---
name: unknown_workflow_video_sampler_clip_194
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.758
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/aio_v9图生视频_2039317134282592258.json, 视频生成/图生视频/【首尾帧+图生视频+文生视频】Wan2.2万相视频rapid mega aio综合工作流_1972197412775391234.json, 视频生成/文生视频/05基础版本+图生视频+全节点注释_2055549946513903617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/aio_v9图生视频_2039317134282592258.json、视频生成/图生视频/【首尾帧+图生视频+文生视频】Wan2.2万相视频rapid mega aio综合工作流_1972197412775391234.json、视频生成/文生视频/05基础版本+图生视频+全节点注释_2055549946513903617.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `wanBlockSwap` —— 2/3 个有
- `EmptyHunyuanLatentVideo` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `WanVaceToVideo` —— 1/3 个有
- `WanVideoVACEStartToEndFrame` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
