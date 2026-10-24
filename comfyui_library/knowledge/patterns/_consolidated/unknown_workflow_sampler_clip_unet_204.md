---
name: unknown_workflow_sampler_clip_unet_204
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.919
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, INTConstant, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-Klein _ 一致性｜九宫格｜自定义角度 _ 一键出图_2022376852790190082.json, 图片生成/图生图/FLUX2-Klein-9b图像编辑_2033421207898431489.json, 图片生成/图生图/FLUX2-Klein一致性分镜生成_2067832036592807938.json, 图片生成/图生图/Flux2_Klein9B_无限分镜工作流_2067621889706643458.json, 图片生成/图生图/WH-AI-Studio超强FLUX2-Klein单图语义修改器_2053315100181835777.json, 图片生成/图生图/WH-AI-Studio（超强FLUX2-Klein单图语义修改器）_2026674751833378817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_204

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein _ 一致性｜九宫格｜自定义角度 _ 一键出图_2022376852790190082.json、图片生成/图生图/FLUX2-Klein-9b图像编辑_2033421207898431489.json、图片生成/图生图/FLUX2-Klein一致性分镜生成_2067832036592807938.json、图片生成/图生图/Flux2_Klein9B_无限分镜工作流_2067621889706643458.json、图片生成/图生图/WH-AI-Studio超强FLUX2-Klein单图语义修改器_2053315100181835777.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `INTConstant`
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
- `PreviewImage` —— 4/6 个有
- `ImageConcanate` —— 2/6 个有
- `Int` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `easy promptLine` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Getter` —— 1/6 个有
- `HAIGC_SaveImagesToZip` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageGetter` —— 1/6 个有
- `KepStringList` —— 1/6 个有
- `Kep_JoinListAny` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `Setter` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextImage` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
