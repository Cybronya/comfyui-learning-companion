---
name: unknown_workflow_sampler_clip_unet_61
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.932778
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Fans Prompt Styler Negative]
members: [图片生成/文生图/1951256026077188097.json, 图片生成/文生图/1951281909651419137.json, 图片生成/文生图/1951839776326537218.json, 图片生成/文生图/1951967199781179393.json, 图片生成/文生图/1952021213906415618.json, 图片生成/文生图/1954159231169642497.json, 图片生成/文生图/1959107680914845697.json, 图片生成/文生图/FLUX Krea文生图，低“AI味”，真实感_1991804904345907201.json, 图片生成/文生图/flux1_dev文生图_2059177447408627714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_61

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1951256026077188097.json、图片生成/文生图/1951281909651419137.json、图片生成/文生图/1951839776326537218.json、图片生成/文生图/1951967199781179393.json、图片生成/文生图/1952021213906415618.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/9 个有
- `Fans Prompt Styler Negative` —— 1/9 个有
- `FluxKontextImageScale` —— 1/9 个有
- `HYPIRImageRestoration` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 9 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Fans Prompt Styler Negative
