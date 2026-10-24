---
name: unknown_workflow_inpaint_sampler_clip_7
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.876778
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GrowMaskWithBlur, InpaintModelConditioning, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 万物迁移 + 涂抹精确控制大小_2017205500747714561.json, 图片生成/图生图/Flux2 Klein 局部重绘+ 万物迁移_2016435579096928258.json, 图片生成/图生图/Flux2 Klein【局部重绘】_2015209186262523906.json, 图片生成/图生图/Flux2 Klein服装迁移_2018144805066383361.json, 图片生成/图生图/万能图片局部重绘+图片去水印+物品迁移_2054764387465998338.json, 图片生成/图生图/产品设计｜局部修改 + 参考图（可选）｜Flux2 Klein_2052324457221509121.json, 图片生成/图生图/局部重绘+指定物品迁移 Flux2 Klein_2016402322179493889.json, "图片生成/图生图/局部重绘，效果很好，速度很快,Flux2 Klein_2052246216712437761.json", "图片生成/图生图/物体迁移，效果很好，速度很快,Flux2 Klein_2049660145730371585.json"]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 万物迁移 + 涂抹精确控制大小_2017205500747714561.json、图片生成/图生图/Flux2 Klein 局部重绘+ 万物迁移_2016435579096928258.json、图片生成/图生图/Flux2 Klein【局部重绘】_2015209186262523906.json、图片生成/图生图/Flux2 Klein服装迁移_2018144805066383361.json、图片生成/图生图/万能图片局部重绘+图片去水印+物品迁移_2054764387465998338.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
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
- `Image Comparer (rgthree)` —— 8/9 个有
- `MaskPreview+` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `Text` —— 7/9 个有
- `Int` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `ImageResize+` —— 2/9 个有
- `ResizeMask` —— 2/9 个有
- `ZML_MaskStroke` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `ImageScaleToTotalPixelsX` —— 1/9 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `ZML_AnyTypeSwitch` —— 1/9 个有
- `遮罩内外扩展` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
