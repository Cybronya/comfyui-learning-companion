---
name: image_to_image_sampler_clip_unet_30
type: Image To Image
frequency: 10
level: strong
coverage: 0.8281
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合014.人像去瑕美白精修_2035268281833099265.json, 图片生成/图生图/14.tonnie-kontext多图融合_1993643721023569921.json, 图片生成/图生图/260110009.人像去瑕美白精修_2011257114731225089.json, 图片生成/图生图/3D人物写实背景工作流_1941850807816110082.json, 图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json, 图片生成/图生图/Flux Kontext Dev图像编辑_1938636499573526530.json, 图片生成/图生图/Kontext-优化光影_1970693596301193217.json, 图片生成/图生图/Kontext_人像修图调色-清新色调_2099054597053706241.json, 图片生成/图生图/Kontext_人像修图调色-清新色调_2099659729835479041.json, 图片生成/图生图/kontext万物产品精修放大  保留细节_1948710764765949953.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合014.人像去瑕美白精修_2035268281833099265.json、图片生成/图生图/14.tonnie-kontext多图融合_1993643721023569921.json、图片生成/图生图/260110009.人像去瑕美白精修_2011257114731225089.json、图片生成/图生图/3D人物写实背景工作流_1941850807816110082.json、图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/10 个有
- `ConstrainImage|pysssss` —— 7/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `JjkText` —— 6/10 个有
- `Anything Everywhere3` —— 5/10 个有
- `FluxKontextImageScale` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `Image Levels Adjustment` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `easy imageConcat` —— 2/10 个有
- `Anything Everywhere` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `Text Multiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 10 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
