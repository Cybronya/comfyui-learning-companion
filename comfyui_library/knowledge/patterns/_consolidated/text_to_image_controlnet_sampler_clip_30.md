---
name: text_to_image_controlnet_sampler_clip_30
type: Text To Image
frequency: 2
level: weak
coverage: 0.903
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/controlnet深度与姿势双控制人物出图sdxl模型（lora+提示词）_1965699024550559746.json, 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/controlnet深度与姿势双控制人物出图sdxl模型（lora+提示词）_1965699024550559746.json、图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `Image Compare (mtb)` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `MiDaS-NormalMapPreprocessor` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 896 | - | 2 | 86% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 0.6 | - | 1 | 100% |
| 采样步数 | 23.5 | - | 2 | 85% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样步数 中位数 23.5，样本不足，未给区间，2 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
