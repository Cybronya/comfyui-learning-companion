---
name: unknown_workflow_lora_sampler_clip_130
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.983333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/低显存Flux文生图工作流_1900451456095498241.json, 图片生成/文生图/生成系列性服装设计_1884234765942538241.json, 图片生成/文生图/风后文生图_1878760414459932673.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/低显存Flux文生图工作流_1900451456095498241.json、图片生成/文生图/生成系列性服装设计_1884234765942538241.json、图片生成/文生图/风后文生图_1878760414459932673.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1080 | 3 | 86% |
| 高度 | 1280 | 1024 - 1920 | 3 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1080，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1280，观测区间 1024 - 1920，3 个样本
