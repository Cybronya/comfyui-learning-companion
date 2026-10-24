---
name: unknown_workflow_sampler_clip_unet_9
type: Unknown Workflow
frequency: 34
level: moderate
coverage: 0.928147
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageSharpen, KSamplerAdvanced, KSamplerSelect, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2三采-全自动文生图全模式_2074751859335716866.json, 图片生成/图生图/Krea2三采流-全自动风格迁移_2084535557341925377.json, 图片生成/图生图/Krea2三采流-全自动风格迁移_2084649386075836418.json, 图片生成/图生图/Krea2三采流-全自动风格迁移_2087389392309669889.json, 图片生成/图生图/Krea2三采流-全自动风格迁移_2091713906174676994.json, 图片生成/图生图/Krea2三采流-全自动风格迁移_2091845053529542658.json, 图片生成/图生图/Krea2三采流-全自动风格迁移_2092616031020871682.json, 图片生成/图生图/Krea2三采流-风格迁移_2070346463154098178.json, 图片生成/文生图/2030590276292583426.json, 图片生成/文生图/Dark Deco 暗黑装饰艺术 三采工作流（无反推模板）_2081052417982033921.json, 图片生成/文生图/Dark Deco 暗黑装饰艺术 全自动三采工作流_2081041992469012482.json, 图片生成/文生图/Krea2 双采样+Flux.2 Klein高清放大-自动提示词改写文生图_2071886759901884418.json, 图片生成/文生图/Krea2-文生图全模式_2074293554280751106.json, 图片生成/文生图/Krea2-文生图全自动风格迁移_2074293504108490754.json, 图片生成/文生图/Krea2三采-全自动文生图_2075218791964962818.json, 图片生成/文生图/Krea2三采-全自动文生图_2079754578903523329.json, 图片生成/文生图/Krea2三采-全自动文生图_2090250296709705730.json, 图片生成/文生图/Krea2三采-全自动文生图_2090254777090400258.json, 图片生成/文生图/Krea2三采-全自动文生图_2090303123905662977.json, 图片生成/文生图/Krea2三采-全自动文生图全模式_2071985841202880514.json, 图片生成/文生图/Krea2三采-文生图全模式_2089265262427205633.json, 图片生成/文生图/Krea2三采文生图_2076913794516869122.json, 图片生成/文生图/Krea2三采流-全自动文生图_2070323178886492161.json, 图片生成/文生图/Krea2三采流-全自动文生图全模式_2070098937662496769.json, 图片生成/文生图/Krea2三采流-全自动文生图全模式_2070336281514692609.json, 图片生成/文生图/Krea2三采流-全自动文生图全模式_2071434528807280641.json, 图片生成/文生图/Krea2三采流-全自动风格迁移_2070148898408198146.json, 图片生成/文生图/Krea2三采流-全自动风格迁移_2070376782905298945.json, 图片生成/文生图/Krea2三采流-全自动风格迁移_2082656076536836098.json, 图片生成/文生图/Krea2双采流+高清放大-全自动提示词文生图_2071838011926605825.json, 图片生成/文生图/Krea2文生图_三采_2074852704572239873.json, 图片生成/文生图/Krea2文生图美学感_风格化_2074430949265330178.json, 图片生成/文生图/Z image双采生图+Klein修复_2047201445694410754.json, 图片生成/文生图/全自动文生图Krea2_2101530861849104385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（图片生成/图生图/Krea2三采-全自动文生图全模式_2074751859335716866.json、图片生成/图生图/Krea2三采流-全自动风格迁移_2084535557341925377.json、图片生成/图生图/Krea2三采流-全自动风格迁移_2084649386075836418.json、图片生成/图生图/Krea2三采流-全自动风格迁移_2087389392309669889.json、图片生成/图生图/Krea2三采流-全自动风格迁移_2091713906174676994.json…）

- **类型**：Unknown Workflow
- **样本数**：34
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 34 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageSharpen`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 33/34 个有
- `ImageScaleToTotalPixels` —— 33/34 个有
- `INTConstant` —— 31/34 个有
- `CR Prompt Text` —— 30/34 个有
- `llama_cpp_instruct_adv` —— 30/34 个有
- `llama_cpp_model_loader` —— 30/34 个有
- `llama_cpp_parameters` —— 30/34 个有
- `Int` —— 29/34 个有
- `PreviewAny` —— 29/34 个有
- `PreviewImage` —— 29/34 个有
- `LoadImage` —— 14/34 个有
- `LoraLoaderModelOnly` —— 4/34 个有
- `Image Comparer (rgthree)` —— 3/34 个有
- `RH_LLMAPI_Pro_Node` —— 3/34 个有
- `easy showAnything` —— 3/34 个有
- `GetNode` —— 2/34 个有
- `PrimitiveStringMultiline` —— 2/34 个有
- `SetNode` —— 2/34 个有
- `TTResolutionSelector` —— 2/34 个有
- `CLIPLoaderGGUF` —— 1/34 个有
- `EmptySD3LatentImage` —— 1/34 个有
- `Label (rgthree)` —— 1/34 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/34 个有
- `easy saveText` —— 1/34 个有
- `孤海注释` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 33 | 88% |
| 高度 | 1536 | 512 - 1536 | 33 | 83% |
| 采样步数 | randomize | - | 34 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 12 | 34 | 33% |
| 采样算法 | 2 | 1 - 2 | 34 | 81% |
| 调度器 | euler | - | 34 | 97% |
| 重绘幅度 | simple | - | 34 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，33 个样本，取值集中（一致性 88%）
- 高度 中位数 1536，观测区间 512 - 1536，33 个样本，取值集中（一致性 83%）
- 采样步数 最常用 randomize，34 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 12，34 个样本，取值分散，一致性仅 33%
- 采样算法 中位数 2，观测区间 1 - 2，34 个样本，取值集中（一致性 81%）
- 调度器 最常用 euler，34 个样本，一致性 97%
- 重绘幅度 最常用 simple，34 个样本，一致性 100%
