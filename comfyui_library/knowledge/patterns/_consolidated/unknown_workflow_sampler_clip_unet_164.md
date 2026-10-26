---
name: unknown_workflow_sampler_clip_unet_164
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.820375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX2-klein 文生图4b_2012349235420729345.json, 图片生成/文生图/FLUX2-klein 文生图9b_2012344744420052994.json, 图片生成/文生图/Klein文生图+全节点注释_2072566661164658689.json, 图片生成/文生图/Klein文生图_2014600663744913409.json, 图片生成/文生图/Klein文生图_2072558936527560706.json, 图片生成/文生图/Klein文生图_2073934557337964546.json, 图片生成/文生图/【1月】高质量2K文生图 Flux2-Klein-9B_2012159064800763905.json, 视频生成/图生视频/Klein文生图+全节点注释_2072926956559097858.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_164

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/FLUX2-klein 文生图4b_2012349235420729345.json、图片生成/文生图/FLUX2-klein 文生图9b_2012344744420052994.json、图片生成/文生图/Klein文生图+全节点注释_2072566661164658689.json、图片生成/文生图/Klein文生图_2014600663744913409.json、图片生成/文生图/Klein文生图_2072558936527560706.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/8 个有
- `JWInteger` —— 6/8 个有
- `LoadImage` —— 5/8 个有
- `FluxResolutionNode` —— 2/8 个有
- `Int` —— 2/8 个有
- `Text` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
