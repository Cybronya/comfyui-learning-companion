---
name: text_to_image_ipadapter_inpaint_lora
type: Text To Image
frequency: 2
level: weak
coverage: 0.822
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CR Image Input Switch, CR Text Concatenate, CheckpointLoaderSimple, EmptyLatentImage, Fast Groups Bypasser (rgthree), IPAdapterFaceID, IPAdapterInsightFaceLoader, IPAdapterModelLoader, InpaintCropImproved, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, ShowText|pysssss, TextEncodeQwenImageEditPlus, TextInput_, VAEDecode, VAEEncode, easy cleanGpuUsed, easy getNode, easy setNode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-image-edit 人脸生图_2071398731890642946.json, 图片生成/文生图/Qwen-image-edit_人脸生图N版_2072591304965582850.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen-image-edit 人脸生图_2071398731890642946.json、图片生成/文生图/Qwen-image-edit_人脸生图N版_2072591304965582850.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CLIPLoader` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.09 | - | 2 | 89% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1600 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.09，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1600，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
