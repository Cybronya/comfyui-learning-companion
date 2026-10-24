---
name: text_to_image_upscale_lora_sampler_14
type: Text To Image
frequency: 11
level: weak
coverage: 0.907455
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4K写实增强放大｜Krea2 + SeedVR文生图高清处理_2095102546200322050.json, 图片生成/文生图/Krea2 Turbo+RAW加速版双方案文生图处理工作流_2102150335660908546.json, 图片生成/文生图/Krea2+SeedVR双链路增强｜文生图4K写实放大直出_2110753734966992897.json, 图片生成/文生图/Krea2+SeedVR放大4K写实增强二版｜文生图高清放大写实一步到位不返工_2100478328087072770.json, 图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json, 图片生成/文生图/Krea2与SeedVR放大4K写实增强｜文生图高清画质提升_2097047991512293378.json, 图片生成/文生图/Krea2写实增强SeedVR精修版｜文生图真实质感再上一档_2099147440539660289.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强处理_2100294226142654465.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强处理工具_2100653749168590849.json, 图片生成/文生图/Krea2加SeedVR放大4K写实增强｜文生图再叠高清放大，写实质感直接拉满_2100455779584266241.json, 图片生成/文生图/Krea2加SeedVR放大增强，4K写实文生图质感升级_2110847767793983490.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/4K写实增强放大｜Krea2 + SeedVR文生图高清处理_2095102546200322050.json、图片生成/文生图/Krea2 Turbo+RAW加速版双方案文生图处理工作流_2102150335660908546.json、图片生成/文生图/Krea2+SeedVR双链路增强｜文生图4K写实放大直出_2110753734966992897.json、图片生成/文生图/Krea2+SeedVR放大4K写实增强二版｜文生图高清放大写实一步到位不返工_2100478328087072770.json、图片生成/文生图/Krea2-turbo 版+RAW加速版双方案 2026.9.20更新_2071073541021323265.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 10/11 个有
- `solarL_SaveImagesToZip` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `EmptySD3LatentImage` —— 9/11 个有
- `ImpactInt` —— 9/11 个有
- `Lora Loader Stack (rgthree)` —— 9/11 个有
- `ModelSamplingAuraFlow` —— 9/11 个有
- `LayerUtility: PurgeVRAM V2` —— 8/11 个有
- `PreviewImage` —— 8/11 个有
- `Fast Groups Muter (rgthree)` —— 2/11 个有
- `Image Comparer (rgthree)` —— 2/11 个有
- `ImageScaleBy` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `easy clearCacheAll` —— 2/11 个有
- `easy int` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 74% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 91% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1680 | 11 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 91%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1680，11 个样本，取值分散，一致性仅 0%
- 高发问题（27/11 个样本）：Steps较低可能导致细节不足
