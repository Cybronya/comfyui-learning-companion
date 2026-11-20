---
name: image_to_image_lora_sampler_unet_232
type: Image To Image
frequency: 3
level: weak
coverage: 0.774
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image_字体直出_字体设计_书法字体_综艺字体_海报生成QwenEdit_1982996678984773634.json, 图片生成/文生图/最新千问图像编辑_1970656696915927042.json, 平台全量/AI服装拆解_2008177332917379074.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_232

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-Image_字体直出_字体设计_书法字体_综艺字体_海报生成QwenEdit_1982996678984773634.json、图片生成/文生图/最新千问图像编辑_1970656696915927042.json、平台全量/AI服装拆解_2008177332917379074.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `CLIPTextEncode` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Float` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 3 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.55 - 1 | 3 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，3 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.55 - 1，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
