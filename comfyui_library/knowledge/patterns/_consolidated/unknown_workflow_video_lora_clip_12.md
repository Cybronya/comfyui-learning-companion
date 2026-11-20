---
name: unknown_workflow_video_lora_clip_12
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91825
common_nodes: [ApplySageAttention, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LoraLoaderModelOnly, ModelSamplingSD3, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.2RemixV2.0图生视频_1989285733921902593.json, 视频生成/图生视频/Z-image+Wan2.2 文生图生视频工作流 高动态_1993950908476309506.json, 视频生成/图生视频/wan2.1图生视频官流【教学】_2001218246663602177.json, 视频生成/图生视频/wan2.1首尾帧视频【教学】_2000392269180137473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2RemixV2.0图生视频_1989285733921902593.json、视频生成/图生视频/Z-image+Wan2.2 文生图生视频工作流 高动态_1993950908476309506.json、视频生成/图生视频/wan2.1图生视频官流【教学】_2001218246663602177.json、视频生成/图生视频/wan2.1首尾帧视频【教学】_2000392269180137473.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Int` —— 2/4 个有
- `PainterI2V` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `WanMoeKSampler` —— 2/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `WanFirstLastFrameToVideo` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 4 | 22% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 22%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
