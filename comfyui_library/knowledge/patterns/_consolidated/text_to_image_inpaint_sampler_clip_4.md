---
name: text_to_image_inpaint_sampler_clip_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.759
common_nodes: [BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, EmptyLatentImage, FluxGuidance, GetImageSize, GetNode, GrowMask, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, KSamplerSelect, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage, LayerUtility: ColorPicker, LoadImage, MaskToImage, MathExpression|pysssss, PrimitiveInt, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SetNode, StyleModelApply, StyleModelLoader, Text Concatenate (JPS), TextInput_, VAEDecode, VAELoader, easy forLoopEnd, easy forLoopStart, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商批量虚拟换装急速版，2分半出4图（Nunchaku，For loop)_1914917133233418241.json, 图片生成/图生图/电商批量虚拟换装标准版，5分钟出4图（FLUX，For loop）_1915686280489795585.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商批量虚拟换装急速版，2分半出4图（Nunchaku，For loop)_1914917133233418241.json、图片生成/图生图/电商批量虚拟换装标准版，5分钟出4图（FLUX，For loop）_1915686280489795585.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `GrowMask`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `Text Concatenate (JPS)`
- `TextInput_`
- `VAEDecode`
- `VAELoader`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `BasicGuider` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `NunchakuTextEncoderLoader` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveImageAndMetadata_` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `workflow>Setting` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 616 | - | 2 | 83% |
| 高度 | 896 | - | 2 | 57% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 616，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 896，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
