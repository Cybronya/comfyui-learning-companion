---
name: image_to_image_sampler_clip_unet_115
type: Image To Image
frequency: 4
level: strong
coverage: 0.7855
common_nodes: [CLIPTextEncode, Compositor3, CompositorConfig3, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcatMulti, ImageScaleToMegapixels, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Kontext 二阶段多图编辑_1948951304136269825.json, 图片生成/图生图/Kontext-双图合并_1944947594637533185.json, 图片生成/图生图/Kontext-双图合并_1971036154441175042.json, 图片生成/图生图/Kontext优化多图融合，批量出图_1939381299322994689.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_115

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext 二阶段多图编辑_1948951304136269825.json、图片生成/图生图/Kontext-双图合并_1944947594637533185.json、图片生成/图生图/Kontext-双图合并_1971036154441175042.json、图片生成/图生图/Kontext优化多图融合，批量出图_1939381299322994689.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `Compositor3`
- `CompositorConfig3`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `GetImageSize` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `CR Latent Batch Size` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `LoraLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
