---
name: image_to_image_lora_sampler_clip_45
type: Image To Image
frequency: 6
level: moderate
coverage: 0.920167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSize, ImageScaleToTotalPixels, KSampler, LatentCutToBatch, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-layered图片分层工作流_2003451865083854850.json, 图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json, 图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json, 图片生成/图生图/qwen_layered_一键图像分层工作流_2007791149074878466.json, 图片生成/图生图/图片分层_2013537317499179010.json, 图片生成/文生图/图片分层工作流（支持复杂图层，亲测可跑！！！）_2093280821024223233.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-image-layered图片分层工作流_2003451865083854850.json、图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json、图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json、图片生成/图生图/qwen_layered_一键图像分层工作流_2007791149074878466.json、图片生成/图生图/图片分层_2013537317499179010.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `easy promptConcat` —— 3/6 个有
- `CFGNorm` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 6 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 6 | 57% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
