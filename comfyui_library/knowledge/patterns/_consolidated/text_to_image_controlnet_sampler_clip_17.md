---
name: text_to_image_controlnet_sampler_clip_17
type: Text To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】换脸之InstantID_2019297726940323842.json, 图片生成/图生图/参考人物手办设计——任意人像转手办工作流_1923624171220496386.json, 图片生成/图生图/手办设计——任意人像转手办工作流_1923642776616169474.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【遇见AI】换脸之InstantID_2019297726940323842.json、图片生成/图生图/参考人物手办设计——任意人像转手办工作流_1923624171220496386.json、图片生成/图生图/手办设计——任意人像转手办工作流_1923642776616169474.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 2/3 个有
- `PMRF` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `easy imageInterrogator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 896 - 1024 | 3 | 94% |
| 高度 | 1152 | 1024 - 1152 | 3 | 95% |
| 采样步数 | 25 | 15 - 30 | 3 | 73% |
| Prompt 约束强度(CFG) | 4 | 2 - 7.95 | 3 | 47% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.7 - 1 | 3 | 84% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 896 - 1024，3 个样本，取值集中（一致性 94%）
- 高度 中位数 1152，观测区间 1024 - 1152，3 个样本，取值集中（一致性 95%）
- 采样步数 中位数 25，观测区间 15 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 2 - 7.95，3 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
