---
name: image_to_image_sampler_clip_unet_6
type: Image To Image
frequency: 5
level: strong
coverage: 0.876
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
members: [图片生成/文生图/1960606116021493762.json, 图片生成/文生图/1961604160586190849.json, 图片生成/文生图/1977561433867210753.json, 图片生成/文生图/芝麻街特效_2073346446350442497.json, 视频生成/图生视频/2048657663176740866.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1960606116021493762.json、图片生成/文生图/1961604160586190849.json、图片生成/文生图/1977561433867210753.json、图片生成/文生图/芝麻街特效_2073346446350442497.json、视频生成/图生视频/2048657663176740866.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SUPIR_Upscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、CR Prompt Text
