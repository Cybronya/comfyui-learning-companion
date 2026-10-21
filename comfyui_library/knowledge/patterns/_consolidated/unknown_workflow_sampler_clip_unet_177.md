---
name: unknown_workflow_sampler_clip_unet_177
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.864333
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1904911641337860097.json, 图片生成/文生图/krea2-极致写实工作流_2087741288522280962.json, 图片生成/文生图/文生图V1_2087151380954963970.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_177

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1904911641337860097.json、图片生成/文生图/krea2-极致写实工作流_2087741288522280962.json、图片生成/文生图/文生图V1_2087151380954963970.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CFGZeroStarAndInit` —— 1/3 个有
- `DetailDaemonGraphSigmasNode` —— 1/3 个有
- `DetailDaemonSamplerNode` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1280 | 3 | 90% |
| 高度 | 1560 | 1024 - 1920 | 3 | 75% |
| LoRA 模型强度 | 0 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
- 高度 中位数 1560，观测区间 1024 - 1920，3 个样本
