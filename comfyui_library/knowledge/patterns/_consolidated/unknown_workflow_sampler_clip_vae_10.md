---
name: unknown_workflow_sampler_clip_vae_10
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.915571
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2图像编辑上线_1994235957700476930.json, 图片生成/图生图/Flux2图生图工作流_1954841342910316546.json, 图片生成/图生图/Flux2最新图像多图编辑（支持中文的flux）_1993556016021389313.json, 图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json, 图片生成/图生图/flux2-dev-fp8-mixed 双图编辑_2008366363550687234.json, 图片生成/图生图/flux2-dev-fp8-mixed 多图编辑_2008381017370923010.json, 图片生成/图生图/【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121.json, 图片生成/图生图/🦖Flux2DEV多图编辑_2007631030517239810.json, 图片生成/文生图/3D人物编辑器应用系列之二——FLUX-2-klein-9B文生图_2020299327251423234.json, 图片生成/文生图/FLUX-2-klein-9B_动作精准设计之二工作流_2016865671568691202.json, 图片生成/文生图/FLUX-2-klein-9b_动作精准设计之一工作流_2013405319954702338.json, 图片生成/文生图/FLUX2 混合模型_1993527380123860994.json, 图片生成/文生图/Flux2-TurboV2加速_2007448172402057217.json, "视频生成/文生视频/谁与争锋 Flux2 Z-image,  多图编辑 挑战 Qwen Edit_1994227326332370945.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Flux2图像编辑上线_1994235957700476930.json、图片生成/图生图/Flux2图生图工作流_1954841342910316546.json、图片生成/图生图/Flux2最新图像多图编辑（支持中文的flux）_1993556016021389313.json、图片生成/图生图/Y-FLUX.2 Klein 9B 单图编辑_2012793735624527873.json、图片生成/图生图/flux2-dev-fp8-mixed 双图编辑_2008366363550687234.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `ImageConcanate` —— 3/14 个有
- `LoraLoaderModelOnly` —— 3/14 个有
- `easy int` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `EmptySD3LatentImage` —— 1/14 个有
- `GetImageSize+` —— 1/14 个有
- `Int Literal` —— 1/14 个有
- `PathchSageAttentionKJ` —— 1/14 个有
- `Text Multiline` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
