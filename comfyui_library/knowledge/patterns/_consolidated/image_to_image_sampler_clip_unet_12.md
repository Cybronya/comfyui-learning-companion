---
name: image_to_image_sampler_clip_unet_12
type: Image To Image
frequency: 16
level: moderate
coverage: 0.971562
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json, 图片生成/图生图/Aiwood-Kontext多图变单图_1939277870109794305.json, 图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json, 图片生成/图生图/Flux Kontext Dev-三图融合-加速版+放大_1947113716854337537.json, 图片生成/图生图/Flux Kontext Dev-图片生成3视图加速版+放大_1942029327120941058.json, 图片生成/图生图/Flux Kontext Dev-图片转变手办加速版+放大_1943663969976352770.json, 图片生成/图生图/Flux Kontext Dev-图片转国画风格加速版+放大_1943229697700618241.json, 图片生成/图生图/Flux Kontext Dev-图片转水彩画加速版+放大_1943871375528329218.json, 图片生成/图生图/Flux Kontext Dev-图片转电影颗粒质感风格加速版+放大_1943871523440693250.json, 图片生成/图生图/Flux Kontext Dev-图片风格转绘（毛毡）加速版+放大_1943122910695342081.json, 图片生成/图生图/Flux Kontext Dev-扩图加速版+放大_1943871102491955202.json, 图片生成/图生图/Flux Kontext Dev-拼好图-加速版+放大_1946752768034136066.json, 图片生成/图生图/Flux Kontext Dev万物转3D Chibi Style加速版+放大（单图）_1940291607579021314.json, 图片生成/图生图/Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410.json, 图片生成/图生图/Flux Kontext Dev万物转吉卜力加速版+放大（单图）_1940569779944189954.json, 图片生成/图生图/kontext万能贴图融图_1947305896571457537.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json、图片生成/图生图/Aiwood-Kontext多图变单图_1939277870109794305.json、图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json、图片生成/图生图/Flux Kontext Dev-三图融合-加速版+放大_1947113716854337537.json、图片生成/图生图/Flux Kontext Dev-图片生成3视图加速版+放大_1942029327120941058.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 15/16 个有
- `NunchakuFluxDiTLoader` —— 14/16 个有
- `NunchakuFluxLoraLoader` —— 14/16 个有
- `ImageStitch` —— 12/16 个有
- `PMRF` —— 12/16 个有
- `RH_Translator` —— 12/16 个有
- `Text Multiline` —— 12/16 个有
- `LoraLoaderModelOnly` —— 6/16 个有
- `PreviewImage` —— 6/16 个有
- `easy imageRemBg` —— 6/16 个有
- `FastCanvas` —— 5/16 个有
- `FastCanvasTool` —— 5/16 个有
- `ImageScaleToMegapixels` —— 4/16 个有
- `DeepTranslatorTextNode` —— 3/16 个有
- `ImageConcanate` —— 3/16 个有
- `CR Text Concatenate` —— 1/16 个有
- `Compositor3` —— 1/16 个有
- `CompositorConfig3` —— 1/16 个有
- `ImageCrop+` —— 1/16 个有
- `ImagePadForOutpaint` —— 1/16 个有
- `LayerUtility: CropByMask V2` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `ShowText|pysssss` —— 1/16 个有
- `TextInput_` —— 1/16 个有
- `easy imageConcat` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 16 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（10/16 个样本）：Steps较低可能导致细节不足
