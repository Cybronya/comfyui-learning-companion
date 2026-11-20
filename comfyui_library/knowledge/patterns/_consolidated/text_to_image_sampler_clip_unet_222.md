---
name: text_to_image_sampler_clip_unet_222
type: Text To Image
frequency: 3
level: moderate
coverage: 0.882667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Redux参考生图_1974749882097471489.json, 平台全量/flux可调参数风格融图_1953788293831905282.json, 平台全量/flux风格融图_1936713642945466369.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_222

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Redux参考生图_1974749882097471489.json、平台全量/flux可调参数风格融图_1953788293831905282.json、平台全量/flux风格融图_1936713642945466369.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `FluxResolutionNode` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `RH_Prompter` —— 1/3 个有
- `ReduxAdvanced` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `StyleModelAdvancedApply` —— 1/3 个有
- `StyleModelApply` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 25 | 3 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 864 | 512 - 968 | 3 | 75% |
| 高度 | 1152 | 512 - 1280 | 3 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 25，3 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 864，观测区间 512 - 968，3 个样本
- 高度 中位数 1152，观测区间 512 - 1280，3 个样本
