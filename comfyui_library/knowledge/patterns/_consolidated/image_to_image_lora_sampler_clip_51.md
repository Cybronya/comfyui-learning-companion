---
name: image_to_image_lora_sampler_clip_51
type: Image To Image
frequency: 6
level: strong
coverage: 0.637667
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ImpactInt, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键动漫转真人-可以更换各种画风_2013236666323968002.json, 图片生成/图生图/一键动漫转真人-支持各种画风输入_2004212976079044610.json, 图片生成/图生图/动漫转真人_2008928543228567553.json, 图片生成/图生图/最强一键动漫转真人（支持二次元，各种画风）_2007718006536802306.json, 图片生成/图生图/最强动漫转真人-支持各种画风_2010171657729609729.json, 图片生成/文生图/Qwenimage-edit2511一键动漫转真人-支持各种画风输入_2004568960207122434.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键动漫转真人-可以更换各种画风_2013236666323968002.json、图片生成/图生图/一键动漫转真人-支持各种画风输入_2004212976079044610.json、图片生成/图生图/动漫转真人_2008928543228567553.json、图片生成/图生图/最强一键动漫转真人（支持二次元，各种画风）_2007718006536802306.json、图片生成/图生图/最强动漫转真人-支持各种画风_2010171657729609729.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `MemoryCleaner` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Qwen3_VQA` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `UNETLoader_Any` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 6 | 75% |
| Prompt 约束强度(CFG) | 1.6 | 1 - 1.6 | 6 | 85% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 83% |
| 重绘幅度 | 0.9 | 0.9 - 1 | 6 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1.6，观测区间 1 - 1.6，6 个样本，取值集中（一致性 85%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 83%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 1，6 个样本，取值集中（一致性 96%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
