---
name: text_to_image_inpaint_lora_sampler_11
type: Text To Image
frequency: 2
level: weak
coverage: 0.643
common_nodes: [Anything Everywhere, CLIPTextEncode, CM_IntBinaryOperation, CM_IntToFloat, CM_IntToNumber, CM_NumberBinaryOperation, CM_NumberToInt, CR Float To Integer, CR Prompt Text, CheckpointLoader|pysssss, Display Int (rgthree), EmptyLatentImage, GetNode, Image Crop Location, Image Paste Crop by Location, ImagePadForOutpaint, JWFloatAdd, JWFloatMul, JWIntegerToFloat, KSampler, LoraLoader|pysssss, Mask Gaussian Region, Mask Invert, Mask Smooth Region, MaskComposite, MaskToImage, PreviewImage, SaveImage, Seed Generator, SetLatentNoiseMask, SetNode, ShowText|pysssss, SolidMask, Text Concatenate, Text to Conditioning, VAEDecode, VAEEncodeForInpaint, easy float, easy int]
problems: []
missing: []
members: [图片生成/文生图/万物一键扩图_1905242718396665858.json, 平台全量/一键扩图(Outpaint)-B.Duck_1894270543351427074.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/万物一键扩图_1905242718396665858.json、平台全量/一键扩图(Outpaint)-B.Duck_1894270543351427074.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CM_IntBinaryOperation`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberBinaryOperation`
- `CM_NumberToInt`
- `CR Float To Integer`
- `CR Prompt Text`
- `CheckpointLoader|pysssss`
- `Display Int (rgthree)`
- `EmptyLatentImage`
- `GetNode`
- `Image Crop Location`
- `Image Paste Crop by Location`
- `ImagePadForOutpaint`
- `JWFloatAdd`
- `JWFloatMul`
- `JWIntegerToFloat`
- `KSampler`
- `LoraLoader|pysssss`
- `Mask Gaussian Region`
- `Mask Invert`
- `Mask Smooth Region`
- `MaskComposite`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `Seed Generator`
- `SetLatentNoiseMask`
- `SetNode`
- `ShowText|pysssss`
- `SolidMask`
- `Text Concatenate`
- `Text to Conditioning`
- `VAEDecode`
- `VAEEncodeForInpaint`
- `easy float`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 2 | 100% |
| 调度器 | exponential | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 760 | - | 2 | 100% |
| LoRA 模型强度 | 0.85 | - | 2 | 100% |
| LoRA 文本强度 | 0.85 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 exponential，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 760，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
