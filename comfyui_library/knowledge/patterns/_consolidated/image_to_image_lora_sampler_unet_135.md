---
name: image_to_image_lora_sampler_unet_135
type: Image To Image
frequency: 5
level: strong
coverage: 0.9302
common_nodes: [CFGNorm, CLIPLoader, Get Image Size, ImageScale, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, crop, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/前置判断+图片处理_2042070492542144514.json, 图片生成/图生图/横向-4张处理_2034900727230898178.json, 图片生成/图生图/横向-4张处理_2039340323746353153.json, 图片生成/图生图/竖版-4张处理_2034826289911173122.json, 图片生成/图生图/竖版-4张处理_2039318003090726913.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/前置判断+图片处理_2042070492542144514.json、图片生成/图生图/横向-4张处理_2034900727230898178.json、图片生成/图生图/横向-4张处理_2039340323746353153.json、图片生成/图生图/竖版-4张处理_2034826289911173122.json、图片生成/图生图/竖版-4张处理_2039318003090726913.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Get Image Size`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `crop`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `PadImageToCanvas` —— 4/5 个有
- `MaskToImage` —— 3/5 个有
- `Preview from image [Crystools]` —— 3/5 个有
- `Qwen3VL_Chat` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `ttN text` —— 3/5 个有
- `ImpactCompare` —— 1/5 个有
- `ImpactImageInfo` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `kkPadImageToCanvas` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（18/5 个样本）：Steps较低可能导致细节不足
