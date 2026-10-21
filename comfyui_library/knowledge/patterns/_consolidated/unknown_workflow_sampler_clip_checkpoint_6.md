---
name: unknown_workflow_sampler_clip_checkpoint_6
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.862
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/sd3.5_simple_example.json, 图片生成/文生图/02.Lumina_Image_2.0_中文_1991131395038773250.json, 图片生成/文生图/11111_1943236511586271234.json, 图片生成/文生图/1905175007570350082.json, 图片生成/文生图/1930157809210441730.json, 图片生成/文生图/1930158858272980993.json, 图片生成/文生图/1930264243235405826.json, 图片生成/文生图/1951277492470493185.json, 图片生成/文生图/简单易用的 FP8 版本_1898159424081448962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（comfyui-workflow-templates-json/sd3.5_simple_example.json、图片生成/文生图/02.Lumina_Image_2.0_中文_1991131395038773250.json、图片生成/文生图/11111_1943236511586271234.json、图片生成/文生图/1905175007570350082.json、图片生成/文生图/1930157809210441730.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 4/9 个有
- `FluxGuidance` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `Bjornulf_LatentResolutionSelector` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 9 | 69% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 9 | 39% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，9 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
