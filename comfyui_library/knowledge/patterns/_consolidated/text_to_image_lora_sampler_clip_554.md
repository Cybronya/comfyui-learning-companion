---
name: text_to_image_lora_sampler_clip_554
type: Text To Image
frequency: 3
level: moderate
coverage: 0.932333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PIP_图像联结, SaveImage, SeedVR2, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/与IP合照_2020696703266988033.json, 图片生成/图生图/我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578.json, 平台全量/多图编辑一致性qwen_image_edit_2509_1971215633121787906.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_554

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/与IP合照_2020696703266988033.json、图片生成/图生图/我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578.json、平台全量/多图编辑一致性qwen_image_edit_2509_1971215633121787906.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PIP_图像联结`
- `SaveImage`
- `SeedVR2`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ReActorFaceSwap` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 20 | 3 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1920 | 768 - 1920 | 3 | 65% |
| 高度 | 1600 | 1024 - 1600 | 3 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 20，3 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 768 - 1920，3 个样本
- 高度 中位数 1600，观测区间 1024 - 1600，3 个样本，取值集中（一致性 81%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
