---
name: text_to_image_upscale_lora_sampler_21
type: Text To Image
frequency: 5
level: strong
coverage: 0.8628
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1978855905909444610.json, 图片生成/文生图/1981575575947091970.json, 图片生成/文生图/1985377282284003329.json, 图片生成/文生图/1986395833375617026.json, 图片生成/文生图/Qwen千问文生图【加速+放大】image_fp8_e4m3f + 低配 GGUF_2060253510142349313.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1978855905909444610.json、图片生成/文生图/1981575575947091970.json、图片生成/文生图/1985377282284003329.json、图片生成/文生图/1986395833375617026.json、图片生成/文生图/Qwen千问文生图【加速+放大】image_fp8_e4m3f + 低配 GGUF_2060253510142349313.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `FluxResolutionNode` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `ControlNetApplyAdvanced` —— 1/5 个有
- `ControlNetLoader` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 1024 - 1536 | 5 | 86% |
| 高度 | 2048 | 1024 - 2048 | 5 | 78% |
| 采样步数 | 4 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.8 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1536，观测区间 1024 - 1536，5 个样本，取值集中（一致性 86%）
- 高度 中位数 2048，观测区间 1024 - 2048，5 个样本
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
