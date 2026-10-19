---
name: text_to_image_inpaint_lora_sampler
type: Text To Image
frequency: 2
level: weak
coverage: 0.927
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, GetImageSize, HAIGC_SavePSD, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text]
members: [图片生成/图生图/2013139159199784961.json, 图片生成/图生图/局部重绘加扩图工作流，图生图局部处理图像扩展工具_2107188537446715393.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2013139159199784961.json、图片生成/图生图/局部重绘加扩图工作流，图生图局部处理图像扩展工具_2107188537446715393.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `HAIGC_SavePSD`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 296 | - | 2 | 27% |
| 高度 | 296 | - | 2 | 27% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 296，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 高度 中位数 296，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 高发问题（9/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
