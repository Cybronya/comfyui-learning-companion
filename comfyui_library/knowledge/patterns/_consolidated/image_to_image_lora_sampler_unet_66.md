---
name: image_to_image_lora_sampler_unet_66
type: Image To Image
frequency: 9
level: strong
coverage: 0.898778
common_nodes: [CFGNorm, CLIPLoader, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditEnhanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/多图融合Qwen-Image-Edit图像编辑_1958033725604900866.json, 图片生成/图生图/打光-Qwen-Image-Edit图像编辑_1959152314194014209.json, 图片生成/图生图/文字编辑设计-Qwen-Image-Edit图像编辑_1958318280551370754.json, 图片生成/图生图/文字编辑设计-Qwen-Image-Edit图像编辑_1973274791648038914.json, 图片生成/图生图/服装加模特-Qwen-Image-Edit图像编辑_1958680755813642241.json, 图片生成/图生图/电商手提包溶图-Put-It-Here-Qwen-8步加速版_1964254396915830786.json, 图片生成/图生图/电商手提包溶图-Put-It-Here-Qwen版_1962153400169381889.json, 图片生成/图生图/电商服装溶图-Put-It-Here-Qwen版_1962134309098471425.json, 图片生成/图生图/耳坠珠宝溶图-Put-It-Here-Qwen版_1962130346370383874.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_66

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/多图融合Qwen-Image-Edit图像编辑_1958033725604900866.json、图片生成/图生图/打光-Qwen-Image-Edit图像编辑_1959152314194014209.json、图片生成/图生图/文字编辑设计-Qwen-Image-Edit图像编辑_1958318280551370754.json、图片生成/图生图/文字编辑设计-Qwen-Image-Edit图像编辑_1973274791648038914.json、图片生成/图生图/服装加模特-Qwen-Image-Edit图像编辑_1958680755813642241.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditEnhanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleDownToSize` —— 8/9 个有
- `Text Multiline` —— 8/9 个有
- `TextEncodeQwenImageEdit` —— 8/9 个有
- `FastCanvas` —— 4/9 个有
- `FastCanvasTool` —— 4/9 个有
- `easy imageRemBg` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `GetImageSizeAndCount` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 9 | 83% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 9 | 80% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，9 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
