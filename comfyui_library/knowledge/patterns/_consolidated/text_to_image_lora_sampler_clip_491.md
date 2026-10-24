---
name: text_to_image_lora_sampler_clip_491
type: Text To Image
frequency: 3
level: strong
coverage: 0.873333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Batch Images From List, CR Prompt List, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageFromBatch, ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2 一键生成多张模特图 生成多张模特图 随机洗图 超强一致性 双采样-提示词优化-全套_2073578961900228609.json, 图片生成/图生图/krea2 一键生成多张模特图 超强一致性 双采样-提示词优化-全套_2073574167177416705.json, 图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_491

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea2 一键生成多张模特图 生成多张模特图 随机洗图 超强一致性 双采样-提示词优化-全套_2073578961900228609.json、图片生成/图生图/krea2 一键生成多张模特图 超强一致性 双采样-提示词优化-全套_2073574167177416705.json、图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `RegexReplace`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextGenerate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 720 | 720 - 720 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
