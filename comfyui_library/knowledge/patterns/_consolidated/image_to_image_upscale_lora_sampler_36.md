---
name: image_to_image_upscale_lora_sampler_36
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8908
common_nodes: [CLIPLoader, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit-2511可视化重打光·自由调节灯光_2017606636478664705.json, 图片生成/图生图/QwenEdit-参考图像人物重打光V1.0_2008916789152976898.json, 图片生成/图生图/Zimage重绘放大_1930179095877861377.json, 图片生成/图生图/【动漫转真人】极速流_Qwen+Z-image_真实洗图_2031187547338051585.json, 图片生成/图生图/星绘-千问Qwen动漫转真人流+Z-iamge增加质感-Seed放大(整合)_2015686476117315586.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit-2511可视化重打光·自由调节灯光_2017606636478664705.json、图片生成/图生图/QwenEdit-参考图像人物重打光V1.0_2008916789152976898.json、图片生成/图生图/Zimage重绘放大_1930179095877861377.json、图片生成/图生图/【动漫转真人】极速流_Qwen+Z-image_真实洗图_2031187547338051585.json、图片生成/图生图/星绘-千问Qwen动漫转真人流+Z-iamge增加质感-Seed放大(整合)_2015686476117315586.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `EmptySD3LatentImage` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `QwenMultiangleLightningNode` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `WujiCleaner` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 5 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 0.4 | 0.2 - 1 | 5 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，5 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.2 - 1，5 个样本，取值分散，一致性仅 40%
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
