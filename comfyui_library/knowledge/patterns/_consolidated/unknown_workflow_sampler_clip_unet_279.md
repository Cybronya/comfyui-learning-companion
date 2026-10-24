---
name: unknown_workflow_sampler_clip_unet_279
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9185
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein Euler_2034106354624897025.json, 图片生成/图生图/Flux2_Klein-PS扩图_无需参数白色填充_2087356447444258818.json, 图片生成/图生图/PS扩图 无需参数（个人原创）_2039171118006804482.json, 图片生成/图生图/设计工作流——鸟瞰设计_2018294277486419969.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_279

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein Euler_2034106354624897025.json、图片生成/图生图/Flux2_Klein-PS扩图_无需参数白色填充_2087356447444258818.json、图片生成/图生图/PS扩图 无需参数（个人原创）_2039171118006804482.json、图片生成/图生图/设计工作流——鸟瞰设计_2018294277486419969.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
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
- `AILab_QwenVL_Advanced` —— 2/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `InspyrenetRembg` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `CR Simple Text Watermark` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_RhartImageG2ImageToImage` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `scale` —— 1/4 个有
- `text_mul_Join` —— 1/4 个有
- `text_mul_remove` —— 1/4 个有
- `text_mul_replace` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
