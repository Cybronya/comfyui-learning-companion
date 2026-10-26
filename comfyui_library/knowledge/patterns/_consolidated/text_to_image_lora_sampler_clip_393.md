---
name: text_to_image_lora_sampler_clip_393
type: Text To Image
frequency: 5
level: strong
coverage: 0.8544
common_nodes: [CLIPLoader, CLIPTextEncode, CR Batch Images From List, CR Prompt List, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageFromBatch, ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2 一键生成多张模特图 生成多张模特图 随机洗图 超强一致性 双采样-提示词优化-全套_2073578961900228609.json, 图片生成/图生图/krea2 一键生成多张模特图 超强一致性 双采样-提示词优化-全套_2073574167177416705.json, 图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json, 图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json, 图片生成/文生图/zimage全能模特反推生图_2064574905911431170.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_393

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/krea2 一键生成多张模特图 生成多张模特图 随机洗图 超强一致性 双采样-提示词优化-全套_2073578961900228609.json、图片生成/图生图/krea2 一键生成多张模特图 超强一致性 双采样-提示词优化-全套_2073574167177416705.json、图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json、图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json、图片生成/文生图/zimage全能模特反推生图_2064574905911431170.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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
- `PreviewImage` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `PreviewAny` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `TextGenerate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 5 | 95% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1280 | 720 - 1280 | 5 | 74% |
| 高度 | 720 | 720 - 1280 | 5 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，5 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 720 - 1280，5 个样本
- 高度 中位数 720，观测区间 720 - 1280，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
