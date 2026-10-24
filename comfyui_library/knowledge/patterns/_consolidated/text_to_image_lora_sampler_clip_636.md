---
name: text_to_image_lora_sampler_clip_636
type: Text To Image
frequency: 2
level: weak
coverage: 0.806
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, DF_Integer, EmptyLatentImage, Fast Groups Bypasser (rgthree), Get Image Size, Image Compare (mtb), ImageCASharpening+, ImageResize+, ImpactMinMax, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2, SetNode, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/ZIT 尼尔：机械纪元 2B_2062556026267852801.json, 图片生成/文生图/ZIT-甜妹风-软萌女生_2062522059820978177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_636

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/ZIT 尼尔：机械纪元 2B_2062556026267852801.json、图片生成/文生图/ZIT-甜妹风-软萌女生_2062522059820978177.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `DF_Integer`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Get Image Size`
- `Image Compare (mtb)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SetNode`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
