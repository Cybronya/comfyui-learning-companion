---
name: image_to_image_lora_sampler_clip_42
type: Image To Image
frequency: 6
level: strong
coverage: 0.924167
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json, 图片生成/图生图/Aiwood-Kontext多图变单图_1939277870109794305.json, 图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json, 图片生成/图生图/Flux Kontext Dev-三图融合-加速版+放大_1947113716854337537.json, 图片生成/图生图/Flux Kontext Dev-拼好图-加速版+放大_1946752768034136066.json, 图片生成/图生图/kontext万能贴图融图_1947305896571457537.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json、图片生成/图生图/Aiwood-Kontext多图变单图_1939277870109794305.json、图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json、图片生成/图生图/Flux Kontext Dev-三图融合-加速版+放大_1947113716854337537.json、图片生成/图生图/Flux Kontext Dev-拼好图-加速版+放大_1946752768034136066.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `FastCanvas` —— 5/6 个有
- `FastCanvasTool` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `ImageScaleToMegapixels` —— 4/6 个有
- `NunchakuFluxDiTLoader` —— 4/6 个有
- `NunchakuFluxLoraLoader` —— 4/6 个有
- `DeepTranslatorTextNode` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `ImageStitch` —— 2/6 个有
- `PMRF` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `Compositor3` —— 1/6 个有
- `CompositorConfig3` —— 1/6 个有
- `ImageCrop+` —— 1/6 个有
- `LayerUtility: CropByMask V2` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextInput_` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
