---
name: unknown_workflow_sampler_clip_unet_357
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.865333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImagePadForOutpaint, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/多多安全区banner_2079455432715890690.json, 图片生成/图生图/扩图-Flux2-klein-模板_2050109267771961345.json, 图片生成/图生图/扩图-自定义尺寸_klein极速版_2027967998400663553.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_357

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多多安全区banner_2079455432715890690.json、图片生成/图生图/扩图-Flux2-klein-模板_2050109267771961345.json、图片生成/图生图/扩图-自定义尺寸_klein极速版_2027967998400663553.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImagePadForOutpaint`
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
- `SetNode` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/3 个有
- `easy seed` —— 1/3 个有
- `图像缩放V2_孤海` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
