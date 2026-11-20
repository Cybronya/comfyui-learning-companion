---
name: image_to_image_sampler_clip_unet_119
type: Image To Image
frequency: 5
level: strong
coverage: 0.8154
common_nodes: [CLIPTextEncode, Compositor3, CompositorConfig3, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcatMulti, ImageScaleToMegapixels, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Kontext 二阶段多图编辑_1948951304136269825.json, 图片生成/图生图/Kontext-双图合并_1944947594637533185.json, 图片生成/图生图/Kontext-双图合并_1971036154441175042.json, 图片生成/图生图/Kontext优化多图融合，批量出图_1939381299322994689.json, 平台全量/kontextCC贴图局部重绘_1951232091746869250.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_119

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext 二阶段多图编辑_1948951304136269825.json、图片生成/图生图/Kontext-双图合并_1944947594637533185.json、图片生成/图生图/Kontext-双图合并_1971036154441175042.json、图片生成/图生图/Kontext优化多图融合，批量出图_1939381299322994689.json、平台全量/kontextCC贴图局部重绘_1951232091746869250.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImageConcanate` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `CR Latent Batch Size` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `LoraLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
