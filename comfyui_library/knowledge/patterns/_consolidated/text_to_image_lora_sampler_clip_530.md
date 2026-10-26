---
name: text_to_image_lora_sampler_clip_530
type: Text To Image
frequency: 3
level: strong
coverage: 0.702667
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, Qwen3_VQA, RH_LLMAPI_Pro_Node, SaveImage, SetNode, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy showAnything, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/数字人产品介绍分镜（手动）_2044000838875619329.json, 图片生成/图生图/数字人产品介绍分镜（自动版）_2043997163478323201.json, 图片生成/文生图/角色设计（手动版）_2043853457924296705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_530

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/数字人产品介绍分镜（手动）_2044000838875619329.json、图片生成/图生图/数字人产品介绍分镜（自动版）_2043997163478323201.json、图片生成/文生图/角色设计（手动版）_2043853457924296705.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `Qwen3_VQA`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `SetNode`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 1/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `RH_Nano_Banana_Image2Image` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 2000 | 3 | 69% |
| 高度 | 1920 | 1504 - 1920 | 3 | 89% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 2000，3 个样本
- 高度 中位数 1920，观测区间 1504 - 1920，3 个样本，取值集中（一致性 89%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（15/3 个样本）：Steps较低可能导致细节不足
