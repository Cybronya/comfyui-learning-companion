---
name: unknown_workflow_sampler_clip_unet_36
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.92025
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/文生图/1926661482686353410.json, 图片生成/文生图/1933332658841628674.json, 图片生成/文生图/1986239618842578945.json, 图片生成/文生图/3D人物编辑器应用系列之二——FLUX-2-klein-9B文生图_2020299327251423234.json, 图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json, 图片生成/文生图/FLUX-2-klein-9B_动作精准设计之二工作流_2016865671568691202.json, 图片生成/文生图/FLUX-2-klein-9b_动作精准设计之一工作流_2013405319954702338.json, 图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json, 图片生成/文生图/FLUX2 混合模型_1993527380123860994.json, 图片生成/文生图/FLUX2-多参考一致性创意场景合成_2090769208387923969.json, 图片生成/文生图/FLux2-用嘴改图_2081949979949748226.json, 图片生成/文生图/Flux.2双图编辑_1993607256262508545.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1926661482686353410.json、图片生成/文生图/1933332658841628674.json、图片生成/文生图/1986239618842578945.json、图片生成/文生图/3D人物编辑器应用系列之二——FLUX-2-klein-9B文生图_2020299327251423234.json、图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 11/12 个有
- `FluxGuidance` —— 11/12 个有
- `ReferenceLatent` —— 11/12 个有
- `LoadImage` —— 10/12 个有
- `VAEEncode` —— 10/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `ImpactInt` —— 2/12 个有
- `Int` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `LoraLoaderModelOnly` —— 2/12 个有
- `GetImageSize` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `RH_Translator` —— 1/12 个有
- `TTResolutionSelector` —— 1/12 个有
- `TextInput_` —— 1/12 个有
- `easy positive` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
