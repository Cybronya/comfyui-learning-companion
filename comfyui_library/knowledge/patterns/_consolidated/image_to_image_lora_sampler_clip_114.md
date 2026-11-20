---
name: image_to_image_lora_sampler_clip_114
type: Image To Image
frequency: 4
level: strong
coverage: 0.863
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/小红书爆款3D emoji小人_1956325155729539073.json, 图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json, 图片生成/图生图/最强素颜化妆上妆flux_kontext_dev_1963264724798517250.json, 图片生成/文生图/喜剧复古动漫风格2.0_1942402202403024898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/小红书爆款3D emoji小人_1956325155729539073.json、图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json、图片生成/图生图/最强素颜化妆上妆flux_kontext_dev_1963264724798517250.json、图片生成/文生图/喜剧复古动漫风格2.0_1942402202403024898.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `CR Text Replace` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `Display Any (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `LayerUtility: GetImageSize` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `easy promptList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
