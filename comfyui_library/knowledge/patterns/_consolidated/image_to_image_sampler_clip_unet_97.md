---
name: image_to_image_sampler_clip_unet_97
type: Image To Image
frequency: 5
level: moderate
coverage: 0.6118
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageFromBatch+, ImageResizeKJv2, KSampler, LatentCutToBatch, LoadImage, LoaderGGUF, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-Layered + Qwen3VL_2002935533619802113.json, 图片生成/图生图/Qwen-Image-Layered_2004588849772851202.json, 图片生成/图生图/Qwen-Image-Layered大模型：替代PS魔棒工具，一键把图片分成多个图层！_2003727872856604673.json, 图片生成/图生图/🐱千问图案提取+Qwen-Image-Layered图像拆解分层😼_2006413406139584513.json, 图片生成/文生图/Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_97

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Layered + Qwen3VL_2002935533619802113.json、图片生成/图生图/Qwen-Image-Layered_2004588849772851202.json、图片生成/图生图/Qwen-Image-Layered大模型：替代PS魔棒工具，一键把图片分成多个图层！_2003727872856604673.json、图片生成/图生图/🐱千问图案提取+Qwen-Image-Layered图像拆解分层😼_2006413406139584513.json、图片生成/文生图/Qwen-Image-Layered + Qwen3VL自动提示词-图像分层生成工作流_2003323013783289857.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSampler`
- `LatentCutToBatch`
- `LoadImage`
- `LoaderGGUF`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `AILab_QwenVL` —— 3/5 个有
- `Int` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `AILab_QwenVL_Advanced` —— 1/5 个有
- `CFGNorm` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `QwenImageLayered - Layer to Length Mapper` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 50 | 5 | 54% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4 | 5 | 76% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.99 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 50，5 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.99 - 1，5 个样本，取值集中（一致性 100%）
