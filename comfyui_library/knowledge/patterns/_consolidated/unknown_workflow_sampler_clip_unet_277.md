---
name: unknown_workflow_sampler_clip_unet_277
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.919667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Klein 9B 老照片修复+上色，一键生成_2030087735737851905.json, 平台全量/MumsAIGC-克莱因高清修复_2078337944464740353.json, 平台全量/Shoe buckle replacement_2041373347388334081.json, 平台全量/flux 抠图换背景 本地_云端都可跑  适用于 虚拟主播换场景 和 实体店引流_2055625665218654209.json, 平台全量/人像修复_2070767495530762241.json, 平台全量/电商白底图 flux2 本地云端都可跑_2055328141203263489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_277

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Klein 9B 老照片修复+上色，一键生成_2030087735737851905.json、平台全量/MumsAIGC-克莱因高清修复_2078337944464740353.json、平台全量/Shoe buckle replacement_2041373347388334081.json、平台全量/flux 抠图换背景 本地_云端都可跑  适用于 虚拟主播换场景 和 实体店引流_2055625665218654209.json、平台全量/人像修复_2070767495530762241.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `GetImageSize` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `ColorMatch` —— 2/6 个有
- `ImageSharpen` —— 2/6 个有
- `LayerMask: BiRefNetUltraV2` —— 2/6 个有
- `LayerMask: LoadBiRefNetModel` —— 2/6 个有
- `DifferentialDiffusion` —— 1/6 个有
- `FastCanvas` —— 1/6 个有
- `FastCanvasTool` —— 1/6 个有
- `LayerUtility: ColorImage V2` —— 1/6 个有
- `LayerUtility: ImageBlendAdvance` —— 1/6 个有
- `MultiTextConcatenate` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
