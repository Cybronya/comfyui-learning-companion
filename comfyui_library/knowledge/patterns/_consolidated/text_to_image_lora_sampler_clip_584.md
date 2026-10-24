---
name: text_to_image_lora_sampler_clip_584
type: Text To Image
frequency: 2
level: weak
coverage: 0.901
common_nodes: [AIO_Preprocessor, CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, Flex2Conditioner, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/​​Flex.2文生图+局部重绘+CN控制_1917180206874820610.json, 图片生成/文生图/​​Flex.2控制文生图图生图_1920256323848437761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_584

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/​​Flex.2文生图+局部重绘+CN控制_1917180206874820610.json、图片生成/文生图/​​Flex.2控制文生图图生图_1920256323848437761.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Flex2Conditioner`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader (segment anything2)` —— 1/2 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 1/2 个有
- `GrowMaskWithBlur` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `SAM2ModelLoader (segment anything2)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | deis | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.8 | - | 2 | 75% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1100 | - | 2 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 deis，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1100，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
