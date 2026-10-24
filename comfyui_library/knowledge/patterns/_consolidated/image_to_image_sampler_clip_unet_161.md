---
name: image_to_image_sampler_clip_unet_161
type: Image To Image
frequency: 2
level: weak
coverage: 0.878
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Kontext人像换指定背景，稳定高效_1943705110461448193.json, 图片生成/图生图/kontext重打光高清光影工作流_1957997566740803586.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_161

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Kontext人像换指定背景，稳定高效_1943705110461448193.json、图片生成/图生图/kontext重打光高清光影工作流_1957997566740803586.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.9 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
