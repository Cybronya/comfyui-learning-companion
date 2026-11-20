---
name: unknown_workflow_sampler_clip_unet_83
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.960615
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/材质迁移工作流：两次同时（目前最强）_2106755242196037633.json, 图片生成/图生图/炉石卡通转换_2093517690102181890.json, 图片生成/图生图/预测女儿长相_2046549583253213186.json, 图片生成/图生图/👾怪獸-Flux2Klein 去水印马赛克👾_2047809913426022401.json, 平台全量/KIein 9B Base 4k高清放大+增强细节_2030987361521242113.json, 平台全量/KIein 9B Base 产品精修_2041322038987591682.json, 平台全量/KIein 9B Base 人像精修_2043141656685318146.json, 平台全量/KIein 9B Base人物融图_2051132852267429890.json, 平台全量/Klein 9B Base 肌肤细节增强_2027294504553816066.json, 平台全量/klein 9B 增强皮肤细节_2025111356504018946.json, 平台全量/klein产品材质替换_2021066492002967554.json, 平台全量/【阡陌】FLUX-2-Klein 9B 蒸馏版4步单图编辑工作流_2016512839728504833.json, 平台全量/产品精修+高清放大V1.0_2064740555518726146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_83

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/材质迁移工作流：两次同时（目前最强）_2106755242196037633.json、图片生成/图生图/炉石卡通转换_2093517690102181890.json、图片生成/图生图/预测女儿长相_2046549583253213186.json、图片生成/图生图/👾怪獸-Flux2Klein 去水印马赛克👾_2047809913426022401.json、平台全量/KIein 9B Base 4k高清放大+增强细节_2030987361521242113.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
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
- `LoraLoaderModelOnly` —— 9/13 个有
- `Image Comparer (rgthree)` —— 7/13 个有
- `ImageUpscaleWithModel` —— 2/13 个有
- `LayerUtility: PurgeVRAM V2` —— 2/13 个有
- `UpscaleModelLoader` —— 2/13 个有
- `ttN text` —— 2/13 个有
- `FancyNoteNode` —— 1/13 个有
- `ImageBatch` —— 1/13 个有
- `ImageBlend` —— 1/13 个有
- `ImageGrid` —— 1/13 个有
- `ImageSharpen` —— 1/13 个有
- `MuyeSizeSelector` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
