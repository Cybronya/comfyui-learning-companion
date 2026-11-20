---
name: unknown_workflow_sampler_unet_vae_182
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.958333
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/danotebook-qwen-image-edit-2511_2062476056275279873.json, 图片生成/图生图/图生图_2057815724835565569.json, 图片生成/图生图/小红书二图编辑(适用换装)_2034643139293618177.json, 图片生成/图生图/服装提取-上下_2038138778417635330.json, 图片生成/图生图/服装提取-前后上下_2038448443059871745.json, 图片生成/文生图/Qwen Edit 2509新旅游飞机_1991073540537524226.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_182

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/danotebook-qwen-image-edit-2511_2062476056275279873.json、图片生成/图生图/图生图_2057815724835565569.json、图片生成/图生图/小红书二图编辑(适用换装)_2034643139293618177.json、图片生成/图生图/服装提取-上下_2038138778417635330.json、图片生成/图生图/服装提取-前后上下_2038448443059871745.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `GetImage` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `StringCompare` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1280 | 6 | 77% |
| 高度 | 1024 | 512 - 1352 | 6 | 72% |
| 采样步数 | 8 | 4 - 8 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1280，6 个样本
- 高度 中位数 1024，观测区间 512 - 1352，6 个样本
- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
