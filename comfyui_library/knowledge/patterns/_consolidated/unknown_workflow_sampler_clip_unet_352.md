---
name: unknown_workflow_sampler_clip_unet_352
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.951667
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全屋定制-2-衣柜材质更改-PS_2059839460128411649.json, 图片生成/图生图/快速万物消除 擦除 去水印_2102605007383261185.json, 图片生成/文生图/flux2图像修复_2064329697353359361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_352

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全屋定制-2-衣柜材质更改-PS_2059839460128411649.json、图片生成/图生图/快速万物消除 擦除 去水印_2102605007383261185.json、图片生成/文生图/flux2图像修复_2064329697353359361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `BasicGuider` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `InpaintCropImproved` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `InpaintStitchImproved` —— 1/3 个有
- `LayerColor: Brightness & Contrast` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PiDTextPrompt` —— 1/3 个有
- `RepeatLatentBatch` —— 1/3 个有
- `image_scale_pixel_v2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
