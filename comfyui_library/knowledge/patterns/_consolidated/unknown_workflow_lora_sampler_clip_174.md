---
name: unknown_workflow_lora_sampler_clip_174
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.919333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein图像风格互转_真人转动漫风格_动漫风格转真人_2054440839576866818.json, 图片生成/图生图/人物换发型_2036784926481190914.json, 图片生成/图生图/净化截图_2059612411639980033.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/klein图像风格互转_真人转动漫风格_动漫风格转真人_2054440839576866818.json、图片生成/图生图/人物换发型_2036784926481190914.json、图片生成/图生图/净化截图_2059612411639980033.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerColor: ColorAdapter` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `FillMaskedArea_UTK` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `Model Input Switch` —— 1/3 个有
- `ModelPatchLoader` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `QwenImageDiffsynthControlnet` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
