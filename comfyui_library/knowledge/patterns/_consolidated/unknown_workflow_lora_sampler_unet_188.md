---
name: unknown_workflow_lora_sampler_unet_188
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8265
common_nodes: [CFGNorm, CLIPLoader, DownloadAndLoadFlorence2Model, EmptySD3LatentImage, Florence2Run, KSampler, LoadImage, LoraLoader, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy imageRemBg, easy saveText]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/印花提取并反推抠图一体化(带抠图开关)_2048300194034356226.json, 图片生成/图生图/印花提取并反推抠图一体化(开关2)_2048316730962874370.json, 图片生成/图生图/印花提取并反推抠图一体化_2048275866085494785.json, 图片生成/图生图/印花提取并反推抠图内部使用_加速版(05-03)_2050941344520122370.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_188

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/印花提取并反推抠图一体化(带抠图开关)_2048300194034356226.json、图片生成/图生图/印花提取并反推抠图一体化(开关2)_2048316730962874370.json、图片生成/图生图/印花提取并反推抠图一体化_2048275866085494785.json、图片生成/图生图/印花提取并反推抠图内部使用_加速版(05-03)_2050941344520122370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `DownloadAndLoadFlorence2Model`
- `EmptySD3LatentImage`
- `Florence2Run`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageRemBg`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImpactSwitch` —— 2/4 个有
- `ImpactInversedSwitch` —— 1/4 个有
- `Int Input [DVB]` —— 1/4 个有
- `Int Input [Dream]` —— 1/4 个有
- `TwoWaySwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
