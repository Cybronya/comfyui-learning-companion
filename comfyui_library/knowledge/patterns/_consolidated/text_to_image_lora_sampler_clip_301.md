---
name: text_to_image_lora_sampler_clip_301
type: Text To Image
frequency: 3
level: strong
coverage: 0.845333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Batch Images From List, CR Prompt List, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageFromBatch, ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json, 图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json, 图片生成/文生图/zimage全能模特反推生图_2064574905911431170.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_301

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea 2 电商模特图-2.0_2076532743651020802.json、图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json、图片生成/文生图/zimage全能模特反推生图_2064574905911431170.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Batch Images From List`
- `CR Prompt List`
- `CR Text`
- `ConditioningZeroOut`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RegexReplace`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `SeedVR2Conditioning` —— 1/3 个有
- `SeedVR2PostProcessing` —— 1/3 个有
- `SeedVR2Preprocess` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1280 | 3 | 71% |
| 高度 | 1280 | 720 - 1280 | 3 | 76% |
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 1.1 | 3 | 96% |
| 采样算法 | euler_ancestral | - | 3 | 33% |
| 调度器 | bong_tangent | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1280，3 个样本
- 高度 中位数 1280，观测区间 720 - 1280，3 个样本
- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 1.1，3 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 33%
- 调度器 最常用 bong_tangent，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
