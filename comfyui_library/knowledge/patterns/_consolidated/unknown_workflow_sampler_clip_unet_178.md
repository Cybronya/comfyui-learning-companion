---
name: unknown_workflow_sampler_clip_unet_178
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.936143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2_klein_image_edit_单图_2017799165614497794.json, 图片生成/图生图/Flux2_klein_image_edit_双图_2018351257873813506.json, 图片生成/图生图/Flux2转换角度_2015006159463256065.json, 图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json, 图片生成/图生图/Klein9b-BFS-换脸_2034835916870656002.json, 图片生成/图生图/一键高品质产品精修Klein_2014308186299310082.json, 图片生成/图生图/三图编辑 Flux2-Klein_2012122566953013249.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_178

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux2_klein_image_edit_单图_2017799165614497794.json、图片生成/图生图/Flux2_klein_image_edit_双图_2018351257873813506.json、图片生成/图生图/Flux2转换角度_2015006159463256065.json、图片生成/图生图/Klein9b-BFS 最强换面工作流 V1.0_2040383033378873346.json、图片生成/图生图/Klein9b-BFS-换脸_2034835916870656002.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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
- `EmptyFlux2LatentImage` —— 6/7 个有
- `GetImageSize` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `Number to Float` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `Text` —— 2/7 个有
- `Text Dictionary Get` —— 2/7 个有
- `Text Dictionary New` —— 2/7 个有
- `Text to Number` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `QwenMultiangleCameraNode` —— 1/7 个有
- `RH_Translator` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
