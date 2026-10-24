---
name: unknown_workflow_sampler_clip_unet_205
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.666667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-Klein-9b图像编辑(支持扩图，图片编辑，高清放大，局部重绘) 阿贵_2035301463336951810.json, 图片生成/图生图/FLUX2-Klein-9b图像编辑(支持扩图，图片编辑，高清放大，局部重绘)_阿贵_2089728958869889026.json, 图片生成/图生图/FLUX2-Klein-9b图像编辑(支持扩图，图片编辑，高清放大，局部重绘)_阿贵_2089729449523769346.json, 图片生成/图生图/Flux2 Klein  动漫转真实照片 增强细节_2110543060793913345.json, 图片生成/图生图/Flux2-Klein 多图编辑版：通用版_2093566736946786306.json, 图片生成/文生图/Flux2 Klein 9B 文生图_单图_双图编辑 工作流合集_2012152763832082434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_205

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein-9b图像编辑(支持扩图，图片编辑，高清放大，局部重绘) 阿贵_2035301463336951810.json、图片生成/图生图/FLUX2-Klein-9b图像编辑(支持扩图，图片编辑，高清放大，局部重绘)_阿贵_2089728958869889026.json、图片生成/图生图/FLUX2-Klein-9b图像编辑(支持扩图，图片编辑，高清放大，局部重绘)_阿贵_2089729449523769346.json、图片生成/图生图/Flux2 Klein  动漫转真实照片 增强细节_2110543060793913345.json、图片生成/图生图/Flux2-Klein 多图编辑版：通用版_2093566736946786306.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `Any Switch (rgthree)` —— 4/6 个有
- `Int` —— 4/6 个有
- `MuyeTextEditOutput` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `DapaoImagePadDirectionNode` —— 3/6 个有
- `EmptyFlux2LatentImage` —— 3/6 个有
- `ImageCompositorNode` —— 3/6 个有
- `LayerUtility: ColorImage` —— 3/6 个有
- `MaskFillHoles` —— 3/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `Anything Everywhere` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `ColorMatch` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `Float` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `easy conditioningIndexSwitch` —— 1/6 个有
- `easy imageIndexSwitch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
