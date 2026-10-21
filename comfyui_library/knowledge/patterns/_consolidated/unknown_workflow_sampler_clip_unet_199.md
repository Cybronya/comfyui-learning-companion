---
name: unknown_workflow_sampler_clip_unet_199
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.747
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, ImageConcatMulti, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image对比测试工作流_2068508638993534977.json, 图片生成/文生图/Z-image模型 与 Engineer v6 交叉对比-测试工作流_2065276186162458626.json, 图片生成/文生图/Z-turbo Engineer v6对比工作流_2064619941457907714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_199

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image对比测试工作流_2068508638993534977.json、图片生成/文生图/Z-image模型 与 Engineer v6 交叉对比-测试工作流_2065276186162458626.json、图片生成/文生图/Z-turbo Engineer v6对比工作流_2064619941457907714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `ImageConcatMulti`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ClipLoaderGGUF` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 3 | 65% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，3 个样本
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（8/3 个样本）：Steps较低可能导致细节不足
