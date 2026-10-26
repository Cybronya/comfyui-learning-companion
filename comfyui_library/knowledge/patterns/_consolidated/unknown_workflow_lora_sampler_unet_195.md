---
name: unknown_workflow_lora_sampler_unet_195
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9875
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多图生图运行工作流_2084273933980884993.json, 图片生成/图生图/多图生图运行工作流_2091809550411321346.json, 图片生成/文生图/人物三视图-高一致性_2062129476934389761.json, 数字人/数字人/免费 开源 2511 角色设计+数字人 三视图真人动漫人物一致性_2101744942149357570.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_195

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/多图生图运行工作流_2084273933980884993.json、图片生成/图生图/多图生图运行工作流_2091809550411321346.json、图片生成/文生图/人物三视图-高一致性_2062129476934389761.json、数字人/数字人/免费 开源 2511 角色设计+数字人 三视图真人动漫人物一致性_2101744942149357570.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `LatentUpscaleBy` —— 2/4 个有
- `SDXL Empty Latent Image` —— 2/4 个有
- `SDXL Empty Latent Image (rgthree)` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 4 - 5 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 4 - 5，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
