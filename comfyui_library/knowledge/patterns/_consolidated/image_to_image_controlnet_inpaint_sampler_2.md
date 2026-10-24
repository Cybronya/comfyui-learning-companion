---
name: image_to_image_controlnet_inpaint_sampler_2
type: Image To Image
frequency: 8
level: strong
coverage: 0.842125
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, ImageConcanate, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image InstanX方案2超强一致性扩图V2（支持文字）_1966497493393584130.json, 图片生成/图生图/Qwen Image InstanX方案2超强局部重绘V1（支持文字）_1966505436751015937.json, 图片生成/图生图/Qwen Image InstanX超强局部重绘V1（支持文字）_1966206334339289089.json, 图片生成/图生图/Qwen Image InstanX超强扩图V1（支持文字）_1966211637923540993.json, 图片生成/图生图/Qwen Image 外扩_1969329744925913090.json, 图片生成/图生图/Qwen Image 局部重绘 手动遮罩_1968885539195822082.json, 图片生成/图生图/Qwen-Image-inpaint完美扩图_1966196008294281217.json, 图片生成/图生图/🦖超强局部重绘（支持文字）_1968137236959100929.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image InstanX方案2超强一致性扩图V2（支持文字）_1966497493393584130.json、图片生成/图生图/Qwen Image InstanX方案2超强局部重绘V1（支持文字）_1966505436751015937.json、图片生成/图生图/Qwen Image InstanX超强局部重绘V1（支持文字）_1966206334339289089.json、图片生成/图生图/Qwen Image InstanX超强扩图V1（支持文字）_1966211637923540993.json、图片生成/图生图/Qwen Image 外扩_1969329744925913090.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `GrowMaskWithBlur` —— 5/8 个有
- `ImageAndMaskPreview` —— 5/8 个有
- `ImagePadForOutpaint` —— 5/8 个有
- `InpaintPreprocessor` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `PDIMAGE_LongerSize` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `SetLatentNoiseMask` —— 5/8 个有
- `CFGNorm` —— 2/8 个有
- `GetImageSize` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `SolidMask` —— 2/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `LayerMask: MaskPreview` —— 1/8 个有
- `LayerUtility: ImageBlend V2` —— 1/8 个有
- `MaskPreview` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 79% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 8 | 79% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
