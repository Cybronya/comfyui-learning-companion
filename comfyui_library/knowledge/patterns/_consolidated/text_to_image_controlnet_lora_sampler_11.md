---
name: text_to_image_controlnet_lora_sampler_11
type: Text To Image
frequency: 3
level: strong
coverage: 0.862667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/Qwen Image, Controlnet 深度图转绘_1987177038278758402.json", "图片生成/图生图/Qwen Image,线稿控制 室内设计_1987163511790964738.json", "图片生成/图生图/Qwen Image，千问图生图, Controlnet 深度图转绘，SeedVR2.5.1_1987760149278429186.json"]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image, Controlnet 深度图转绘_1987177038278758402.json、图片生成/图生图/Qwen Image,线稿控制 室内设计_1987163511790964738.json、图片生成/图生图/Qwen Image，千问图生图, Controlnet 深度图转绘，SeedVR2.5.1_1987760149278429186.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Canny` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
