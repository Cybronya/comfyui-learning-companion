---
name: image_to_image_lora_sampler_clip_163
type: Image To Image
frequency: 2
level: weak
coverage: 0.792
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ColorMatch, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageScaleToTotalPixels, JjkText, KSampler, KSamplerAdvanced, LatentSwitch, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenMultiangleCameraNode, ReferenceLatent, SaveImage, TextCombinerTwo, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptList, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多角度，自由调整，变清晰，色调修正，极速版 multipleangles_2009957796439134210.json, "图片生成/图生图/最强多视角，任意角度，任意优化，变清晰，色调修正, 滑动柯基版。multiangles_2009962056258166785.json"]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_163

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/多角度，自由调整，变清晰，色调修正，极速版 multipleangles_2009957796439134210.json、图片生成/图生图/最强多视角，任意角度，任意优化，变清晰，色调修正, 滑动柯基版。multiangles_2009962056258166785.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LatentSwitch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenMultiangleCameraNode`
- `ReferenceLatent`
- `SaveImage`
- `TextCombinerTwo`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptList`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
