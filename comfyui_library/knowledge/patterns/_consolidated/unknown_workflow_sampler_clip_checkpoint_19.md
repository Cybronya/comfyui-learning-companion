---
name: unknown_workflow_sampler_clip_checkpoint_19
type: Unknown Workflow
frequency: 5
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/sim▶Wan2.2-AllInOne-V10-【文生图】_1965952460185579522.json, 视频生成/图生视频/AIO-V10大一统文生视频-Wan2.2_1950720538975096834.json, 视频生成/文生视频/rapid-aio一个模型搞定文生视频_1955156862251536386.json, 视频生成/文生视频/▶Wan2.2-AllInOne-V10文生视频超快速工作流【好奇漫步】_1970121357323366402.json, 视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/sim▶Wan2.2-AllInOne-V10-【文生图】_1965952460185579522.json、视频生成/图生视频/AIO-V10大一统文生视频-Wan2.2_1950720538975096834.json、视频生成/文生视频/rapid-aio一个模型搞定文生视频_1955156862251536386.json、视频生成/文生视频/▶Wan2.2-AllInOne-V10文生视频超快速工作流【好奇漫步】_1970121357323366402.json、视频生成/文生视频/文生视频Wan2.2 - T2V-rapid-aio AI 文生视频_2009171871626960898.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 60% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
