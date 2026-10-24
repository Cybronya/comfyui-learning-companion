---
name: text_to_image_sampler_clip_unet_22
type: Text To Image
frequency: 16
level: weak
coverage: 0.837375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Trubo极速文生图｜美商极高出图快 颜值党直呼内行_2105557272117202946.json, 图片生成/文生图/Krea2 Turbo极速版美商极高文生图V2_2100289687335297026.json, 图片生成/文生图/Krea2 Turbo极速版美商极高文生图，高质量文本到图像生成工具_2105735805019971585.json, 图片生成/文生图/Krea2 Turbo美商极高文生图 极速版高质量图片生成_2098661641754857473.json, 图片生成/文生图/Krea2 turbo 4K放大｜文生图高清美少女生成_2095953325475852289.json, 图片生成/文生图/Krea2-真人角色4K文生图_2095131210359074818.json, 图片生成/文生图/Krea2_turbo 4K放大_2079597154166988801.json, 图片生成/文生图/Krea2_turbo 4K放大_2080129101544906754.json, 图片生成/文生图/Krea2_turbo_4K放大_2080939525467099137.json, 图片生成/文生图/Krea2_turbo_4K放大_2095797338735468546.json, 图片生成/文生图/Krea2_turbo_4K放大_2096154230204751874.json, 图片生成/文生图/Krea2_turbo高清放大4K｜美少女文生图画质增强_2096327079028678658.json, 图片生成/文生图/Moss image 官方文生图｜人像写真二次元两相宜_2112447881939611649.json, 图片生成/文生图/Qwen image 2.1文生图全套｜模型节点下载链接都备齐_2103098595393228801.json, 图片生成/文生图/Qwen image 2.1文生图带模型节点下载链接 新手友好_2104780019913543682.json, 图片生成/文生图/Qwen image 2.1文生图教程版｜附模型和节点下载链接，开箱即用_2104549164205039618.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Krea2 Trubo极速文生图｜美商极高出图快 颜值党直呼内行_2105557272117202946.json、图片生成/文生图/Krea2 Turbo极速版美商极高文生图V2_2100289687335297026.json、图片生成/文生图/Krea2 Turbo极速版美商极高文生图，高质量文本到图像生成工具_2105735805019971585.json、图片生成/文生图/Krea2 Turbo美商极高文生图 极速版高质量图片生成_2098661641754857473.json、图片生成/文生图/Krea2 turbo 4K放大｜文生图高清美少女生成_2095953325475852289.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/16 个有
- `PreviewImage` —— 12/16 个有
- `PrimitiveStringMultiline` —— 12/16 个有
- `ResolutionSelector` —— 12/16 个有
- `SeedVR2LoadDiTModel` —— 12/16 个有
- `SeedVR2LoadVAEModel` —— 12/16 个有
- `SeedVR2VideoUpscaler` —— 12/16 个有
- `LoraLoaderModelOnly` —— 11/16 个有
- `JjkText` —— 10/16 个有
- `solarL_SaveImagesToZip` —— 10/16 个有
- `孤海注释` —— 10/16 个有
- `TextConcatenate` —— 7/16 个有
- `Fast Groups Bypasser (rgthree)` —— 5/16 个有
- `ImageScaleToTotalPixels` —— 5/16 个有
- `CR Text` —— 4/16 个有
- `Image Comparer (rgthree)` —— 4/16 个有
- `PreviewAny` —— 4/16 个有
- `QZ_ResolutionPreset` —— 4/16 个有
- `Seed (rgthree)` —— 4/16 个有
- `TextGenerate` —— 4/16 个有
- `Any Switch (rgthree)` —— 3/16 个有
- `RegexExtract` —— 3/16 个有
- `StringConcatenate` —— 3/16 个有
- `TextEncodeQwenImage21` —— 3/16 个有
- `ComfySwitchNode` —— 1/16 个有
- `EmptyFlux2LatentImage` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 16 | 0% |
| 高度 | 80 | 80 - 1280 | 16 | 0% |
| 采样步数 | 4 | 4 - 9 | 16 | 64% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 16 | 48% |
| 采样算法 | er_sde | - | 16 | 69% |
| 调度器 | beta | - | 16 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1280，16 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 9，16 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，16 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，16 个样本，一致性 69%
- 调度器 最常用 beta，16 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
