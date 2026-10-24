---
name: unknown_workflow_sampler_clip_unet_51
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8766
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/图生图/F.2klein9b一键渲染级材质替换_2054422098839392258.json, 图片生成/图生图/F.2klein9b一键渲染级材质替换_2057678216738992129.json, 图片生成/图生图/F2-Klein材质替换（局部重绘）_2055650299225886722.json, 图片生成/图生图/F2_Klein_服饰_产品材质花纹替换_局部材质替换_电商产品换材质_材质质感迁移_局部重绘_2056197943123816449.json, 图片生成/图生图/F2_Klein_服饰产品花纹替换_局部材质替换_电商产品换材质_材质迁移_局部重绘_2056537368320102402.json, 图片生成/图生图/Klein局部材质替换   比PS香多了_2031606144984158209.json, 图片生成/图生图/Klein局部材质替换_2054740088747241473.json, 图片生成/图生图/Klein局部材质替换_2054841219976572929.json, 图片生成/图生图/Klein局部材质替换_2057331878755131394.json, 图片生成/图生图/flux2-klein9b-一键渲染级材质替换_2037899783381196801.json, 图片生成/图生图/flux2klein9b一键渲染级材质替换_2044351025196306433.json, 图片生成/图生图/klein材质替换，效果好_2054807540877283329.json, 图片生成/图生图/一键局部材质替换（可指定材质）_2059874119453331457.json, 图片生成/图生图/局部材质替换+电商产品换材质+材质质感迁移+F2 Klein准确局部重绘+全节点注释_2055600232863412226.json, 图片生成/图生图/超好用🔥局部重绘-图片内指定物品材质颜色替换_2052688818792353794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_51

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/F.2klein9b一键渲染级材质替换_2054422098839392258.json、图片生成/图生图/F.2klein9b一键渲染级材质替换_2057678216738992129.json、图片生成/图生图/F2-Klein材质替换（局部重绘）_2055650299225886722.json、图片生成/图生图/F2_Klein_服饰_产品材质花纹替换_局部材质替换_电商产品换材质_材质质感迁移_局部重绘_2056197943123816449.json、图片生成/图生图/F2_Klein_服饰产品花纹替换_局部材质替换_电商产品换材质_材质迁移_局部重绘_2056537368320102402.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 14/15 个有
- `Image Comparer (rgthree)` —— 13/15 个有
- `Mask Fill Holes` —— 13/15 个有
- `MaskPreview` —— 13/15 个有
- `easy imageSizeBySide` —— 13/15 个有
- `CR Text` —— 10/15 个有
- `Masks Add` —— 10/15 个有
- `easy sam3ImageSegmentation` —— 10/15 个有
- `easy sam3ModelLoader` —— 10/15 个有
- `AIO_Preprocessor` —— 8/15 个有
- `DeepTranslatorTextNode` —— 8/15 个有
- `easy ifElse` —— 5/15 个有
- `easy isMaskEmpty` —— 5/15 个有
- `Int` —— 4/15 个有
- `SDVN Translate` —— 2/15 个有
- `ImageConcanate` —— 1/15 个有
- `LoraLoaderModelOnly` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
