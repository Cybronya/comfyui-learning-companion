---
name: image_to_image_sampler_clip_unet_40
type: Image To Image
frequency: 9
level: strong
coverage: 0.894667
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商产品全能化妆品场景美妆白底图精修_2042856879147196418.json, 图片生成/图生图/电商产品全能场景人物手臂手势白底图精修_2048960893014249473.json, 图片生成/图生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2043516708916301826.json, 图片生成/图生图/电商人物修图全能场景模特人像白底图精修_2050541837659713538.json, 图片生成/图生图/豹豹喵呜：flux2-klein+z-image动漫转真人_2029883821256089602.json, 图片生成/图生图/超好用🔥挂拍_平铺图转纯色立体图-电商服饰展示-手残党专用_2062814563917189121.json, 图片生成/图生图/超细节-工业级产品精修_2068953091722010626.json, 图片生成/文生图/Klein文生图3D国漫CG风格（可以图像编辑）_2089981140185735170.json, 图片生成/文生图/Klein文生图CG动漫风格（可以图像编辑）_2043415759203868673.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/电商产品全能化妆品场景美妆白底图精修_2042856879147196418.json、图片生成/图生图/电商产品全能场景人物手臂手势白底图精修_2048960893014249473.json、图片生成/图生图/电商产品全能珠宝首饰场景戒指项链手镯白底图精修_2043516708916301826.json、图片生成/图生图/电商人物修图全能场景模特人像白底图精修_2050541837659713538.json、图片生成/图生图/豹豹喵呜：flux2-klein+z-image动漫转真人_2029883821256089602.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `ConditioningCombine` —— 4/9 个有
- `EmptyFlux2LatentImage` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `Int` —— 3/9 个有
- `CR Latent Input Switch` —— 2/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `Float` —— 1/9 个有
- `LayerUtility: FluxKontextImageScale` —— 1/9 个有
- `easy imageSize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 9 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.6 - 1 | 9 | 87% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 87%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
