---
name: unknown_workflow_sampler_checkpoint_vae_30
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.931
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Rapid-AIO_2005268893805543426.json, 图片生成/文生图/Qwen-image-2509-v3 文生图 图生图 图像编辑all-in-one_1976881433581178881.json, 图片生成/文生图/aio v11工作流（平替nano 全能图片V1 pro）_1993982116488822786.json, 图片生成/文生图/myV4-Qwen-Rapid-AIO 4-10步采样 改图神器_1978426223942635521.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-Rapid-AIO_2005268893805543426.json、图片生成/文生图/Qwen-image-2509-v3 文生图 图生图 图像编辑all-in-one_1976881433581178881.json、图片生成/文生图/aio v11工作流（平替nano 全能图片V1 pro）_1993982116488822786.json、图片生成/文生图/myV4-Qwen-Rapid-AIO 4-10步采样 改图神器_1978426223942635521.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerColor: Brightness & Contrast` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 75% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 744 | 720 - 1024 | 4 | 84% |
| 高度 | 1280 | 1024 - 1344 | 4 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 744，观测区间 720 - 1024，4 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1024 - 1344，4 个样本，取值集中（一致性 90%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
