---
name: text_to_image_upscale_lora_sampler_23
type: Text To Image
frequency: 9
level: moderate
coverage: 0.978333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json, 图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json, 图片生成/文生图/Krea2 - 2K Ultra-clear details_2095547125550641153.json, 图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json, 图片生成/文生图/Qwen 2512千问专业生图 4步加速 高清修复_2006400610735759362.json, 图片生成/文生图/Qwen千问专业美人儿艺术写真摄影_V1无损加速版_1991993648657264642.json, 图片生成/文生图/Qwen千问专业美人儿艺术写真摄影_V2细节放大加速版_1994424416291393538.json, 图片生成/文生图/Z image专业摄影艺术写真日常照V1_1993867062244212738.json, 图片生成/文生图/Z image艺术写真日常照自动反推洗图版V2_1994424539327176706.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/2号特工：Z-image-base文生图+人脸Lora+seedvr2超分放大_2076991277698211841.json、图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json、图片生成/文生图/Krea2 - 2K Ultra-clear details_2095547125550641153.json、图片生成/文生图/Krea2 lora+高清放大基础工作流_2089602538793422849.json、图片生成/文生图/Qwen 2512千问专业生图 4步加速 高清修复_2006400610735759362.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 6/9 个有
- `ModelSamplingAuraFlow` —— 6/9 个有
- `CR SDXL Aspect Ratio` —— 5/9 个有
- `CR Seed` —— 5/9 个有
- `FastFilmGrain` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `easy clearCacheAll` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageLoader` —— 1/9 个有
- `Int` —— 1/9 个有
- `MultiplePathsInput` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有
- `SaveImagePlus` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `TTResolutionSelector` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1104 | 9 | 71% |
| 高度 | 1472 | 512 - 1920 | 9 | 63% |
| 采样步数 | 8 | 4 - 10 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 0.58 - 1 | 9 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1104，9 个样本
- 高度 中位数 1472，观测区间 512 - 1920，9 个样本
- 采样步数 中位数 8，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，9 个样本，取值集中（一致性 86%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
