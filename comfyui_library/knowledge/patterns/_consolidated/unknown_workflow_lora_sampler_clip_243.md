---
name: unknown_workflow_lora_sampler_clip_243
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5995
common_nodes: [Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptySD3LatentImage, Florence2ModelLoader, Florence2Run, GetImageSize, GetNode, ImageScaleToMegapixels, KSampler, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, SaveImage, SetNode, ShowText|pysssss, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/FLUX双截棍-真人写真【反推图_参考风格】_1948020884901638146.json, 图片生成/图生图/超棒！各种风格人像转绘2.5D风格!_1913060300755562498.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_243

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/FLUX双截棍-真人写真【反推图_参考风格】_1948020884901638146.json、图片生成/图生图/超棒！各种风格人像转绘2.5D风格!_1913060300755562498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSize`
- `GetNode`
- `ImageScaleToMegapixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two_advanced` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `Joy_extra_options` —— 1/2 个有
- `Switch conditioning [Crystools]` —— 1/2 个有
- `easy boolean` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
