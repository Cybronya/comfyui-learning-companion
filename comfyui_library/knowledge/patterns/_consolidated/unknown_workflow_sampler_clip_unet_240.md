---
name: unknown_workflow_sampler_clip_unet_240
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9518
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein9b-BFS最强换脸 V2版相似度99% 谁用谁知道（记得看说明文件）_2029587665544286209.json, 图片生成/图生图/Klein转线稿_2039620047836024834.json, 图片生成/图生图/Klein转线稿_2060181415077171201.json, 图片生成/图生图/PS专用 klein 9b 扩图_2071036709902569474.json, 图片生成/图生图/klein 9b 顶级扩图工作流_2070692761212375042.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_240

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein9b-BFS最强换脸 V2版相似度99% 谁用谁知道（记得看说明文件）_2029587665544286209.json、图片生成/图生图/Klein转线稿_2039620047836024834.json、图片生成/图生图/Klein转线稿_2060181415077171201.json、图片生成/图生图/PS专用 klein 9b 扩图_2071036709902569474.json、图片生成/图生图/klein 9b 顶级扩图工作流_2070692761212375042.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `ColorMatch` —— 2/5 个有
- `FlexLoraLoaderModelOnly` —— 2/5 个有
- `Float` —— 2/5 个有
- `ImageScale` —— 2/5 个有
- `PixelSnapping` —— 2/5 个有
- `GrowMask` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `ImageToMask` —— 1/5 个有
- `InpaintStitchImproved` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `LayerUtility: ExtendCanvas` —— 1/5 个有
- `Manual XY Entry Info` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `TextBoxMira` —— 1/5 个有
- `YCImageSmartCrop` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
