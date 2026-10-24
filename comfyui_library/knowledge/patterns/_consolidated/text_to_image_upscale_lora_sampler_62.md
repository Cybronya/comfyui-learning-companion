---
name: text_to_image_upscale_lora_sampler_62
type: Text To Image
frequency: 4
level: moderate
coverage: 0.91825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN终极编辑图片+KLEIN洗真实图4K高清_2024522702354128898.json, 图片生成/图生图/🌸快图-圆桌布提取测试自己的模型_2052220894784835585.json, 图片生成/文生图/QWEN-IMAGE商用快速流(YIHAN AIGC)_2027722964245942273.json, 图片生成/文生图/Z-IMAGE文生图+图生图(YIHAN AIGC)_2026990202874503170.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/QWEN终极编辑图片+KLEIN洗真实图4K高清_2024522702354128898.json、图片生成/图生图/🌸快图-圆桌布提取测试自己的模型_2052220894784835585.json、图片生成/文生图/QWEN-IMAGE商用快速流(YIHAN AIGC)_2027722964245942273.json、图片生成/文生图/Z-IMAGE文生图+图生图(YIHAN AIGC)_2026990202874503170.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `Text` —— 1/4 个有
- `TextConcatenate` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1800 | 4 | 66% |
| 高度 | 1140 | 720 - 1920 | 4 | 65% |
| 采样步数 | 8 | 4 - 12 | 4 | 65% |
| Prompt 约束强度(CFG) | 1.25 | 1 - 3 | 4 | 50% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.69 - 1 | 4 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1800，4 个样本
- 高度 中位数 1140，观测区间 720 - 1920，4 个样本
- 采样步数 中位数 8，观测区间 4 - 12，4 个样本
- Prompt 约束强度(CFG) 中位数 1.25，观测区间 1 - 3，4 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.69 - 1，4 个样本，取值集中（一致性 85%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
