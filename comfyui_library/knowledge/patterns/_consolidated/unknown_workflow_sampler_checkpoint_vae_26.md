---
name: unknown_workflow_sampler_checkpoint_vae_26
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8415
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2509-Rapid-AIO-V10 多功能融合模型_1988191921103355906.json, 图片生成/图生图/Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001.json, 图片生成/图生图/千问AIO-V5极速编辑图像双图版_1978309164088877058.json, 图片生成/图生图/千问编辑Rapid-AIO-V5融合模型极速出图_1977697617566203906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_26

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2509-Rapid-AIO-V10 多功能融合模型_1988191921103355906.json、图片生成/图生图/Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001.json、图片生成/图生图/千问AIO-V5极速编辑图像双图版_1978309164088877058.json、图片生成/图生图/千问编辑Rapid-AIO-V5融合模型极速出图_1977697617566203906.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

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
- `PreviewImage` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageScaleDownToSize` —— 1/4 个有
- `JjkText` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | sa_solver | - | 4 | 50% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 832 | 512 - 1024 | 4 | 77% |
| 高度 | 1136 | 512 - 1248 | 4 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，观测区间 512 - 1024，4 个样本
- 高度 中位数 1136，观测区间 512 - 1248，4 个样本
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
