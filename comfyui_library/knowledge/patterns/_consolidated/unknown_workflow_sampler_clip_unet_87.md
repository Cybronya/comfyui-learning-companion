---
name: unknown_workflow_sampler_clip_unet_87
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.838286
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [YC Color Match, CR Text, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2]
members: [comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json, 图片生成/图生图/2016848786680713218.json, 图片生成/图生图/2053519932205355010.json, 图片生成/图生图/2056398938592342018.json, 图片生成/图生图/2056400490073780225.json, 图片生成/图生图/2068673231879491585.json, 图片生成/文生图/产品抠图透明背景精修版+全节点注释_2090760561532424194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json、图片生成/图生图/2016848786680713218.json、图片生成/图生图/2053519932205355010.json、图片生成/图生图/2056398938592342018.json、图片生成/图生图/2056400490073780225.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 6/7 个有
- `VAEEncode` —— 6/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `YC Color Match` —— 2/7 个有
- `27eacb9f-0da2-421d-a0bf-b4b4e5fe5709` —— 1/7 个有
- `93041a64-452a-477a-9447-40330b7c1136` —— 1/7 个有
- `FluxKVCache` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LayerMask: BiRefNetUltra` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：YC Color Match、CR Text、Label (rgthree)、LayerUtility: ImageScaleByAspectRatio V2
