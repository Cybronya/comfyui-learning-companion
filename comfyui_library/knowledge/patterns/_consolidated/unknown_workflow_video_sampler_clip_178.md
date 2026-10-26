---
name: unknown_workflow_video_sampler_clip_178
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.942
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ChronoEdit 时空一致性图像编辑_2073256078221078529.json, 视频生成/图生视频/WAN2.1 Comfy-Org 官方图生视频原始工作流_1895181615108849666.json, 视频生成/图生视频/WAN2.1图生视频_2021960428812771330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_178

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/ChronoEdit 时空一致性图像编辑_2073256078221078529.json、视频生成/图生视频/WAN2.1 Comfy-Org 官方图生视频原始工作流_1895181615108849666.json、视频生成/图生视频/WAN2.1图生视频_2021960428812771330.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `ScaleROPE` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 20 | 3 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 3 | 12% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 20，3 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，3 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
