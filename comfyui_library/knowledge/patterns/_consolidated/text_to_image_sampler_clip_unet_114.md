---
name: text_to_image_sampler_clip_unet_114
type: Text To Image
frequency: 6
level: moderate
coverage: 0.889
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, ImpactInt, KSampler, LoadImage, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json, 图片生成/文生图/Zimage-turbo保暖内衣_2051484069925531650.json, 图片生成/文生图/krea2+z_image+boogu模型测试对比_2069616764018843650.json, 图片生成/文生图/zimage+krea2+boogu三模型对比_2069599329727373314.json, 图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json, 图片生成/文生图/zimage全能模特反推生图_2064574905911431170.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea-2 高真实感与卓越美学文生图_2069624809176256513.json、图片生成/文生图/Zimage-turbo保暖内衣_2051484069925531650.json、图片生成/文生图/krea2+z_image+boogu模型测试对比_2069616764018843650.json、图片生成/文生图/zimage+krea2+boogu三模型对比_2069599329727373314.json、图片生成/文生图/zimage-turbo-青少年模特_2067209702450229250.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLatentImage`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `RegexReplace`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `CR Batch Images From List` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `ImageFromBatch` —— 2/6 个有
- `LayerUtility: ImageReel` —— 2/6 个有
- `LayerUtility: ImageReelComposit` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `ProcessString` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1280 | 6 | 74% |
| 高度 | 1280 | 720 - 1280 | 6 | 82% |
| 采样步数 | 8 | 4 - 15 | 6 | 63% |
| Prompt 约束强度(CFG) | 1.05 | 1 - 1.1 | 6 | 95% |
| 采样算法 | er_sde | - | 6 | 33% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1280，6 个样本
- 高度 中位数 1280，观测区间 720 - 1280，6 个样本，取值集中（一致性 82%）
- 采样步数 中位数 8，观测区间 4 - 15，6 个样本
- Prompt 约束强度(CFG) 中位数 1.05，观测区间 1 - 1.1，6 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
