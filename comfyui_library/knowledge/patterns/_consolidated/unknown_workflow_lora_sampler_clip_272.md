---
name: unknown_workflow_lora_sampler_clip_272
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.771
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Input Switch, CheckpointLoaderSimple, ConditioningZeroOut, FluxGuidance, GetImageSize, GetNode, Image Comparer (rgthree), ImageScale, ImageScaleToTotalPixels, KSamplerAdvanced, LanPaint_KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview, PrimitiveFloat, ReferenceLatent, ResizeImageMaskNode, SaveImage, SetLatentNoiseMask, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kinghere-klein局部重绘+改图+面部精修+抠图v3_2041831795703943169.json, 图片生成/图生图/kinghere-klein局部重绘+改图+面部精修v2_2041460608687673346.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_272

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/kinghere-klein局部重绘+改图+面部精修+抠图v3_2041831795703943169.json、图片生成/图生图/kinghere-klein局部重绘+改图+面部精修v2_2041460608687673346.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Input Switch`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `LanPaint_KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `PrimitiveFloat`
- `ReferenceLatent`
- `ResizeImageMaskNode`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
