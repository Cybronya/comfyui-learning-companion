---
name: unknown_workflow_upscale_latent_upscale_sampler_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.736
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JjkText, KSampler, LatentUpscaleBy, PreviewAny, PreviewImage, PrimitiveStringMultiline, QwenImageLatentAspectRatio, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, StringReplace, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/极速文生图 百度图片 Ernie_turbo_2045388211031121921.json, 图片生成/文生图/极速文生图 百度图片 Ernie_turbo_2045403077443850241.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/极速文生图 百度图片 Ernie_turbo_2045388211031121921.json、图片生成/文生图/极速文生图 百度图片 Ernie_turbo_2045403077443850241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LatentUpscaleBy`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImageLatentAspectRatio`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `StringReplace`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 1/2 个有
- `Switch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
