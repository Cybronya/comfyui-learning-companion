---
name: image_to_image_controlnet_inpaint_lora_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.5075
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, GetNode, Image Comparer (rgthree), ImageAndMaskPreview, ImagePadForOutpaint, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-inpaint扩图 多种模式可选_1966324763754999809.json, 图片生成/图生图/Qwen自由尺寸扩图_1998211983528878082.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-inpaint扩图 多种模式可选_1966324763754999809.json、图片生成/图生图/Qwen自由尺寸扩图_1998211983528878082.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImagePadForOutpaint`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: RestoreCropBox` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
