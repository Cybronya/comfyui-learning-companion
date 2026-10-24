---
name: unknown_workflow_sampler_clip_unet_212
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8915
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-2-klein图像编辑_2013562172701413377.json, 图片生成/图生图/flux2 klein 9B极速换脸，0像素偏移，最快4步出图。_2013267509121654786.json, 图片生成/图生图/flux2klein4b内衣虚拟试衣低显存_2060710585700012034.json, 图片生成/图生图/flux2klein4b内衣试衣快速版_2062130665725980673.json, 图片生成/图生图/换脸工作流111_2081385261786812418.json, 图片生成/文生图/Bfs Klein人物换脸V1_2019423087078412290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_212

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/flux-2-klein图像编辑_2013562172701413377.json、图片生成/图生图/flux2 klein 9B极速换脸，0像素偏移，最快4步出图。_2013267509121654786.json、图片生成/图生图/flux2klein4b内衣虚拟试衣低显存_2060710585700012034.json、图片生成/图生图/flux2klein4b内衣试衣快速版_2062130665725980673.json、图片生成/图生图/换脸工作流111_2081385261786812418.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `ImageStitch` —— 3/6 个有
- `DifferentialDiffusion` —— 2/6 个有
- `ImageConcanate` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `easy ifElse` —— 2/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `ImageCropByMask` —— 1/6 个有
- `Int` —— 1/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `Resize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
