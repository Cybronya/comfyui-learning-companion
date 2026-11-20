---
name: text_to_image_sampler_clip_unet_59
type: Text To Image
frequency: 11
level: moderate
coverage: 0.851818
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json, 图片生成/文生图/Z-image-暗黑浮世绘_1997401855502258178.json, 图片生成/文生图/Z-image-神级文生图-20秒超快速出图TEXT TO IMAGE_1993958594863366145.json, 图片生成/文生图/Z-image文生图_1993860952581931009.json, 图片生成/文生图/Z-image文生图人像摄影2K版_1994574159525126145.json, 图片生成/文生图/Z-image文生图工作流_2009195465652314113.json, 图片生成/文生图/Z-image文生图（最新加速版）_1996623220235182081.json, 图片生成/文生图/Z-image文生图（非收敛-随机种子生效版）_1996582595745955841.json, 图片生成/文生图/z-image-turbo flow dpo版文生图 自用_2050564898463207426.json, 图片生成/文生图/森哥AI文生图-超自然人像-20秒快速出图_2051690409042161666.json, 图片生成/文生图/（Z-image）dpmpp-2m-sde对比euler-文生图_1995128750184574977.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json、图片生成/文生图/Z-image-暗黑浮世绘_1997401855502258178.json、图片生成/文生图/Z-image-神级文生图-20秒超快速出图TEXT TO IMAGE_1993958594863366145.json、图片生成/文生图/Z-image文生图_1993860952581931009.json、图片生成/文生图/Z-image文生图人像摄影2K版_1994574159525126145.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 10/11 个有
- `SaveImage` —— 10/11 个有
- `CR Prompt Text` —— 8/11 个有
- `easy promptLine` —— 7/11 个有
- `GetNode` —— 6/11 个有
- `SetNode` —— 6/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `easy seed` —— 3/11 个有
- `LoadImage` —— 2/11 个有
- `HAIGC_SaveImagesToZip` —— 1/11 个有
- `ZML_ImageEncryption` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 11 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 62% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1080 | 768 - 1920 | 11 | 65% |
| 高度 | 1080 | 1024 - 1920 | 11 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，11 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1920，11 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，11 个样本
