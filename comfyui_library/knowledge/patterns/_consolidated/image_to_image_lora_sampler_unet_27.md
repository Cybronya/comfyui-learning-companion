---
name: image_to_image_lora_sampler_unet_27
type: Image To Image
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/qwen2511图转速手绘线条水彩风格_2088151301396975617.json, 视频生成/文生视频/真人转动漫++真人转卡通++真人转漫画++ (1)_2061990337312280578.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/qwen2511图转速手绘线条水彩风格_2088151301396975617.json、视频生成/文生视频/真人转动漫++真人转卡通++真人转漫画++ (1)_2061990337312280578.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
