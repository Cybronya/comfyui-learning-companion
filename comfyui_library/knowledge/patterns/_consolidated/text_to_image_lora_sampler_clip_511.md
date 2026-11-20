---
name: text_to_image_lora_sampler_clip_511
type: Text To Image
frequency: 3
level: strong
coverage: 0.762333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SaveImageKJ, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169.json, 图片生成/图生图/Qwen-多角度真人摄影一致性图生图_1989605255010766849.json, 数字人/数字人/Dataset gen - QWEN - Icekiub v4_1978295273489326081.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_511

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/LH-DMT版本-2.生图片类-048.Qwen一致性多角度写真摄影_2016524960361095169.json、图片生成/图生图/Qwen-多角度真人摄影一致性图生图_1989605255010766849.json、数字人/数字人/Dataset gen - QWEN - Icekiub v4_1978295273489326081.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SaveImageKJ`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveString` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
