---
name: image_to_image_sampler_clip_unet_29
type: Image To Image
frequency: 12
level: strong
coverage: 0.8275
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合014.人像去瑕美白精修_2035268281833099265.json, 图片生成/图生图/14.tonnie-kontext多图融合_1993643721023569921.json, 图片生成/图生图/260110009.人像去瑕美白精修_2011257114731225089.json, 图片生成/图生图/3D人物写实背景工作流_1941850807816110082.json, 图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json, 图片生成/图生图/Flux Kontext Dev图像编辑_1938636499573526530.json, 图片生成/图生图/Kontext-优化光影_1970693596301193217.json, 图片生成/图生图/Kontext_人像修图调色-清新色调_2099054597053706241.json, 图片生成/图生图/Kontext_人像修图调色-清新色调_2099659729835479041.json, 图片生成/图生图/kontext万物产品精修放大  保留细节_1948710764765949953.json, 平台全量/Flux Kontext 三视图_1941715710777389058.json, 平台全量/Kontext-保持角色一致-改变动作_1956022389840728066.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合014.人像去瑕美白精修_2035268281833099265.json、图片生成/图生图/14.tonnie-kontext多图融合_1993643721023569921.json、图片生成/图生图/260110009.人像去瑕美白精修_2011257114731225089.json、图片生成/图生图/3D人物写实背景工作流_1941850807816110082.json、图片生成/图生图/FLUX.kontext 产品精修官方工作流_1938785654178566146.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ConstrainImage|pysssss` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `JjkText` —— 8/12 个有
- `Anything Everywhere3` —— 7/12 个有
- `Image Comparer (rgthree)` —— 6/12 个有
- `FluxKontextImageScale` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `Anything Everywhere` —— 3/12 个有
- `easy imageConcat` —— 3/12 个有
- `Image Levels Adjustment` —— 2/12 个有
- `RH_Translator` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `Text Multiline` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 12 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
