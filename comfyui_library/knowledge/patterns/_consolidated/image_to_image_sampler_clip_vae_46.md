---
name: image_to_image_sampler_clip_vae_46
type: Image To Image
frequency: 5
level: strong
coverage: 0.8818
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/一键优化光影工作流_1968279142452088833.json, 平台全量/一键去水印工作流_1965037278286462978.json, 平台全量/一键转治愈卡通风格_1963635692441260034.json, 平台全量/一键转绘3D Q版 Chibi风格_1965257698738622465.json, 平台全量/照片转线稿_1963494281804861442.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_46

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/一键优化光影工作流_1968279142452088833.json、平台全量/一键去水印工作流_1965037278286462978.json、平台全量/一键转治愈卡通风格_1963635692441260034.json、平台全量/一键转绘3D Q版 Chibi风格_1965257698738622465.json、平台全量/照片转线稿_1963494281804861442.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `NunchakuTextEncoderLoaderV2` —— 4/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `Any Switch (rgthree)` —— 2/5 个有
- `NunchakuFluxLoraLoader` —— 2/5 个有
- `easy imagePixelPerfect` —— 2/5 个有
- `easy positive` —— 2/5 个有
- `DF_Text_Box` —— 1/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `ImageInvert` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `Manga2Anime_LineArt_Preprocessor` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
