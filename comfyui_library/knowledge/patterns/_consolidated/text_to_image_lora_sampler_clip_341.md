---
name: text_to_image_lora_sampler_clip_341
type: Text To Image
frequency: 6
level: strong
coverage: 0.846333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Batch Images From List, CR Prompt List, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageFromBatch, ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json, 图片生成/图生图/krea2 一键生成多张模特图 生成多张模特图 随机洗图 超强一致性 双采样-提示词优化-全套_2073578961900228609.json, 图片生成/图生图/krea2 一键生成多张模特图 超强一致性 双采样-提示词优化-全套_2073574167177416705.json, 图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json, 图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json, 图片生成/文生图/zimage全能模特反推生图_2064574905911431170.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_341

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/doubao-seed-2+zimage-turbo模特文生图_2072582582184796162.json、图片生成/图生图/krea2 一键生成多张模特图 生成多张模特图 随机洗图 超强一致性 双采样-提示词优化-全套_2073578961900228609.json、图片生成/图生图/krea2 一键生成多张模特图 超强一致性 双采样-提示词优化-全套_2073574167177416705.json、图片生成/文生图/Krea 2 turbo-时尚模特_2079102838994718721.json、图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Batch Images From List`
- `CR Prompt List`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Dapao_LlamaCaption` —— 5/6 个有
- `Dapao_LlamaCaptionOptions` —— 5/6 个有
- `RegexReplace` —— 5/6 个有
- `PreviewImage` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `PreviewAny` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `TextGenerate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1000 | 720 - 1280 | 6 | 72% |
| 高度 | 1000 | 720 - 1280 | 6 | 72% |
| 采样步数 | 8 | 8 - 10 | 6 | 89% |
| Prompt 约束强度(CFG) | 1.05 | 1 - 1.1 | 6 | 95% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | bong_tangent | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1000，观测区间 720 - 1280，6 个样本
- 高度 中位数 1000，观测区间 720 - 1280，6 个样本
- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.05，观测区间 1 - 1.1，6 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 bong_tangent，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
