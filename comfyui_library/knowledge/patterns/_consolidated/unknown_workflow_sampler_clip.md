---
name: unknown_workflow_sampler_clip
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.87925
common_nodes: [CLIPTextEncode, PiDFinalize, PiDKSamplerCapture, PiDPrepare, PiDSample, PiDTextPrompt, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json, 图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json, 图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json, 图片生成/文生图/Z-Image Turbo｜PiD直出4K极速版_2059961793564471298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json、图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json、图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json、图片生成/文生图/Z-Image Turbo｜PiD直出4K极速版_2059961793564471298.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `PiDFinalize`
- `PiDKSamplerCapture`
- `PiDPrepare`
- `PiDSample`
- `PiDTextPrompt`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `CLIPLoader` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26.5 | 9 - 50 | 4 | 48% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.4 | 4 | 38% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 25% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26.5，观测区间 9 - 50，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.4，4 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 25%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
