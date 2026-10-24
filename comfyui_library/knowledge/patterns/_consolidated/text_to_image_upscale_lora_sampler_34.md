---
name: text_to_image_upscale_lora_sampler_34
type: Text To Image
frequency: 7
level: moderate
coverage: 0.933571
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/二次元人物生成_2088191460100362241.json, 图片生成/文生图/二次元真人(男生）_2088399659025911810.json, 图片生成/文生图/二次元真人_2088197741246767105.json, 图片生成/文生图/摄影-文生图-Z-image-turbo_2096447342345015297.json, 图片生成/文生图/摄影质感文生图工作流｜Z-image turbo快速出图生成_2096729113515089922.json, 图片生成/文生图/文生图-人像生成写实风格_2087860545537011714.json, 图片生成/文生图/文生图-人像生成写实风格_2088186685191450626.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/二次元人物生成_2088191460100362241.json、图片生成/文生图/二次元真人(男生）_2088399659025911810.json、图片生成/文生图/二次元真人_2088197741246767105.json、图片生成/文生图/摄影-文生图-Z-image-turbo_2096447342345015297.json、图片生成/文生图/摄影质感文生图工作流｜Z-image turbo快速出图生成_2096729113515089922.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoaderGGUF` —— 5/7 个有
- `KOOK_ImageCompression` —— 5/7 个有
- `TextInputBasic` —— 5/7 个有
- `CLIPLoader` —— 2/7 个有
- `ImageFromBatch` —— 2/7 个有
- `LayerColor: Brightness & Contrast` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `solarL_SaveImagesToZip` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 80 - 1080 | 7 | 61% |
| 高度 | 1024 | 80 - 1920 | 7 | 52% |
| 采样步数 | 12 | 4 - 12 | 7 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 18% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 80 - 1080，7 个样本
- 高度 中位数 1024，观测区间 80 - 1920，7 个样本
- 采样步数 中位数 12，观测区间 4 - 12，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
