---
name: text_to_image_controlnet_sampler_clip_29
type: Text To Image
frequency: 3
level: strong
coverage: 0.911667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/controlnet深度与姿势双控制人物出图sdxl模型（lora+提示词）_1965699024550559746.json, 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json, 平台全量/controlnet深度与姿势双控制人物出图sdxl（lora+提示词）_1965677902790578178.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/controlnet深度与姿势双控制人物出图sdxl模型（lora+提示词）_1965699024550559746.json、图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+controlnet_2011326038407651330.json、平台全量/controlnet深度与姿势双控制人物出图sdxl（lora+提示词）_1965677902790578178.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Image Compare (mtb)` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `MiDaS-NormalMapPreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1024 | 768 - 1024 | 3 | 87% |
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 0.6 | - | 2 | 100% |
| 采样步数 | 27 | 20 - 27 | 3 | 87% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 27，观测区间 20 - 27，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
