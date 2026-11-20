---
name: image_to_image_sampler_clip_unet_79
type: Image To Image
frequency: 6
level: strong
coverage: 0.760333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext构建统一特征编辑图片_1947557530525442050.json, 图片生成/图生图/【手把手教你用Kontext】抠图换物_改衣换发_一键换景_秒变风格 _ ComfyUI 保姆级教程_1939170907774767106.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜光影修改_1938479250225692674.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜图像文字增加_1938450260434051074.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜图像风格重绘_1938443160634720257.json, 图片生成/图生图/合照生成器_1952250801282560001.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/kontext构建统一特征编辑图片_1947557530525442050.json、图片生成/图生图/【手把手教你用Kontext】抠图换物_改衣换发_一键换景_秒变风格 _ ComfyUI 保姆级教程_1939170907774767106.json、图片生成/图生图/【非API】 Kontext Dev 模型｜光影修改_1938479250225692674.json、图片生成/图生图/【非API】 Kontext Dev 模型｜图像文字增加_1938450260434051074.json、图片生成/图生图/【非API】 Kontext Dev 模型｜图像风格重绘_1938443160634720257.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
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
- `EmptySD3LatentImage` —— 5/6 个有
- `LoadImageOutput` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `ImageCompositeMasked` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `StringReplace` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
