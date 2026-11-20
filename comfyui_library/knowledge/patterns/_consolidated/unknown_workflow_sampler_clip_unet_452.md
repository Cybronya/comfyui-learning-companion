---
name: unknown_workflow_sampler_clip_unet_452
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.952667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/image_omnigen2_文生图_1939949487580160001.json, 图片生成/文生图/image_omnigen2_文生图_1943503078144286722.json, 图片生成/文生图/z-image-细节增强 (enable)_2093973176530329601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_452

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/image_omnigen2_文生图_1939949487580160001.json、图片生成/文生图/image_omnigen2_文生图_1943503078144286722.json、图片生成/文生图/z-image-细节增强 (enable)_2093973176530329601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCFGGuider` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DetailDaemonSamplerNode` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1.4 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.86 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
