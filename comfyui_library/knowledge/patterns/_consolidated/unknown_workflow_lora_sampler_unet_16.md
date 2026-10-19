---
name: unknown_workflow_lora_sampler_unet_16
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.974857
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1988774900942909442.json, 图片生成/文生图/1988927261430648834.json, 图片生成/文生图/1989171870014517249.json, 图片生成/文生图/1989311154684129281.json, 图片生成/文生图/1989695013087047682.json, 视频生成/图生视频/1982020667237384193.json, 视频生成/图生视频/1961983511181856769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1988774900942909442.json、图片生成/文生图/1988927261430648834.json、图片生成/文生图/1989171870014517249.json、图片生成/文生图/1989311154684129281.json、图片生成/文生图/1989695013087047682.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 6/7 个有
- `LoadImage` —— 2/7 个有
- `TextEncodeQwenImageEdit` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1280 | 7 | 89% |
| 高度 | 1024 | 720 - 1280 | 7 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1280，7 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 720 - 1280，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
