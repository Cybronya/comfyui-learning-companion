---
name: unknown_workflow_sampler_clip_unet_279
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.895833
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/换头换脸 真实自然  Flux2-Klein 极速版_2033408085707984897.json, 平台全量/换脸工作流-BFS-Klein9b_2103031205582168065.json, 平台全量/提取服装精修 Flux2 Klein9b 提取服装精修+服装提取+3D虚拟模特+服装展示+隐形模特+_2021489280987697154.json, 平台全量/最好的换脸流-Klein9b-BFS_2029545923734413313.json, 平台全量/材质类精修【御川0723】_2080153320605442049.json, 平台全量/电商产品精修KLEIN_2032897352041766913.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_279

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/换头换脸 真实自然  Flux2-Klein 极速版_2033408085707984897.json、平台全量/换脸工作流-BFS-Klein9b_2103031205582168065.json、平台全量/提取服装精修 Flux2 Klein9b 提取服装精修+服装提取+3D虚拟模特+服装展示+隐形模特+_2021489280987697154.json、平台全量/最好的换脸流-Klein9b-BFS_2029545923734413313.json、平台全量/材质类精修【御川0723】_2080153320605442049.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
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
- `ImageScaleToTotalPixels` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `easy imageColorMatch` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CR Text Input Switch (4 way)` —— 1/6 个有
- `ConstrainImage|pysssss` —— 1/6 个有
- `LG_Color_Match_V2` —— 1/6 个有
- `SegmentV2` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
