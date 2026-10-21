---
name: image_to_image_sampler_clip_unet_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.8395
common_nodes: [AnimaLLLiteApply, CLIPLoader, CLIPTextEncode, ImageCropV2, ImageResizeKJv2, KSampler, LoadImage, MaskPreview, PreviewImage, PrimitiveBoundingBox, PrimitiveStringMultiline, SaveImage, SetLatentNoiseMask, StringReplace, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima Base 参考编辑+局部重绘二合一工作流_2073322505967849474.json, 图片生成/文生图/Anima Base 双图参考_2073322704605896706.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima Base 参考编辑+局部重绘二合一工作流_2073322505967849474.json、图片生成/文生图/Anima Base 双图参考_2073322704605896706.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AnimaLLLiteApply`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageCropV2`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `MaskPreview`
- `PreviewImage`
- `PrimitiveBoundingBox`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetLatentNoiseMask`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_ICLoRAConcat` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.75 | - | 2 | 95% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.75，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
