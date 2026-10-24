---
name: unknown_workflow_sampler_checkpoint_vae_21
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9568
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王024.自动分镜-本地反推模型_2034916136629837825.json, 图片生成/图生图/Mymang-Qwen 2509 AIO 图像编辑_1977364306721415170.json, 图片生成/图生图/Qwen3VL+Next Scene分镜图_2053111296182239233.json, 图片生成/图生图/公众号嘉宾嘉宾推荐美化_2056989501834223617.json, 图片生成/文生图/支持24分镜图一次性生成   Edit Next Scene（自动分镜）_2041498219431071745.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王024.自动分镜-本地反推模型_2034916136629837825.json、图片生成/图生图/Mymang-Qwen 2509 AIO 图像编辑_1977364306721415170.json、图片生成/图生图/Qwen3VL+Next Scene分镜图_2053111296182239233.json、图片生成/图生图/公众号嘉宾嘉宾推荐美化_2056989501834223617.json、图片生成/文生图/支持24分镜图一次性生成   Edit Next Scene（自动分镜）_2041498219431071745.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/5 个有
- `easy promptLine` —— 3/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LoraLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | sa_solver | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
