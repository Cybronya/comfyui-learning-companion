---
name: unknown_workflow_sampler_clip_vae_61
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [EasyFunction_Lite, EmptyLatentImage, LoadImage, SaveImage, StoryDiffusion_Apply, StoryDiffusion_CLIPTextEncode, StoryDiffusion_KSampler, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306.json, 图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json, 图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/DreamO-StoryDiffusion单_双人分镜制作V1_1925885915884130306.json、图片生成/文生图/StoryDiffusion+DreamO单人物一致性_1926167931795771393.json、图片生成/文生图/StoryDiffusion+DreamO多人物一致性_1926146782307258370.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `EasyFunction_Lite`
- `EmptyLatentImage`
- `LoadImage`
- `SaveImage`
- `StoryDiffusion_Apply`
- `StoryDiffusion_CLIPTextEncode`
- `StoryDiffusion_KSampler`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Image Batch` —— 1/3 个有
- `ImageBatch` —— 1/3 个有
- `JWInteger` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| 宽度 | 456 | 456 - 512 | 3 | 94% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 456，观测区间 456 - 512，3 个样本，取值集中（一致性 94%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
