---
name: text_to_image_ipadapter_inpaint_lora
type: Text To Image
frequency: 5
level: strong
coverage: 0.8212
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CR Image Input Switch, CR Text Concatenate, CheckpointLoaderSimple, EmptyLatentImage, Fast Groups Bypasser (rgthree), IPAdapterFaceID, IPAdapterInsightFaceLoader, IPAdapterModelLoader, InpaintCropImproved, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, ShowText|pysssss, TextEncodeQwenImageEditPlus, TextInput_, VAEDecode, VAEEncode, easy cleanGpuUsed, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit 人脸生图_2070350537991737345.json, 图片生成/图生图/Qwen-image-edit 人脸生图（N版）_2069194857998016514.json, 图片生成/图生图/Qwen-image-edit_人脸生图N版_2072856697135263746.json, 图片生成/文生图/Qwen-image-edit 人脸生图_2071398731890642946.json, 图片生成/文生图/Qwen-image-edit_人脸生图N版_2072591304965582850.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit 人脸生图_2070350537991737345.json、图片生成/图生图/Qwen-image-edit 人脸生图（N版）_2069194857998016514.json、图片生成/图生图/Qwen-image-edit_人脸生图N版_2072856697135263746.json、图片生成/文生图/Qwen-image-edit 人脸生图_2071398731890642946.json、图片生成/文生图/Qwen-image-edit_人脸生图N版_2072591304965582850.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Image Input Switch`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `IPAdapterFaceID`
- `IPAdapterInsightFaceLoader`
- `IPAdapterModelLoader`
- `InpaintCropImproved`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `VAEDecode`
- `VAEEncode`
- `easy cleanGpuUsed`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `VAELoader` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.08 | 0.08 - 0.1 | 5 | 89% |
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1600 | 1600 - 1600 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.08，观测区间 0.08 - 0.1，5 个样本，取值集中（一致性 89%）
- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1600，观测区间 1600 - 1600，5 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
