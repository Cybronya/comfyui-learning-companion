---
name: unknown_workflow_video_sampler_clip_126
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7875
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DF_Int_to_Float, GetNode, INTConstant, Int, KSampler, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, ModelSamplingSD3, Primitive integer [Crystools], SetNode, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, Primitive integer [Crystools]]
members: [图片生成/文生图/文生视频极速版Wan2.2+Rapid_2021387179699740674.json, 视频生成/文生视频/1968649892224802818.json, 视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json, 视频生成/文生视频/极速多合一文生视频_2043517312220798978.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文生视频极速版Wan2.2+Rapid_2021387179699740674.json、视频生成/文生视频/1968649892224802818.json、视频生成/文生视频/文生视频极速版Wan2.2+多合一极速Rapid-AIO-Mega_2041755387250089986.json、视频生成/文生视频/极速多合一文生视频_2043517312220798978.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DF_Int_to_Float`
- `GetNode`
- `INTConstant`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `Primitive integer [Crystools]`
- `SetNode`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ipndm | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、MathExpression|pysssss、Primitive integer [Crystools]
