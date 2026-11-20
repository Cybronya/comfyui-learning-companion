---
name: unknown_workflow_sampler_clip_unet_193
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.881429
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/klein 局部重绘+全节点注释_2061408975094112257.json, 图片生成/图生图/klein溶图打光_2110918582837272578.json, 图片生成/图生图/全屋定制-2-衣柜材质更改-PS_2059839460128411649.json, 图片生成/图生图/材质纹理迁移_最新klein工作流_2032735984915320833.json, 图片生成/图生图/材质纹理迁移_最新klein工作流_2097884372610404353.json, 图片生成/图生图/材质纹理迁移_最新klein工作流_2099412832235380737.json, 图片生成/文生图/F.2klein9b自动溶图打光一致性_2058899052313530370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_193

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/klein 局部重绘+全节点注释_2061408975094112257.json、图片生成/图生图/klein溶图打光_2110918582837272578.json、图片生成/图生图/全屋定制-2-衣柜材质更改-PS_2059839460128411649.json、图片生成/图生图/材质纹理迁移_最新klein工作流_2032735984915320833.json、图片生成/图生图/材质纹理迁移_最新klein工作流_2097884372610404353.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `easy positive` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `Mask Fill Holes` —— 3/7 个有
- `MaskPreview` —— 3/7 个有
- `SetLatentNoiseMask` —— 3/7 个有
- `Int` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `INPAINT_ExpandMask` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有
- `LayerColor: Brightness & Contrast` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RepeatLatentBatch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
