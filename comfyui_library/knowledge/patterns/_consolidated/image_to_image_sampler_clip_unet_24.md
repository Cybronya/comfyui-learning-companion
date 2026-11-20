---
name: image_to_image_sampler_clip_unet_24
type: Image To Image
frequency: 14
level: strong
coverage: 0.794571
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/换装-Kontext-白底图穿衣上身走秀_1955854421794193409.json, 平台全量/4K高清放大 拯救废片 匹敌SeedVR 一键优化光影+增强清晰度 一键专业摄影人物模特写真_2000387998258692098.json, 平台全量/9.tonnie-kontext去水印_1991948516983459842.json, 平台全量/Flux Kontext 高清修复+4k放大_1944948883966582786.json, 平台全量/Kontext - ins风高级感暗调_1955983227603308546.json, 平台全量/Kontext - 消除水印_1962818918081540097.json, 平台全量/Kontext Dev生成医疗素材骨骼图_1948054291473924098.json, 平台全量/Kontext 人像修图调色-清新色调_1954472011533840385.json, 平台全量/Kontext 闪光灯效果_1952377409792356354.json, 平台全量/Kontext-优化光影_1957645581407678466.json, 平台全量/Kontext人像调色_冰甜音鸣色调_1952328998632271874.json, 平台全量/人像精修 _ 统一色调 _ 清洁瑕疵 _ 精修皮肤_1948294884968005633.json, 平台全量/人像精修 人像瘦脸祛痘磨皮美白 皮肤美白人像精修  颜色统一色调 清洁瑕疵 精修皮肤_2000842658815803394.json, 平台全量/婚纱摄影精修 拯救废片 kontext 一键精修原片  人物皮肤变白皙 瘦脸_2000401498007797761.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/换装-Kontext-白底图穿衣上身走秀_1955854421794193409.json、平台全量/4K高清放大 拯救废片 匹敌SeedVR 一键优化光影+增强清晰度 一键专业摄影人物模特写真_2000387998258692098.json、平台全量/9.tonnie-kontext去水印_1991948516983459842.json、平台全量/Flux Kontext 高清修复+4k放大_1944948883966582786.json、平台全量/Kontext - ins风高级感暗调_1955983227603308546.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 13/14 个有
- `ConstrainImage|pysssss` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `JjkText` —— 11/14 个有
- `Anything Everywhere3` —— 10/14 个有
- `Image Comparer (rgthree)` —— 9/14 个有
- `PreviewImage` —— 4/14 个有
- `FluxKontextImageScale` —— 3/14 个有
- `Image Levels Adjustment` —— 3/14 个有
- `DeepTranslatorTextNode` —— 1/14 个有
- `PrimitiveString` —— 1/14 个有
- `PromptComposerMerge` —— 1/14 个有
- `SUPIR_Upscale` —— 1/14 个有
- `easy imageCount` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 14 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，14 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
