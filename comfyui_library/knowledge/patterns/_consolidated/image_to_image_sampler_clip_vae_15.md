---
name: image_to_image_sampler_clip_vae_15
type: Image To Image
frequency: 13
level: strong
coverage: 0.985923
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontest 室内视角切换_1984511757903347714.json, 图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json, 图片生成/图生图/KontextDev转绘Aaron Limonick风格_1940989134209183745.json, 图片生成/图生图/KontextDev转绘Aaron Siskind风格_1941007183553445890.json, 图片生成/图生图/KontextNunchakuDev3D游戏动画_1942411012631105537.json, 图片生成/图生图/KontextNunchakuDevLora万物3D立体风格_1943136210699108354.json, 图片生成/图生图/KontextNunchakuDevLora万物加蓝色怪物_1943138415128821762.json, 图片生成/图生图/KontextNunchakuDevLora万物国画风格_1942785288521322498.json, 图片生成/图生图/KontextNunchakuDevLora万物毛毡_1943147438742134786.json, 图片生成/图生图/KontextNunchakuDevLora万物皮克斯风格_1944262455931338753.json, 图片生成/图生图/KontextNunchakuDevLora人物三视图_1944263357543120898.json, 图片生成/图生图/KontextNunchakuDevLora发光粒子素描风格_1943525207695126529.json, 图片生成/图生图/KontextNunchakuDevLora拍立得相片_1944265400445992961.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_15

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Kontest 室内视角切换_1984511757903347714.json、图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json、图片生成/图生图/KontextDev转绘Aaron Limonick风格_1940989134209183745.json、图片生成/图生图/KontextDev转绘Aaron Siskind风格_1941007183553445890.json、图片生成/图生图/KontextNunchakuDev3D游戏动画_1942411012631105537.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 13 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 12/13 个有
- `ModelSamplingFlux` —— 12/13 个有
- `RH_Translator` —— 12/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `SDXLPromptStyler` —— 5/13 个有
- `ArtistsImage_Zho` —— 4/13 个有
- `EmptySD3LatentImage` —— 4/13 个有
- `JoinStringMulti` —— 4/13 个有
- `ShowText|pysssss` —— 2/13 个有
- `CR Upscale Image` —— 1/13 个有
- `GoogleTranslator` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `NunchakuFluxLoraLoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
