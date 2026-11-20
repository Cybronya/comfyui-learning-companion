---
name: unknown_workflow_lora_sampler_unet_311
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8935
common_nodes: [CLIPLoader, EmptyFlux2LatentImage, Image Comparer (rgthree), Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SkipLayerGuidanceDiTSimple, TextEncodeMOSSImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Moss Image SFT 图像编辑｜裁剪贴回｜零位移｜无偏色_2115699649809051649.json, 平台全量/Moss-image-动漫转真人_2117230096191934465.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_311

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Moss Image SFT 图像编辑｜裁剪贴回｜零位移｜无偏色_2115699649809051649.json、平台全量/Moss-image-动漫转真人_2117230096191934465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `TextEncodeMOSSImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `InpaintCropImproved` —— 1/2 个有
- `InpaintStitchImproved` —— 1/2 个有
- `MaskFillHoles` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `TextGenerate` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
