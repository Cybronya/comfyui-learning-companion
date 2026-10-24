---
name: image_to_image_controlnet_inpaint_lora_16
type: Image To Image
frequency: 2
level: weak
coverage: 0.746
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, Cut By Mask, GrowMask, Image Comparer (rgthree), ImageRemoveAlpha+, ImageScaleToMaxDimension, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingAuraFlow, Paste By Mask, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN局部高清重绘_1986388231803596801.json, 图片生成/图生图/神都猫高清图片千问局部修改还是高清_1986368129397882881.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QWEN局部高清重绘_1986388231803596801.json、图片生成/图生图/神都猫高清图片千问局部修改还是高清_1986368129397882881.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `Cut By Mask`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageRemoveAlpha+`
- `ImageScaleToMaxDimension`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `Paste By Mask`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `2a4b2cc0-db37-4302-a067-da392f38f06b` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `f93c215e-c393-460e-9534-ed2c3d8a652e` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
