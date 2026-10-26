---
name: unknown_workflow_sampler_clip_unet_189
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.940286
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, ManualSigmas, RandomNoise, ReferenceMultiLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-3-Image-Klein 多图编辑_2110969114528403457.json, 图片生成/图生图/Flux-3-Image-Klein 多图编辑_2111237868306911233.json, 图片生成/图生图/Flux-3平面图转彩平图_2111287781887668226.json, 图片生成/图生图/flux_klien3图像编辑_2110985829039558657.json, 图片生成/图生图/户型平面图转成3D軸测空间框模型图_2111292703928573954.json, 图片生成/图生图/（双图）Flux-3-Image-Klein 多图编辑_2111219534840549378.json, 图片生成/文生图/Flux-3-Image-Klein 多图编辑_2111347095805452290.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_189

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux-3-Image-Klein 多图编辑_2110969114528403457.json、图片生成/图生图/Flux-3-Image-Klein 多图编辑_2111237868306911233.json、图片生成/图生图/Flux-3平面图转彩平图_2111287781887668226.json、图片生成/图生图/flux_klien3图像编辑_2110985829039558657.json、图片生成/图生图/户型平面图转成3D軸测空间框模型图_2111292703928573954.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `ReferenceMultiLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `EmptyLatentImage` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `Latent Switch (JPS)` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `EmptyFlux2LatentImage` —— 4/7 个有
- `ImageConcanate` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RH_RhartImageG2ImageToImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
