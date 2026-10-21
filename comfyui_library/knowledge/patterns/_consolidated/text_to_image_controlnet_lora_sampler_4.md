---
name: text_to_image_controlnet_lora_sampler_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux_现代都市_文生图_1999040279489470466.json, 图片生成/文生图/pose 姿态 flux版本_1897223021747195906.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux_现代都市_文生图_1999040279489470466.json、图片生成/文生图/pose 姿态 flux版本_1897223021747195906.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `GemmaxRun` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `TextInput_` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 744 | - | 2 | 97% |
| 高度 | 1264 | - | 2 | 99% |
| ControlNet 权重 | 0.875 | - | 2 | 86% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.8 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 744，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1264，样本不足，未给区间，2 个样本，取值集中（一致性 99%）
- ControlNet 权重 中位数 0.875，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.8，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
