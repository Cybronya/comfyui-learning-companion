---
name: unknown_workflow_sampler_clip_vae_5
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.965733
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageResize+, KSamplerSelect, LoadImage, ModelSamplingFlux, RH_Translator, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI站-Kontext+单图-万能改图_1958728770838491137.json, 图片生成/图生图/FLUX-KONTEXT万能改图王_1942396729872297986.json, 图片生成/图生图/Flux Kontext - LoRA 加速改图_1952543043369021442.json, 图片生成/图生图/Flux Kontext Dev｜模特手持产品海报_1938591805661175809.json, 图片生成/图生图/KonText一句话改双图，技术有限，创意无限！_1948024769821192193.json, 图片生成/图生图/Kontext Dev ｜ 产品换背景_1939712994286673922.json, 图片生成/图生图/Kontext Dev ｜ 稳定背景替换_1939558862167130114.json, 图片生成/图生图/Kontext 万能改图_1967793005967081473.json, 图片生成/图生图/Kontext 三图-万能改图_1938438669726580738.json, 图片生成/图生图/Kontext 单图-万能改图_1938422713163649026.json, 图片生成/图生图/Kontext 单图-万能改图_1944937257440825346.json, 图片生成/图生图/Kontext 单图-万能改图_1957344213035839489.json, 图片生成/图生图/Kontext 单图-万能改图_1981601811096313857.json, 图片生成/图生图/Kontext 双图-nun版_1944378870537572354.json, 图片生成/图生图/Kontext 双图-万能改图_1938432790901755906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/AI站-Kontext+单图-万能改图_1958728770838491137.json、图片生成/图生图/FLUX-KONTEXT万能改图王_1942396729872297986.json、图片生成/图生图/Flux Kontext - LoRA 加速改图_1952543043369021442.json、图片生成/图生图/Flux Kontext Dev｜模特手持产品海报_1938591805661175809.json、图片生成/图生图/KonText一句话改双图，技术有限，创意无限！_1948024769821192193.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageResize+`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 12/15 个有
- `MathExpression|pysssss` —— 12/15 个有
- `SaveImage` —— 12/15 个有
- `UNETLoader` —— 12/15 个有
- `PreviewImage` —— 8/15 个有
- `ImageConcanate` —— 6/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/15 个有
- `RMBG` —— 6/15 个有
- `NunchakuFluxDiTLoader` —— 4/15 个有
- `ImpactSwitch` —— 3/15 个有
- `Int` —— 3/15 个有
- `NunchakuFluxLoraLoader` —— 3/15 个有
- `SaveImagePlus` —— 3/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `ImageStitch` —— 1/15 个有
- `LayerUtility: CropByMask V2` —— 1/15 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/15 个有
- `NunchakuTextEncoderLoaderV2` —— 1/15 个有
- `PIP_图像联结` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 15 | 100% |
| 高度 | 1280 | 1280 - 1280 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，15 个样本，取值集中（一致性 100%）
