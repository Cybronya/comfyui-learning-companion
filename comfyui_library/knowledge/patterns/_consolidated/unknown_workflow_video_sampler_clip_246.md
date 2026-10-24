---
name: unknown_workflow_video_sampler_clip_246
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.984
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json, 视频生成/图生视频/分镜首尾帧_2012172730455564290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_246

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/remix V3.0首-中-尾多帧生视频-无提示词工程_2039336981896892418.json、视频生成/图生视频/分镜首尾帧_2012172730455564290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `LatentFromBatch` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 8.5 | - | 2 | 59% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8.5，样本不足，未给区间，2 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
