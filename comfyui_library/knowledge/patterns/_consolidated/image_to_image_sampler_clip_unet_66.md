---
name: image_to_image_sampler_clip_unet_66
type: Image To Image
frequency: 8
level: strong
coverage: 0.816125
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, PreviewImage, RH_Translator, ReferenceLatent, SaveImage, ShowText|pysssss, TTP_text_mix, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext-稳定融图-双图版-产品_1940597087887323137.json, 图片生成/图生图/Kontext-稳定融图-双图版-产品_1970426361695379458.json, 图片生成/图生图/Kontext-稳定融图-双图版-产品_2115282970700505090.json, 图片生成/图生图/Kontext-稳定融图-双图版-产品_2115433914847285250.json, 图片生成/图生图/Kontext-稳定融图-双图版-产品_2115659549901414401.json, 图片生成/图生图/Kontext指定区域产品溶图（双图）_1942126651151171585.json, 平台全量/Kontext-人物换衣-绝不空卡_1939521018585333761.json, 平台全量/Kontext换指定背景_1941393036704432129.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_66

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext-稳定融图-双图版-产品_1940597087887323137.json、图片生成/图生图/Kontext-稳定融图-双图版-产品_1970426361695379458.json、图片生成/图生图/Kontext-稳定融图-双图版-产品_2115282970700505090.json、图片生成/图生图/Kontext-稳定融图-双图版-产品_2115433914847285250.json、图片生成/图生图/Kontext-稳定融图-双图版-产品_2115659549901414401.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_text_mix`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 7/8 个有
- `ImpactSwitch` —— 7/8 个有
- `RH_Captioner` —— 7/8 个有
- `CR Text Concatenate` —— 6/8 个有
- `FluxKontextImageScale` —— 6/8 个有
- `ImageAndMaskPreview` —— 6/8 个有
- `ImageConcanate` —— 6/8 个有
- `Mask Fill Holes` —— 6/8 个有
- `RepeatLatentBatch` —— 6/8 个有
- `ImpactInt` —— 5/8 个有
- `NunchakuFluxDiTLoader` —— 5/8 个有
- `RHHiddenNodes` —— 5/8 个有
- `Seed` —— 5/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `ImagePadForOutpaint` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `LoraLoader` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
