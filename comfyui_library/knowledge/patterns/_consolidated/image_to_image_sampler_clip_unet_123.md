---
name: image_to_image_sampler_clip_unet_123
type: Image To Image
frequency: 4
level: strong
coverage: 0.9515
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键三视图+骨骼图参考_Kontext-DEV_1948706378098122753.json, 图片生成/图生图/老照片修复-Flux-Kontext图像编辑-老照片上色_1943519646446481409.json, 图片生成/图生图/老照片修复极速版_1992987621192302594.json, 图片生成/文生图/黑森林官方Kontext Presets预设模板_1944383441200664578.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键三视图+骨骼图参考_Kontext-DEV_1948706378098122753.json、图片生成/图生图/老照片修复-Flux-Kontext图像编辑-老照片上色_1943519646446481409.json、图片生成/图生图/老照片修复极速版_1992987621192302594.json、图片生成/文生图/黑森林官方Kontext Presets预设模板_1944383441200664578.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ImageScaleDownToSize` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `CR Simple Image Compare` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `LoadKontextPresets` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
