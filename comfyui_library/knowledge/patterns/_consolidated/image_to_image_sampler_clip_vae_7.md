---
name: image_to_image_sampler_clip_vae_7
type: Image To Image
frequency: 18
level: strong
coverage: 0.911778
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontest 室内视角切换_1984511757903347714.json, 图片生成/图生图/Kontext-极速图像去水印擦除_1982499686877675521.json, 图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json, 图片生成/图生图/KontextDev转绘Aaron Limonick风格_1940989134209183745.json, 图片生成/图生图/KontextDev转绘Aaron Siskind风格_1941007183553445890.json, 图片生成/图生图/KontextNunchakuDevLora万物3D立体风格_1943136210699108354.json, 图片生成/图生图/KontextNunchakuDevLora万物加蓝色怪物_1943138415128821762.json, 图片生成/图生图/KontextNunchakuDevLora万物国画风格_1942785288521322498.json, 图片生成/图生图/KontextNunchakuDevLora万物毛毡_1943147438742134786.json, 图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json, 图片生成/图生图/KontextNunchakuDev转绘墨绘长笔画_1940998785357213697.json, 图片生成/图生图/KontextNunchakuDev转绘英雄幻想风格_1941004455217414145.json, 图片生成/图生图/kontext+nunchaku极速版工作流_1939455859959242754.json, 图片生成/图生图/nunchaku-flux.1-kontext-dev_1939389707900076034.json, 图片生成/图生图/nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353.json, 图片生成/图生图/全能去除图形_字体_水印图片【无残留】_2057355116965089281.json, 图片生成/图生图/去水印_2010982510636834818.json, 图片生成/图生图/简易Kontext Dev （nunchaku加速）_1938911346601680897.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/Kontest 室内视角切换_1984511757903347714.json、图片生成/图生图/Kontext-极速图像去水印擦除_1982499686877675521.json、图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json、图片生成/图生图/KontextDev转绘Aaron Limonick风格_1940989134209183745.json、图片生成/图生图/KontextDev转绘Aaron Siskind风格_1941007183553445890.json…）

- **类型**：Image To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 16/18 个有
- `ModelSamplingFlux` —— 10/18 个有
- `RH_Translator` —— 10/18 个有
- `ImageStitch` —— 7/18 个有
- `LoadImageOutput` —— 6/18 个有
- `LoraLoaderModelOnly` —— 6/18 个有
- `ShowText|pysssss` —— 6/18 个有
- `PreviewImage` —— 5/18 个有
- `EmptySD3LatentImage` —— 4/18 个有
- `GoogleTranslator` —— 2/18 个有
- `NunchakuFluxLoraLoader` —— 2/18 个有
- `CR Upscale Image` —— 1/18 个有
- `ImageScaleToTotalPixels` —— 1/18 个有
- `Text Multiline` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 18 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
