---
name: unknown_workflow_sampler_unet_vae_279
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.5
common_nodes: [Anything Everywhere3, GetNode, Image Comparer (rgthree), ImageBlur, Int, JoinImageWithAlpha, KSampler, LoadImage, ResizeImageMaskNode, SaveImage, SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, SetNode, SplitImageWithAlpha, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, 孤海注释]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/SeedVR2_疾速放大_2098667368678510593.json, 图片生成/图生图/SeedVR2_疾速放大_2099329585614774274.json, 图片生成/图生图/SeedVR2_疾速放大_2099667442590113793.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_279

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SeedVR2_疾速放大_2098667368678510593.json、图片生成/图生图/SeedVR2_疾速放大_2099329585614774274.json、图片生成/图生图/SeedVR2_疾速放大_2099667442590113793.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageBlur`
- `Int`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadImage`
- `ResizeImageMaskNode`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SetNode`
- `SplitImageWithAlpha`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
