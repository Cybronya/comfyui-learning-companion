---
name: unknown_workflow_sampler_checkpoint_vae_34
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.952667
common_nodes: [CR Text, CR Text Concatenate, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506.json, 图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369.json, 图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 双图版 色彩调整+无位移版_1979058598452039681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506.json、图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 单图版 色彩调整+无位移版_1979054101726138369.json、图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V4 双图版 色彩调整+无位移版_1979058598452039681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
