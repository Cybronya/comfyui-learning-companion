---
name: text_to_image_lora_sampler_clip_264
type: Text To Image
frequency: 7
level: strong
coverage: 0.841571
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, ImpactSwitch, JjkText, KSampler, LoraLoaderModelOnly, PreviewImage, RH_Captioner, RH_Translator, ReferenceLatent, SaveImage, ShowText|pysssss, TTP_text_mix, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext本地版溶图打光｜自动版图生图直出_2092006370110435329.json, 图片生成/图生图/kontext本地版溶图打光｜自动版图生图直出_2092440180966912002.json, 图片生成/图生图/参考图模式换背景｜Kontext重新打光商品替换_2092186316686581762.json, 图片生成/图生图/双图版稳定融图｜Kontext产品商品替换图生图_2092195287308791809.json, 图片生成/图生图/溶图打光自动版｜kontext本地版图生图光影处理_2089495298904248321.json, 图片生成/图生图/自动溶图打光｜kontext本地版图生图一键出图_2092136961707438082.json, 图片生成/图生图/自动版打光溶图kontext本地版图生图_2087406300689952769.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/kontext本地版溶图打光｜自动版图生图直出_2092006370110435329.json、图片生成/图生图/kontext本地版溶图打光｜自动版图生图直出_2092440180966912002.json、图片生成/图生图/参考图模式换背景｜Kontext重新打光商品替换_2092186316686581762.json、图片生成/图生图/双图版稳定融图｜Kontext产品商品替换图生图_2092195287308791809.json、图片生成/图生图/溶图打光自动版｜kontext本地版图生图光影处理_2089495298904248321.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Captioner`
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
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 6/7 个有
- `LoadAndResizeImage` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `LoraLoader` —— 6/7 个有
- `Primitive integer [Crystools]` —— 6/7 个有
- `RepeatLatentBatch` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `ColorMatch` —— 5/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageAndMaskPreview` —— 1/7 个有
- `ImagePadForOutpaint` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `Mask Fill Holes` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `Seed` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
