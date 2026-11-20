---
name: unknown_workflow_sampler_unet_vae_332
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.953667
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Q WEN 图片编辑丨一句话作图丨产品融合图片_1958693043136262145.json, 平台全量/QWEN-image-2511-1_1白底图生成_2079192562761551873.json, 平台全量/Qwen image2.1 姿势参考_2117439587156054018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_332

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Q WEN 图片编辑丨一句话作图丨产品融合图片_1958693043136262145.json、平台全量/QWEN-image-2511-1_1白底图生成_2079192562761551873.json、平台全量/Qwen image2.1 姿势参考_2117439587156054018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `QwenEditConfigPreparer` —— 2/3 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `Text` —— 1/3 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1024 | 512 - 1920 | 3 | 49% |
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1920，3 个样本，取值分散，一致性仅 49%
- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
