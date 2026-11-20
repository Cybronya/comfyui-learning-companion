---
name: unknown_workflow_sampler_clip_unet_411
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.871667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein图像风格互转_真人转动漫风格_动漫风格转真人_2054440839576866818.json, 图片生成/图生图/一致性换脸工作流_2043924693551423490.json, 平台全量/节点系列26-If else节点_2044225440247713794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_411

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/klein图像风格互转_真人转动漫风格_动漫风格转真人_2054440839576866818.json、图片生成/图生图/一致性换脸工作流_2043924693551423490.json、平台全量/节点系列26-If else节点_2044225440247713794.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `Int` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `HAIGC_LoadImagesFromZip` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Model Input Switch` —— 1/3 个有
- `ModelPatchLoader` —— 1/3 个有
- `QwenImageDiffsynthControlnet` —— 1/3 个有
- `RH_BatchImages` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
