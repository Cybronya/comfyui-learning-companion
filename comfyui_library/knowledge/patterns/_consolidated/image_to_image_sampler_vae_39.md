---
name: image_to_image_sampler_vae_39
type: Image To Image
frequency: 3
level: strong
coverage: 0.986
common_nodes: [CFGNorm, CLIPLoader, GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, StringFunction|pysssss, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy positive, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【生产】艾小象故事山绘本生图工作流_2044676456759955457.json, 图片生成/文生图/艾小象故事山绘本生图工作流_2044358558413754370.json, 平台全量/生图-单图编辑-qwen-edit-2509-8步_1973059141738565633.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_39

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【生产】艾小象故事山绘本生图工作流_2044676456759955457.json、图片生成/文生图/艾小象故事山绘本生图工作流_2044358558413754370.json、平台全量/生图-单图编辑-qwen-edit-2509-8步_1973059141738565633.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `StringFunction|pysssss`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
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

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
