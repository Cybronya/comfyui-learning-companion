---
name: unknown_workflow_video_sampler_clip_102
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.820667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, Primitive integer [Crystools]]
members: [视频生成/图生视频/1970828010674888705.json, 视频生成/图生视频/1969960068689108994.json, 视频生成/图生视频/1977754220172562434.json, 视频生成/文生视频/1968649892224802818.json, 视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json, 视频生成/文生视频/极速多合一文生视频_2043517312220798978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1970828010674888705.json、视频生成/图生视频/1969960068689108994.json、视频生成/图生视频/1977754220172562434.json、视频生成/文生视频/1968649892224802818.json、视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `DF_Int_to_Float` —— 4/6 个有
- `Int` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `Primitive integer [Crystools]` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `LayerUtility: PurgeVRAM V2` —— 3/6 个有
- `LoadImage` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `WanVideoVACEStartToEndFrame` —— 3/6 个有
- `PrimitiveInt` —— 2/6 个有
- `ImageResizeKJ` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | ipndm | - | 6 | 83% |
| 调度器 | sgm_uniform | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，6 个样本，一致性 83%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、MathExpression|pysssss、Primitive integer [Crystools]
