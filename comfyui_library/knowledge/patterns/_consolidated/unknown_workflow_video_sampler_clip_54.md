---
name: unknown_workflow_video_sampler_clip_54
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.911889
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Note Plus (mtb), easy imageSize]
members: [图片生成/文生图/1903369844585041921.json, 视频生成/图生视频/1913510854523060225.json, 视频生成/图生视频/1947317037666291713.json, 视频生成/图生视频/2021960428812771330.json, 视频生成/图生视频/1924384393446477826.json, 视频生成/图生视频/1940719231082328066.json, 视频生成/图生视频/2001218246663602177.json, 视频生成/图生视频/2000392269180137473.json, 视频生成/文生视频/1903369844585041921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1903369844585041921.json、视频生成/图生视频/1913510854523060225.json、视频生成/图生视频/1947317037666291713.json、视频生成/图生视频/2021960428812771330.json、视频生成/图生视频/1924384393446477826.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanImageToVideo` —— 8/9 个有
- `ModelSamplingSD3` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `ApplySageAttention` —— 2/9 个有
- `ImageResize+` —— 2/9 个有
- `Int` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `SaveWEBM` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `WanVideoTeaCacheKJ` —— 2/9 个有
- `easy imageSize` —— 2/9 个有
- `WanFirstLastFrameToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 30 | 9 | 46% |
| Prompt 约束强度(CFG) | 4 | 1 - 6 | 9 | 34% |
| 采样算法 | uni_pc | - | 9 | 67% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 30，9 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 6，9 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 uni_pc，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Note Plus (mtb)、easy imageSize
