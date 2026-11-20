---
name: unknown_workflow_sampler_clip_unet_132
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9102
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/Flux2-klein-美甲迁移_2029843703233257474.json, 图片生成/图生图/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2025741951122808834.json, 图片生成/图生图/电商产品FLUX2精修_2094400191687385090.json, 图片生成/图生图/电商产品FLUX2精修_2096169386120925186.json, 图片生成/图生图/电商产品FLUX2精修_2096403269538115586.json, 平台全量/Flux2-klein-美甲迁移-美甲模特_2019613787933904897.json, 平台全量/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2019666920051580929.json, 平台全量/flux2-klein-发型迁移-假发模特_2015394972240977922.json, 平台全量/万物迁移 妆容迁移 美妆模特 Flux2-klein 美甲迁移 美甲模特_2025036225937154050.json, 平台全量/万能发型迁移 Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2019939474045669377.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux2-klein-美甲迁移_2029843703233257474.json、图片生成/图生图/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2025741951122808834.json、图片生成/图生图/电商产品FLUX2精修_2094400191687385090.json、图片生成/图生图/电商产品FLUX2精修_2096169386120925186.json、图片生成/图生图/电商产品FLUX2精修_2096403269538115586.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImpactMakeAnyList` —— 7/10 个有
- `Text Multiline` —— 7/10 个有
- `easy compare` —— 7/10 个有
- `easy ifElse` —— 7/10 个有
- `easy imageSizeBySide` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `AILab_QwenVL` —— 3/10 个有
- `FluxGuidance` —— 3/10 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `SeedVR2LoadDiTModel` —— 3/10 个有
- `SeedVR2LoadVAEModel` —— 3/10 个有
- `SeedVR2VideoUpscaler` —— 3/10 个有
- `easy imageConcat` —— 3/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
