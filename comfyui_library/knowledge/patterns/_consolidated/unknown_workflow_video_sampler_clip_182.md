---
name: unknown_workflow_video_sampler_clip_182
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.989333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2039336981896892418.json, 视频生成/图生视频/2040056903719460866.json, 视频生成/图生视频/2012172730455564290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2039336981896892418.json、视频生成/图生视频/2040056903719460866.json、视频生成/图生视频/2012172730455564290.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `WanFirstLastFrameToVideo` —— 2/3 个有
- `Int` —— 1/3 个有
- `LatentFromBatch` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 5 - 12 | 3 | 66% |
| 采样算法 | 1 | 1 - 3.5 | 3 | 36% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
