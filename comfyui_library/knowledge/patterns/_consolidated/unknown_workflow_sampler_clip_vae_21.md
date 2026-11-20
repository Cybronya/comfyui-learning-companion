---
name: unknown_workflow_sampler_clip_vae_21
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.932875
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2图像编辑上线_1994235957700476930.json, 图片生成/图生图/Flux2图生图工作流_1954841342910316546.json, 图片生成/图生图/Flux2最新图像多图编辑（支持中文的flux）_1993556016021389313.json, 图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json, 图片生成/图生图/flux2-dev-fp8-mixed 双图编辑_2008366363550687234.json, 图片生成/图生图/flux2-dev-fp8-mixed 多图编辑_2008381017370923010.json, 图片生成/图生图/【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121.json, 图片生成/文生图/Flux2-TurboV2加速_2007448172402057217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2图像编辑上线_1994235957700476930.json、图片生成/图生图/Flux2图生图工作流_1954841342910316546.json、图片生成/图生图/Flux2最新图像多图编辑（支持中文的flux）_1993556016021389313.json、图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json、图片生成/图生图/flux2-dev-fp8-mixed 双图编辑_2008366363550687234.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `easy int` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `GetImageSize+` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `Int Literal` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
