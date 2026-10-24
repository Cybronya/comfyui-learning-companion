---
name: unknown_workflow_lora_sampler_unet_180
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.77975
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen image edit 2509_1987811007693262850.json, 图片生成/图生图/qwen2511双图融合_2011333778131656706.json, 图片生成/图生图/保留衣服细节+自然融入环境=完美换装_2035311130079404034.json, 图片生成/图生图/完美换装工作流：衣服细节保留+和谐融入环境_1989633039712088066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_180

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen image edit 2509_1987811007693262850.json、图片生成/图生图/qwen2511双图融合_2011333778131656706.json、图片生成/图生图/保留衣服细节+自然融入环境=完美换装_2035311130079404034.json、图片生成/图生图/完美换装工作流：衣服细节保留+和谐融入环境_1989633039712088066.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `TextEncodeQwenImageEdit` —— 2/4 个有
- `ImpactInt` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1196 | 1024 - 1536 | 4 | 82% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1196，观测区间 1024 - 1536，4 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
