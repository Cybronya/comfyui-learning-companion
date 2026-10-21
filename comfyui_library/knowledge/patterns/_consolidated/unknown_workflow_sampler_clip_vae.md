---
name: unknown_workflow_sampler_clip_vae
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.9328
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy hiresFix]
members: [图片生成/文生图/06.Z-Image-T-Lora文生图-NF_1996576652488491010.json, 图片生成/文生图/1953057914565103617.json, 图片生成/文生图/1953059659532988418.json, 图片生成/文生图/1953087441538322434.json, 图片生成/文生图/1953143788371906562.json, 图片生成/文生图/1953252280764141569.json, 图片生成/文生图/1953287044091023361.json, 图片生成/文生图/1953691322731429889.json, 图片生成/文生图/1953699331356459009.json, 图片生成/文生图/1953710081516994562.json, 图片生成/文生图/1954172979645181954.json, 图片生成/文生图/56.tonnie-zimage文生图_1993951157917777921.json, 图片生成/文生图/Z Image 小强模型极速出图_1993947409080401922.json, 图片生成/文生图/Z-Image 文生图_2016054204908965889.json, 图片生成/文生图/Z-Image 最强文生图，30秒出图，超高性价比_2011687215461572609.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/06.Z-Image-T-Lora文生图-NF_1996576652488491010.json、图片生成/文生图/1953057914565103617.json、图片生成/文生图/1953059659532988418.json、图片生成/文生图/1953087441538322434.json、图片生成/文生图/1953143788371906562.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 14/15 个有
- `UNETLoader` —— 13/15 个有
- `PathchSageAttentionKJ` —— 7/15 个有
- `Text` —— 4/15 个有
- `ConditioningZeroOut` —— 3/15 个有
- `PreviewImage` —— 3/15 个有
- `UnetLoaderGGUF` —— 2/15 个有
- `ClipLoaderGGUF` —— 1/15 个有
- `Int` —— 1/15 个有
- `Lora Loader Stack (rgthree)` —— 1/15 个有
- `easy hiresFix` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 20 | 15 | 69% |
| Prompt 约束强度(CFG) | 2 | 1 - 4 | 15 | 46% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 4，15 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy hiresFix
