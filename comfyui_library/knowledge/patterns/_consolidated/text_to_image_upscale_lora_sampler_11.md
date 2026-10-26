---
name: text_to_image_upscale_lora_sampler_11
type: Text To Image
frequency: 12
level: strong
coverage: 0.894917
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4K写实增强放大｜Krea2 + SeedVR文生图高清处理_2095102546200322050.json, 图片生成/文生图/Krea2 turbo 4K放大｜文生图高清美少女生成_2095953325475852289.json, 图片生成/文生图/Krea2+SeedVR双链路增强｜文生图4K写实放大直出_2110753734966992897.json, 图片生成/文生图/Krea2+SeedVR放大4K写实增强二版｜文生图高清放大写实一步到位不返工_2100478328087072770.json, 图片生成/文生图/Krea2_turbo高清放大4K｜美少女文生图画质增强_2096327079028678658.json, 图片生成/文生图/Krea2与SeedVR放大4K写实增强｜文生图高清画质提升_2097047991512293378.json, 图片生成/文生图/Krea2写实增强SeedVR精修版｜文生图真实质感再上一档_2099147440539660289.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强处理_2100294226142654465.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强处理工具_2100653749168590849.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强｜文生图再叠高清放大，写实质感直接拉满_2100455779584266241.json, 图片生成/文生图/Krea2加SeedVR放大增强，4K写实文生图质感升级_2110847767793983490.json, 图片生成/文生图/Z-Seed超清人像引擎｜高质量写真文生图_2094582526194044930.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/4K写实增强放大｜Krea2 + SeedVR文生图高清处理_2095102546200322050.json、图片生成/文生图/Krea2 turbo 4K放大｜文生图高清美少女生成_2095953325475852289.json、图片生成/文生图/Krea2+SeedVR双链路增强｜文生图4K写实放大直出_2110753734966992897.json、图片生成/文生图/Krea2+SeedVR放大4K写实增强二版｜文生图高清放大写实一步到位不返工_2100478328087072770.json、图片生成/文生图/Krea2_turbo高清放大4K｜美少女文生图画质增强_2096327079028678658.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 11/12 个有
- `EmptySD3LatentImage` —— 10/12 个有
- `ModelSamplingAuraFlow` —— 10/12 个有
- `CR Text Concatenate` —— 9/12 个有
- `ImpactInt` —— 9/12 个有
- `Lora Loader Stack (rgthree)` —— 9/12 个有
- `Text` —— 9/12 个有
- `LayerUtility: PurgeVRAM V2` —— 8/12 个有
- `ResolutionSelector` —— 3/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `TextConcatenate` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `FloatConstant` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `ImageSharpenKJ` —— 1/12 个有
- `SimpleCalculatorKJ` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（24/12 个样本）：Steps较低可能导致细节不足
