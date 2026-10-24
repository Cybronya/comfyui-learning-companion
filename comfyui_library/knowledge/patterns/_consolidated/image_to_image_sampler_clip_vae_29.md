---
name: image_to_image_sampler_clip_vae_29
type: Image To Image
frequency: 5
level: strong
coverage: 0.8362
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux1-Kontext图像外扩加速-Nunchaku_1950438024939266049.json, 图片生成/图生图/Flux1-Kontext扩图_1950434435030278145.json, 图片生成/图生图/Kontext老照片修复上色（高度还原，一键成片）极速版_2034265635953315841.json, 图片生成/图生图/图片胸部变大神器 Flux Kontext一键变大胸_2015768410298261506.json, 图片生成/图生图/图片胸部增强神器 一键变丰胸放大，优化美女身材_2051213394669252609.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux1-Kontext图像外扩加速-Nunchaku_1950438024939266049.json、图片生成/图生图/Flux1-Kontext扩图_1950434435030278145.json、图片生成/图生图/Kontext老照片修复上色（高度还原，一键成片）极速版_2034265635953315841.json、图片生成/图生图/图片胸部变大神器 Flux Kontext一键变大胸_2015768410298261506.json、图片生成/图生图/图片胸部增强神器 一键变丰胸放大，优化美女身材_2051213394669252609.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `TeaCache` —— 3/5 个有
- `UnetLoaderGGUF` —— 3/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `ImageStitch` —— 2/5 个有
- `LayerUtility: ExtendCanvas` —— 2/5 个有
- `NunchakuFluxDiTLoader` —— 2/5 个有
- `NunchakuFluxLoraLoader` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `Text Multiline` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
