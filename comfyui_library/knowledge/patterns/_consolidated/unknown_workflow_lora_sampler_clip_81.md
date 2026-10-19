---
name: unknown_workflow_lora_sampler_clip_81
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.951667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux1-dev-fp8与flux1-dev-Q4模型对比_1836327501579841537.json, 图片生成/文生图/flux文生图(自用）_1891744030592774146.json, 图片生成/文生图/低显存Flux文生图工作流_1900451456095498241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux1-dev-fp8与flux1-dev-Q4模型对比_1836327501579841537.json、图片生成/文生图/flux文生图(自用）_1891744030592774146.json、图片生成/文生图/低显存Flux文生图工作流_1900451456095498241.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `FluxGuidance` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | 1 - 1024 | 3 | 29% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1 - 1024，3 个样本，取值分散，一致性仅 29%
