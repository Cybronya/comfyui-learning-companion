---
name: image_to_image_lora_sampler_clip_40
type: Image To Image
frequency: 7
level: moderate
coverage: 0.607714
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR String To Number, CR Text, ConditioningZeroOut, Fast Groups Muter (rgthree), GetNode, Image Comparer (rgthree), ImageConcanate, ImpactSwitch, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SetNode, ShowText|pysssss, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258.json, 图片生成/图生图/【Cq808】动漫转真人工作流_2012411368175050754.json, 图片生成/图生图/动漫转真人+双效果_2043592000166957058.json, 图片生成/图生图/动漫转真人+双效果（Qwen Edit 2511效果+ Z-image写实）_2010916858924376066.json, 图片生成/图生图/动漫转真人_z-image写实重绘，平替全能图片V1 pro_2004175779003047938.json, 图片生成/图生图/动漫转真人工作流_2051156201915863042.json, 图片生成/图生图/动漫转真人通透+高清版（Qwen Edit 2511+ Z-image写实）_2042432850552688642.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Seedance2.0真人剧人物专用-人物通透+高清_2041795616782688258.json、图片生成/图生图/【Cq808】动漫转真人工作流_2012411368175050754.json、图片生成/图生图/动漫转真人+双效果_2043592000166957058.json、图片生成/图生图/动漫转真人+双效果（Qwen Edit 2511效果+ Z-image写实）_2010916858924376066.json、图片生成/图生图/动漫转真人_z-image写实重绘，平替全能图片V1 pro_2004175779003047938.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR String To Number`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImpactSwitch`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PlaySound|pysssss` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `CFGGuider` —— 2/7 个有
- `ColorMatch` —— 2/7 个有
- `EmptyFlux2LatentImage` —— 2/7 个有
- `Flux2Scheduler` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `ImageSharpen` —— 2/7 个有
- `KSamplerSelect` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `RandomNoise` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `SamplerCustomAdvanced` —— 2/7 个有
- `CustomAddLabel` —— 1/7 个有
- `easy float` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 25 | 7 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 7 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，7 个样本
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
