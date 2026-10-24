---
name: unknown_workflow_lora_sampler_unet_177
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.9155
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwenedit2509女生专属自然轻修自动修图_1971135506622881794.json, 图片生成/图生图/qwen-image 2511 单_双图编辑（换姿态、换背景）_2084887960415199234.json, 图片生成/图生图/千问2509风格迁移_1985993103351980033.json, 图片生成/图生图/水墨化风格转换工作流_1976563380859346945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwenedit2509女生专属自然轻修自动修图_1971135506622881794.json、图片生成/图生图/qwen-image 2511 单_双图编辑（换姿态、换背景）_2084887960415199234.json、图片生成/图生图/千问2509风格迁移_1985993103351980033.json、图片生成/图生图/水墨化风格转换工作流_1976563380859346945.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 3/4 个有
- `ImageGetSize` —— 3/4 个有
- `Text` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `CFGNorm` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `ImageRGBToYUV` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `TextEncodeQwenImageEditPlusAdv` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 12 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 1360 | 4 | 49% |
| 高度 | 512 | 512 - 1920 | 4 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 12，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1360，4 个样本，取值分散，一致性仅 49%
- 高度 中位数 512，观测区间 512 - 1920，4 个样本，取值分散，一致性仅 29%
