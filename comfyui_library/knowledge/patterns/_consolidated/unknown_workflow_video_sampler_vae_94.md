---
name: unknown_workflow_video_sampler_vae_94
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.701
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, DualCLIPLoader, FramePackFindNearestBucket, FramePackSampler_F1, FramePackTimestampedTextEncode, GetImageSizeAndCount, GetNode, ImageResize+, LoadFramePackModel, SetNode, VAEDecodeTiled, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: [SDXLEmptyLatentSizePicker+, CR Prompt Text, ImageResize+]
members: [图片生成/文生图/1932758777428856834.json, 视频生成/图生视频/1932772703088906241.json, 视频生成/图生视频/1932516244178280449.json, 视频生成/图生视频/1932763782831902721.json, 视频生成/图生视频/1932997763401650178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_94

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1932758777428856834.json、视频生成/图生视频/1932772703088906241.json、视频生成/图生视频/1932516244178280449.json、视频生成/图生视频/1932763782831902721.json、视频生成/图生视频/1932997763401650178.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：70%

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

- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、CR Prompt Text、ImageResize+
