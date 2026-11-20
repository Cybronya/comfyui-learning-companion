---
name: unknown_workflow_inpaint_sampler_clip_74
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8185
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetNode, Image Comparer (rgthree), InpaintCropImproved, InpaintStitchImproved, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux2 Klein 万物移除｜局部重绘｜零位移｜零色差｜PS扩图_2112166688010625027.json, 平台全量/Flux2 Klein 强力消除_局部重绘_无损扩图 _ 告别色差位移_2112373965128818689.json, 平台全量/工作流系列04-超大图片的局部编辑-基于CropAndStitch节点组+Klein实现_2042129898801733634.json, 平台全量/工作流系列05-超大图片的局部替换-基于CropAndStitch节点组+Klein实现_2042562772151574529.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Flux2 Klein 万物移除｜局部重绘｜零位移｜零色差｜PS扩图_2112166688010625027.json、平台全量/Flux2 Klein 强力消除_局部重绘_无损扩图 _ 告别色差位移_2112373965128818689.json、平台全量/工作流系列04-超大图片的局部编辑-基于CropAndStitch节点组+Klein实现_2042129898801733634.json、平台全量/工作流系列05-超大图片的局部替换-基于CropAndStitch节点组+Klein实现_2042562772151574529.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GetNode`
- `Image Comparer (rgthree)`
- `InpaintCropImproved`
- `InpaintStitchImproved`
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

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/4 个有
- `CR Text Replace` —— 2/4 个有
- `DF_Get_image_size` —— 2/4 个有
- `DrawMaskOnImage` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `Int` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MaskFillHoles` —— 2/4 个有
- `MuyeTextEditOutput` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `Seed (rgthree)` —— 2/4 个有
- `Text` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
