---
name: image_to_image_lora_sampler_unet_12
type: Image To Image
frequency: 4
level: weak
coverage: 0.90875
common_nodes: [CLIPLoader, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Image Rembg (Remove Background)]
members: [视频生成/图生视频/2030684351255547905.json, 视频生成/图生视频/2030672844018946049.json, 视频生成/文生视频/1970490655065710594.json, 视频生成/文生视频/Qwen Image Edit Plus的单图双图三图参考_2072999556276854784.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2030684351255547905.json、视频生成/图生视频/2030672844018946049.json、视频生成/文生视频/1970490655065710594.json、视频生成/文生视频/Qwen Image Edit Plus的单图双图三图参考_2072999556276854784.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `DWPreprocessor` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `Image Rembg (Remove Background)` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `TTP_Expand_And_Mask` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | 8 - 50 | 4 | 28% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，观测区间 8 - 50，4 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Image Rembg (Remove Background)
