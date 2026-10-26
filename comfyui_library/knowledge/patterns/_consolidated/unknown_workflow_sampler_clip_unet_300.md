---
name: unknown_workflow_sampler_clip_unet_300
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.854
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-2-klein图像编辑_2013562172701413377.json, 图片生成/图生图/flux2 klein 9B极速换脸，0像素偏移，最快4步出图。_2013267509121654786.json, 图片生成/图生图/flux2klein4b内衣虚拟试衣低显存_2060710585700012034.json, 图片生成/图生图/flux2klein4b内衣试衣快速版_2062130665725980673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_300

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux-2-klein图像编辑_2013562172701413377.json、图片生成/图生图/flux2 klein 9B极速换脸，0像素偏移，最快4步出图。_2013267509121654786.json、图片生成/图生图/flux2klein4b内衣虚拟试衣低显存_2060710585700012034.json、图片生成/图生图/flux2klein4b内衣试衣快速版_2062130665725980673.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImageStitch` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `easy ifElse` —— 2/4 个有
- `Fast Bypasser (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageCropByMask` —— 1/4 个有
- `Int` —— 1/4 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/4 个有
- `RMBG` —— 1/4 个有
- `Resize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
