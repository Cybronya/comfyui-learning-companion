---
name: unknown_workflow_sampler_clip_unet_118
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.885667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json, 图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json, 图片生成/文生图/Z-Image-Turbo 文生图 _ 9 节点极简模板_2086642662031060994.json, 图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json, 图片生成/文生图/Z-Image-Turbo基础文生图-工作流_2011542094619353089.json, 图片生成/文生图/Zimage base fp8一键出模特大片_2016314793744932866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z image 直出高清基础流 v1_2002028004870111233.json、图片生成/文生图/Z image 直出高清基础流 v2_2003053873344462850.json、图片生成/文生图/Z-Image-Turbo 文生图 _ 9 节点极简模板_2086642662031060994.json、图片生成/文生图/Z-Image-Turbo 文生图_2104866138722230274.json、图片生成/文生图/Z-Image-Turbo基础文生图-工作流_2011542094619353089.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `Text Multiline` —— 3/6 个有
- `CFGNorm` —— 2/6 个有
- `Display Any (rgthree)` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `QwenImageEngineer` —— 2/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 6 | 31% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，6 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
