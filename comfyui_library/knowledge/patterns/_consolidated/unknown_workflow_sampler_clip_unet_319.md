---
name: unknown_workflow_sampler_clip_unet_319
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.83675
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/文生图/LLM+Z-Image文生图放大工作流,彻底解放Z-Image_1993901432334123010.json", 图片生成/文生图/Qwen-Image千问图像｜文生图全尺寸_1953390443667095554.json, 图片生成/文生图/qwen image 文生图，海报设计，文本效果好_1953351554604695553.json, 视频生成/图生视频/自己用：Qwen-Image +Lora_1955581722751483906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_319

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/LLM+Z-Image文生图放大工作流,彻底解放Z-Image_1993901432334123010.json、图片生成/文生图/Qwen-Image千问图像｜文生图全尺寸_1953390443667095554.json、图片生成/文生图/qwen image 文生图，海报设计，文本效果好_1953351554604695553.json、视频生成/图生视频/自己用：Qwen-Image +Lora_1955581722751483906.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `easy showAnything` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SeedVR2GGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 40 | 4 | 48% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 58% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 40，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
