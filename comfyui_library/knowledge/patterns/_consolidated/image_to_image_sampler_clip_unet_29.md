---
name: image_to_image_sampler_clip_unet_29
type: Image To Image
frequency: 11
level: moderate
coverage: 0.920909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LatentCutToBatch, LoadImage, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【千问拆图层】Qwen Image Layered_2002673476114739202.json, 图片生成/图生图/加速版-最新大模型开源了，Qwen Image Layered千问分层_2002305597573853185.json, 图片生成/图生图/动漫元素拆分+Qwen图像分层（图生图）_2002563301303283714.json, 图片生成/图生图/图层分层 Qwen Image Layered_2002217745301291009.json, 图片生成/图生图/图层分解-8步加速版-Qwen Image Layered_2002217705514102786.json, 图片生成/图生图/图层分解-8步加速版-Qwen Image Layered_2036724128123719681.json, 图片生成/文生图/Qwen Image Layered千问分层模型_2002135922642698242.json, 图片生成/文生图/Qwen Image Layered千问分层模型_2002219692104249346.json, 图片生成/文生图/Qwen Image Layered千问分层模型_2002653665032847361.json, 图片生成/文生图/动漫元素生成+Qwen图像分层（文生图）_2002222909483544577.json, 图片生成/文生图/千问分层模型_2003286731317239809.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_29

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/【千问拆图层】Qwen Image Layered_2002673476114739202.json、图片生成/图生图/加速版-最新大模型开源了，Qwen Image Layered千问分层_2002305597573853185.json、图片生成/图生图/动漫元素拆分+Qwen图像分层（图生图）_2002563301303283714.json、图片生成/图生图/图层分层 Qwen Image Layered_2002217745301291009.json、图片生成/图生图/图层分解-8步加速版-Qwen Image Layered_2002217705514102786.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `Int` —— 6/11 个有
- `LatentFromBatch` —— 6/11 个有
- `MathExpression|pysssss` —— 6/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `Float` —— 2/11 个有
- `PlaySound|pysssss` —— 2/11 个有
- `Anything Everywhere3` —— 1/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `easy imageScaleDownToSize` —— 1/11 个有
- `easy imageSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 8 - 40 | 11 | 56% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 11 | 68% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 8 - 40，11 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
