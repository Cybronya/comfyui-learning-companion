---
name: unknown_workflow_upscale_lora_sampler_13
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8416
common_nodes: [BetterFilmGrain, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ImageScaleToMegapixels, ImageSharpen, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, easy promptConcat, LayerUtility: PurgeVRAM, CR Prompt Text]
members: [图片生成/文生图/1956048542387326978.json, 图片生成/文生图/1956895648390811649.json, 图片生成/文生图/1961790773043904514.json, 图片生成/文生图/1965055612562362369.json, 图片生成/文生图/1968189243870838785.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1956048542387326978.json、图片生成/文生图/1956895648390811649.json、图片生成/文生图/1961790773043904514.json、图片生成/文生图/1965055612562362369.json、图片生成/文生图/1968189243870838785.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BetterFilmGrain`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImageScaleToMegapixels`
- `ImageSharpen`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EsesImageEffectBloom` —— 4/5 个有
- `easy showAnything` —— 3/5 个有
- `CFGNorm` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `NunchakuQwenImageDiTLoader` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy promptConcat` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `LazySwitch2way` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 5 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.15 - 1 | 5 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，5 个样本，取值分散，一致性仅 37%
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、easy promptConcat、LayerUtility: PurgeVRAM、CR Prompt Text
