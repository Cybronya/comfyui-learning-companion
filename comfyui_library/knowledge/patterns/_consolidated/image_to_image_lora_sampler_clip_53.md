---
name: image_to_image_lora_sampler_clip_53
type: Image To Image
frequency: 7
level: moderate
coverage: 0.919714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetImageSize, ImageScaleToTotalPixels, KSampler, LatentCutToBatch, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-layered图片分层工作流_2003451865083854850.json, 图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json, 图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json, 图片生成/图生图/qwen_layered_一键图像分层工作流_2007791149074878466.json, 图片生成/图生图/图片分层_2013537317499179010.json, 图片生成/文生图/图片分层工作流（支持复杂图层，亲测可跑！！！）_2093280821024223233.json, 平台全量/Qwen Image Layered  精准抠图 图片分层抠图 千问分层 分层编辑 八步加速 灵活_2006905453321658370.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-image-layered图片分层工作流_2003451865083854850.json、图片生成/图生图/qwen-image-layered-image2image-分层式生图-图生图_2003438837143642113.json、图片生成/图生图/qwen-image-layered-image2image_2002227567119724545.json、图片生成/图生图/qwen_layered_一键图像分层工作流_2007791149074878466.json、图片生成/图生图/图片分层_2013537317499179010.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
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
- `AILab_QwenVL` —— 4/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `PrimitiveInt` —— 4/7 个有
- `ShowText|pysssss` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `Text Multiline` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `easy promptConcat` —— 4/7 个有
- `CFGNorm` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 7 | 60% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 7 | 60% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
