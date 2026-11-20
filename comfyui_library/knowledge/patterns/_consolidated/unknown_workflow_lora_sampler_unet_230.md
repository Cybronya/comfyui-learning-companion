---
name: unknown_workflow_lora_sampler_unet_230
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.89575
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen局部重绘_2001118892187676674.json, 平台全量/2511 线稿出图（角度自适应）_2013102338214469634.json, 平台全量/多角度打光 _ Qwen-Image-Edit-2509_1901653481667895297.json, 平台全量/恢复曝光 _ Qwen-Image-Edit-2509_1890334410636435458.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_230

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen局部重绘_2001118892187676674.json、平台全量/2511 线稿出图（角度自适应）_2013102338214469634.json、平台全量/多角度打光 _ Qwen-Image-Edit-2509_1901653481667895297.json、平台全量/恢复曝光 _ Qwen-Image-Edit-2509_1890334410636435458.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenEditConfigPreparer` —— 3/4 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 3/4 个有
- `QwenEditAdaptiveLongestEdge` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/4 个有
- `ttN text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 4 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
