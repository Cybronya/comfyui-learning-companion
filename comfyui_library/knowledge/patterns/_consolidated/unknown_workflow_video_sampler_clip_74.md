---
name: unknown_workflow_video_sampler_clip_74
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.886714
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Note Plus (mtb), easy imageSize]
members: [图片生成/文生图/1903369844585041921.json, 视频生成/图生视频/2021960428812771330.json, 视频生成/图生视频/1924384393446477826.json, 视频生成/图生视频/1940719231082328066.json, 视频生成/图生视频/2001218246663602177.json, 视频生成/图生视频/2000392269180137473.json, 视频生成/文生视频/1903369844585041921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1903369844585041921.json、视频生成/图生视频/2021960428812771330.json、视频生成/图生视频/1924384393446477826.json、视频生成/图生视频/1940719231082328066.json、视频生成/图生视频/2001218246663602177.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `WanImageToVideo` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `ModelSamplingSD3` —— 5/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `ApplySageAttention` —— 2/7 个有
- `ImageResize+` —— 2/7 个有
- `Int` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `SaveWEBM` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `WanVideoTeaCacheKJ` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 30 | 7 | 41% |
| Prompt 约束强度(CFG) | 4 | 1 - 6 | 7 | 35% |
| 采样算法 | uni_pc | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 30，7 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 6，7 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 uni_pc，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Note Plus (mtb)、easy imageSize
