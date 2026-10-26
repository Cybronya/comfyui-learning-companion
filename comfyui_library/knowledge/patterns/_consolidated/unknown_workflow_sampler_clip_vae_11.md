---
name: unknown_workflow_sampler_clip_vae_11
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.924
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3D模型材质贴图渲染_2047283420904034306.json, 图片生成/图生图/4.【Flux.2】 Klein_单图像编辑_2014321298746380290.json, 图片生成/图生图/9-12-亚克力金属-有钱包LORA优化质感，纹路，光感，清晰度_2098815251805458433.json, 图片生成/图生图/9-12-亚克力金属-有钱包LORA优化质感，纹路，光感，清晰度_2098820008020373506.json, 图片生成/图生图/9_9-皮带纹路优化-有钱包LORA优化质感，纹路，光感，清晰度_2097358992443006978.json, 图片生成/图生图/FLUX2-Klein图像放大_2044694517214879745.json, "图片生成/图生图/Flux-2 Klein：秒换新生,_2013256781648109570.json", 图片生成/图生图/Flux2 Klein-产品精修_2016028233266892801.json, 图片生成/图生图/Klein 9B Ture商业级光影融合工作流 零偏移_2047233928045531137.json, 图片生成/图生图/Klein 产品精修2.0_2036776123027169281.json, 图片生成/图生图/Klein-模糊变清晰 + 一致性图像细化+编辑_2054578992128241666.json, 图片生成/图生图/Klein_动漫高清放大_超分放大_2052188511582867458.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/3D模型材质贴图渲染_2047283420904034306.json、图片生成/图生图/4.【Flux.2】 Klein_单图像编辑_2014321298746380290.json、图片生成/图生图/9-12-亚克力金属-有钱包LORA优化质感，纹路，光感，清晰度_2098815251805458433.json、图片生成/图生图/9-12-亚克力金属-有钱包LORA优化质感，纹路，光感，清晰度_2098820008020373506.json、图片生成/图生图/9_9-皮带纹路优化-有钱包LORA优化质感，纹路，光感，清晰度_2097358992443006978.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
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
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/12 个有
- `UNETLoader` —— 11/12 个有
- `Image Comparer (rgthree)` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `LayerUtility: PurgeVRAM V2` —— 7/12 个有
- `Seed (rgthree)` —— 7/12 个有
- `CR Text` —— 6/12 个有
- `ImageSmartSharpen+` —— 6/12 个有
- `ImpactSwitch` —— 6/12 个有
- `ShowText` —— 6/12 个有
- `Text` —— 6/12 个有
- `TextCombinerTwo` —— 6/12 个有
- `easy imageColorMatch` —— 6/12 个有
- `easy int` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 5/12 个有
- `GetImageSize` —— 3/12 个有
- `CR Text Input Switch (4 way)` —— 1/12 个有
- `Get resolution [Crystools]` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `PrimitiveString` —— 1/12 个有
- `StringConcatenate` —— 1/12 个有
- `UnetLoaderGGUF` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
