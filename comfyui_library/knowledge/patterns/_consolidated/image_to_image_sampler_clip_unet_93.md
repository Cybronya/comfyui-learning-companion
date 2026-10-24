---
name: image_to_image_sampler_clip_unet_93
type: Image To Image
frequency: 5
level: strong
coverage: 0.6056
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-character-creator_1939591599125086210.json, 图片生成/图生图/flux_1_kontext（5连拍生成图片）_1938980661526978561.json, 图片生成/图生图/kontext构建统一特征编辑图片_1947557530525442050.json, 图片生成/图生图/【手把手教你用Kontext】抠图换物_改衣换发_一键换景_秒变风格 _ ComfyUI 保姆级教程_1939170907774767106.json, 图片生成/图生图/一键三视图Kontext-character-creator_1943503167298695169.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext-character-creator_1939591599125086210.json、图片生成/图生图/flux_1_kontext（5连拍生成图片）_1938980661526978561.json、图片生成/图生图/kontext构建统一特征编辑图片_1947557530525442050.json、图片生成/图生图/【手把手教你用Kontext】抠图换物_改衣换发_一键换景_秒变风格 _ ComfyUI 保姆级教程_1939170907774767106.json、图片生成/图生图/一键三视图Kontext-character-creator_1943503167298695169.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `CFGZeroStar` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `PatchModelPatcherOrder` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `RMBG` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
