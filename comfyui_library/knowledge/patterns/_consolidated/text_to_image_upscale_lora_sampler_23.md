---
name: text_to_image_upscale_lora_sampler_23
type: Text To Image
frequency: 5
level: strong
coverage: 0.992
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, CR Seed, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen 2512千问专业生图 4步加速 高清修复_2006400610735759362.json, 图片生成/文生图/Qwen千问专业美人儿艺术写真摄影_V1无损加速版_1991993648657264642.json, 图片生成/文生图/Qwen千问专业美人儿艺术写真摄影_V2细节放大加速版_1994424416291393538.json, 图片生成/文生图/Z image专业摄影艺术写真日常照V1_1993867062244212738.json, 图片生成/文生图/Z image艺术写真日常照自动反推洗图版V2_1994424539327176706.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen 2512千问专业生图 4步加速 高清修复_2006400610735759362.json、图片生成/文生图/Qwen千问专业美人儿艺术写真摄影_V1无损加速版_1991993648657264642.json、图片生成/文生图/Qwen千问专业美人儿艺术写真摄影_V2细节放大加速版_1994424416291393538.json、图片生成/文生图/Z image专业摄影艺术写真日常照V1_1993867062244212738.json、图片生成/文生图/Z image艺术写真日常照自动反推洗图版V2_1994424539327176706.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Seed`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FastFilmGrain` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy clearCacheAll` —— 2/5 个有
- `ImageLoader` —— 1/5 个有
- `MultiplePathsInput` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1104 | 5 | 96% |
| 高度 | 1536 | 1472 - 1536 | 5 | 98% |
| 采样步数 | 8 | 4 - 10 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1104，5 个样本，取值集中（一致性 96%）
- 高度 中位数 1536，观测区间 1472 - 1536，5 个样本，取值集中（一致性 98%）
- 采样步数 中位数 8，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
