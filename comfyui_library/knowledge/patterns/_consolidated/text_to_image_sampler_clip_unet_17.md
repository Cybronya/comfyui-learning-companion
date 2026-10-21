---
name: text_to_image_sampler_clip_unet_17
type: Text To Image
frequency: 17
level: weak
coverage: 0.774588
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Raw文生图V1_2069649846545506305.json, 图片生成/文生图/Krea2 Raw文生图V1_2069955897165697025.json, 图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json, 图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json, 图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072504382511476738.json, 图片生成/文生图/Krea2 Turbo Realism Engineer文生图_2072366906035761153.json, 图片生成/文生图/Krea2 Turbo 文生图  + 高清_2070085337044574209.json, 图片生成/文生图/Krea2 Turbo 文生图 极速写实摄影工作流_2072318540417425410.json, 图片生成/文生图/Krea2 turbo 4K放大｜文生图高清美少女生成_2095953325475852289.json, 图片生成/文生图/Krea2_turbo 4K放大_2079597154166988801.json, 图片生成/文生图/Krea2_turbo 4K放大_2080129101544906754.json, 图片生成/文生图/Krea2_turbo_4K放大_2080939525467099137.json, 图片生成/文生图/Krea2_turbo_4K放大_2095797338735468546.json, 图片生成/文生图/Krea2_turbo_4K放大_2096154230204751874.json, 图片生成/文生图/Krea2_turbo高清放大4K｜美少女文生图画质增强_2096327079028678658.json, 图片生成/文生图/Qwen2.1文生图带提示词增强高清放大精干版，数字人文生图方案_2103559733838962690.json, 图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_17

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Krea2 Raw文生图V1_2069649846545506305.json、图片生成/文生图/Krea2 Raw文生图V1_2069955897165697025.json、图片生成/文生图/Krea2 Raw版-文生图-v1.0_2070040927531528193.json、图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072187241404911618.json、图片生成/文生图/Krea2 Turbo Realism Engineer V2文生图_2072504382511476738.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 15/17 个有
- `ConditioningZeroOut` —— 14/17 个有
- `SeedVR2LoadDiTModel` —— 10/17 个有
- `SeedVR2LoadVAEModel` —— 10/17 个有
- `SeedVR2VideoUpscaler` —— 10/17 个有
- `TextGenerate` —— 10/17 个有
- `PreviewImage` —— 9/17 个有
- `LoraLoaderModelOnly` —— 8/17 个有
- `PreviewAny` —— 8/17 个有
- `StringConcatenate` —— 8/17 个有
- `TextConcatenate` —— 7/17 个有
- `孤海注释` —— 5/17 个有
- `JjkText` —— 4/17 个有
- `solarL_SaveImagesToZip` —— 4/17 个有
- `ImageConcanate` —— 3/17 个有
- `ImageScaleBy` —— 2/17 个有
- `StringConstantMultiline` —— 2/17 个有
- `TextEncodeQwenImage21` —— 2/17 个有
- `easy clearCacheAll` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `LoadImage` —— 1/17 个有
- `easy int` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 17 | 50% |
| 高度 | 1024 | 80 - 1024 | 17 | 50% |
| 采样步数 | 8 | 4 - 28 | 17 | 22% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 17 | 32% |
| 采样算法 | euler | - | 17 | 76% |
| 调度器 | simple | - | 17 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，17 个样本
- 高度 中位数 1024，观测区间 80 - 1024，17 个样本
- 采样步数 中位数 8，观测区间 4 - 28，17 个样本，取值分散，一致性仅 22%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，17 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，17 个样本，一致性 76%
- 调度器 最常用 simple，17 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（19/17 个样本）：Steps较低可能导致细节不足
