---
name: text_to_image_upscale_lora_sampler_61
type: Text To Image
frequency: 4
level: moderate
coverage: 0.86825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-IMAGE通用便捷流(YIHAN AIGC)_2027358509737713666.json, 图片生成/图生图/🌸快图-圆桌布提取测试自己的模型_2052220894784835585.json, 图片生成/文生图/LLM提示词+二次采样+seedvr2_z_image_2012854900971016194.json, 图片生成/文生图/Z-IMAGE文生图+图生图(YIHAN AIGC)_2026990202874503170.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Z-IMAGE通用便捷流(YIHAN AIGC)_2027358509737713666.json、图片生成/图生图/🌸快图-圆桌布提取测试自己的模型_2052220894784835585.json、图片生成/文生图/LLM提示词+二次采样+seedvr2_z_image_2012854900971016194.json、图片生成/文生图/Z-IMAGE文生图+图生图(YIHAN AIGC)_2026990202874503170.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Qwen3_VQA_Plus` —— 2/4 个有
- `ShowText` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `TextConcatenate` —— 1/4 个有
- `TextEncodeQwenImageEditPlus` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 900 | 720 - 1800 | 4 | 59% |
| 高度 | 960 | 720 - 1920 | 4 | 57% |
| 采样步数 | 9 | 8 - 12 | 4 | 84% |
| Prompt 约束强度(CFG) | 1.25 | 1 - 3 | 4 | 50% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.905 | 0.69 - 1 | 4 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 900，观测区间 720 - 1800，4 个样本
- 高度 中位数 960，观测区间 720 - 1920，4 个样本
- 采样步数 中位数 9，观测区间 8 - 12，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1.25，观测区间 1 - 3，4 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.905，观测区间 0.69 - 1，4 个样本，取值集中（一致性 85%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
