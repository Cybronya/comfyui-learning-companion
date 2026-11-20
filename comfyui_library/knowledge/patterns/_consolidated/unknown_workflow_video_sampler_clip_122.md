---
name: unknown_workflow_video_sampler_clip_122
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9652
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ChronoEdit 时空一致性图像编辑_2073256078221078529.json, 视频生成/图生视频/87time WAN 图生视频_1913510854523060225.json, 视频生成/图生视频/FusioniX图生视频_1947317037666291713.json, 视频生成/图生视频/WAN2.1图生视频_2021960428812771330.json, 视频生成/图生视频/简单挤压捏爆工作流_1906949243003707394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ChronoEdit 时空一致性图像编辑_2073256078221078529.json、视频生成/图生视频/87time WAN 图生视频_1913510854523060225.json、视频生成/图生视频/FusioniX图生视频_1947317037666291713.json、视频生成/图生视频/WAN2.1图生视频_2021960428812771330.json、视频生成/图生视频/简单挤压捏爆工作流_1906949243003707394.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelSamplingSD3` —— 3/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `ScaleROPE` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 30 | 5 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 5 | 20% |
| 采样算法 | uni_pc | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 30，5 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，5 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 uni_pc，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
