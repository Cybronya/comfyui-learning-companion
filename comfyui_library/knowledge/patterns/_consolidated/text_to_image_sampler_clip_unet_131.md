---
name: text_to_image_sampler_clip_unet_131
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9516
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json, 图片生成/文生图/Z-image turbo基础生图工作流_2028382510350082049.json, 图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json, 图片生成/文生图/▶▷Krea2-极清生图流_2112007776892440578.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-Image VS Z-Image-turbo VS Qwen image 2512_2016491036381552641.json、图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json、图片生成/文生图/Z-image turbo基础生图工作流_2028382510350082049.json、图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json、图片生成/文生图/▶▷Krea2-极清生图流_2112007776892440578.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `easy promptList` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 760 - 1080 | 5 | 88% |
| 高度 | 1280 | 1024 - 1920 | 5 | 75% |
| 采样步数 | 7 | 4 - 9 | 4 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.54 - 1 | 4 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 760 - 1080，5 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 7，观测区间 4 - 9，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.54 - 1，4 个样本
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
