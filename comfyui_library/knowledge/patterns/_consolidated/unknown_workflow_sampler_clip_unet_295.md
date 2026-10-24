---
name: unknown_workflow_sampler_clip_unet_295
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94625
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/图生图/材质纹理迁移_最新klein工作流_2032735984915320833.json, 图片生成/图生图/材质纹理迁移_最新klein工作流_2097884372610404353.json, 图片生成/图生图/材质纹理迁移_最新klein工作流_2099412832235380737.json, 图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_295

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/材质纹理迁移_最新klein工作流_2032735984915320833.json、图片生成/图生图/材质纹理迁移_最新klein工作流_2097884372610404353.json、图片生成/图生图/材质纹理迁移_最新klein工作流_2099412832235380737.json、图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
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
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `Mask Fill Holes` —— 3/4 个有
- `MaskPreview` —— 3/4 个有
- `SetLatentNoiseMask` —— 3/4 个有
- `Int` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
