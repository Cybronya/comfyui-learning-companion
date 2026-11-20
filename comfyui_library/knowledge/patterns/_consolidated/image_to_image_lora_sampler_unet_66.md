---
name: image_to_image_lora_sampler_unet_66
type: Image To Image
frequency: 10
level: strong
coverage: 0.8894
common_nodes: [CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2改图_扩图多合一_2091494374692712449.json, 图片生成/图生图/Krea2改图_扩图多合一_2092613324746870785.json, 图片生成/图生图/Krea2改图_扩图多合一_2097137551667720194.json, 图片生成/图生图/Krea2改图_扩图多合一_2097232544029827074.json, 图片生成/图生图/krea2 turbo 图像扩展_2093702213427355650.json, 图片生成/图生图/krea2 单图编辑_2093346016568365057.json, 图片生成/图生图/krea2 双图编辑 换背景_换脸_换衣_2093702412547739650.json, 图片生成/图生图/krea2-Single Image _ Dual Image _ Inpainting_2089356156211912706.json, 图片生成/图生图/▶▷krea2-图像编辑-整合流_2116139918576668674.json, 图片生成/文生图/Krea2-图片扩展_超乎你想象_2089999274397495298.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_66

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Krea2改图_扩图多合一_2091494374692712449.json、图片生成/图生图/Krea2改图_扩图多合一_2092613324746870785.json、图片生成/图生图/Krea2改图_扩图多合一_2097137551667720194.json、图片生成/图生图/Krea2改图_扩图多合一_2097232544029827074.json、图片生成/图生图/krea2 turbo 图像扩展_2093702213427355650.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 9/10 个有
- `DrawMaskOnImage` —— 8/10 个有
- `ImagePadForOutpaint` —— 7/10 个有
- `AnyBooleanSwitch` —— 4/10 个有
- `ImpactConditionalBranch` —— 4/10 个有
- `Label (rgthree)` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `PrimitiveFloat` —— 4/10 个有
- `easy boolean` —— 4/10 个有
- `CompressImages` —— 3/10 个有
- `ResolutionSelector` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
