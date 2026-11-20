---
name: image_to_image_lora_sampler_unet_159
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8594
common_nodes: [CFGNorm, CLIPLoader, ImageConcanate, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen Edit 提示词预设 多功能编辑工作流_1968589171730337793.json, 图片生成/图生图/千问Qwen-image-edit：像素级掌控，图像编辑新纪元！图像编辑_图生图_修图_设计_1958872031519518721.json, 图片生成/图生图/最新Qwen-Image-Edit2509：指令式AI画笔，单图编辑，所指即所改！_1970432534721011714.json, 平台全量/Qwen Edit多功能编辑，提示词预设_1960256323571101698.json, 平台全量/换汤_1976266207454208001.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_159

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/千问Qwen Edit 提示词预设 多功能编辑工作流_1968589171730337793.json、图片生成/图生图/千问Qwen-image-edit：像素级掌控，图像编辑新纪元！图像编辑_图生图_修图_设计_1958872031519518721.json、图片生成/图生图/最新Qwen-Image-Edit2509：指令式AI画笔，单图编辑，所指即所改！_1970432534721011714.json、平台全量/Qwen Edit多功能编辑，提示词预设_1960256323571101698.json、平台全量/换汤_1976266207454208001.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 3/5 个有
- `CR Prompt List` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `LayerUtility: ExtendCanvas` —— 2/5 个有
- `RepeatLatentBatch` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `TextEncodeQwenImageEditPlus` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
