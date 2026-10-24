---
name: unknown_workflow_video_sampler_vae_99
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7232
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, DualCLIPLoader, FramePackFindNearestBucket, FramePackSampler_F1, FramePackTimestampedTextEncode, GetImageSizeAndCount, GetNode, ImageResize+, LoadFramePackModel, SetNode, VAEDecodeTiled, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/framepack F1 Plus文生视频加速版（支持F1和普通混元视频LORA）_1932758777428856834.json, 视频生成/图生视频/Frame Pack F1 Plus稳定动态版首尾帧_1932772703088906241.json, 视频生成/图生视频/FramePack F1 Plus时间戳长视频加速工作流V1_1932516244178280449.json, 视频生成/图生视频/framepack F1 Plus图生视频加速版（支持F1和普通混元视频LORA）_1932763782831902721.json, 视频生成/图生视频/新FramePack F1 超长时间视频加速工作流_1932997763401650178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_99

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/framepack F1 Plus文生视频加速版（支持F1和普通混元视频LORA）_1932758777428856834.json、视频生成/图生视频/Frame Pack F1 Plus稳定动态版首尾帧_1932772703088906241.json、视频生成/图生视频/FramePack F1 Plus时间戳长视频加速工作流V1_1932516244178280449.json、视频生成/图生视频/framepack F1 Plus图生视频加速版（支持F1和普通混元视频LORA）_1932763782831902721.json、视频生成/图生视频/新FramePack F1 超长时间视频加速工作流_1932997763401650178.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DualCLIPLoader`
- `FramePackFindNearestBucket`
- `FramePackSampler_F1`
- `FramePackTimestampedTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResize+`
- `LoadFramePackModel`
- `SetNode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `Float` —— 3/5 个有
- `FramePackLoraSelect` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `Bjornulf_ShowStringText` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SDXLEmptyLatentSizePicker+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768x1280 (0.6) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
