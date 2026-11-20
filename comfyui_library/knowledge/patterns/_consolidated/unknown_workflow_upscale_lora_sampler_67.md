---
name: unknown_workflow_upscale_lora_sampler_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.819333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-Klein 动漫转写实_2018198117404909570.json, 平台全量/KIein 9B Base 4k高清放大细节_2037100544778575873.json, 平台全量/高清放大测试版v1_2075440387845611522.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein 动漫转写实_2018198117404909570.json、平台全量/KIein 9B Base 4k高清放大细节_2037100544778575873.json、平台全量/高清放大测试版v1_2075440387845611522.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `Get resolution [Crystools]` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
