---
name: unknown_workflow_sampler_checkpoint_vae_44
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.834333
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, ImageConcanate, KSampler, LoadImage, RH_LLMAPI_NODE, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多图融合编辑模型-Qwen-Rapid-AIO-v3_1981566069116682241.json, "平台全量/QWEN Image Edit 2509 Rapid AIO-V11, 4步出图，多功能融合模型_1975846387965407233.json", 平台全量/Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_44

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多图融合编辑模型-Qwen-Rapid-AIO-v3_1981566069116682241.json、平台全量/QWEN Image Edit 2509 Rapid AIO-V11, 4步出图，多功能融合模型_1975846387965407233.json、平台全量/Qwen-Image-Edit-Rapid-AIO多图融合编辑工作流_1978013570380300290.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `GetImage` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 960 | 3 | 68% |
| 高度 | 512 | 512 - 1280 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 960，3 个样本
- 高度 中位数 512，观测区间 512 - 1280，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
