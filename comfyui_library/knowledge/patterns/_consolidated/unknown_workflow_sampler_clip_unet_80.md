---
name: unknown_workflow_sampler_clip_unet_80
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.939909
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein三视图_2047955676676231169.json, 图片生成/图生图/Flux2-Klein人物角色三视图3D国漫CG风格（图生图）_2090025230700990466.json, 图片生成/图生图/Flux2-klein9B单图+双图编辑工作流_2012386786735034369.json, 图片生成/图生图/Flux2-klein单图+双图编辑_2012711003414339585.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流_2012077133371281410.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流_2012490858884505601.json, 图片生成/图生图/Flux2-klein单图+双图编辑工作流。两张照片，可以单图编辑，也可以双图融合，效果不错，值得推_2032745452604493825.json, 图片生成/图生图/Flux2-klein编辑工作流_2012818467442921473.json, 图片生成/图生图/flux2klein 扩图_2013515335466487809.json, 图片生成/图生图/flux2klein 重绘_2013530157360877570.json, 图片生成/图生图/局部重绘-Flux2-klein-模板_2050108664723320834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein三视图_2047955676676231169.json、图片生成/图生图/Flux2-Klein人物角色三视图3D国漫CG风格（图生图）_2090025230700990466.json、图片生成/图生图/Flux2-klein9B单图+双图编辑工作流_2012386786735034369.json、图片生成/图生图/Flux2-klein单图+双图编辑_2012711003414339585.json、图片生成/图生图/Flux2-klein单图+双图编辑工作流_2012077133371281410.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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
- `EmptyFlux2LatentImage` —— 10/11 个有
- `ConditioningZeroOut` —— 9/11 个有
- `GetImageSize` —— 9/11 个有
- `ImageScaleToTotalPixels` —— 9/11 个有
- `PreviewImage` —— 6/11 个有
- `ColorMatch` —— 3/11 个有
- `Anything Everywhere` —— 2/11 个有
- `DrawMaskOnImage` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `easy imageConcat` —— 2/11 个有
- `CR Text Concatenate` —— 1/11 个有
- `EmptyLatentImage` —— 1/11 个有
- `ImagePadForOutpaintMasked_UTK` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `easy seed` —— 1/11 个有
- `ttN concat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 576 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
