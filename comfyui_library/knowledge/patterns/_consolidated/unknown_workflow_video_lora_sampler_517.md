---
name: unknown_workflow_video_lora_sampler_517
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7738
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json, 视频生成/文生视频/WAN2.2文生视频_1951636109178646529.json, 视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json, 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json, 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_517

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/WAN2.2-文生视频_2018966000456175618.json、视频生成/文生视频/WAN2.2文生视频_1951636109178646529.json、视频生成/文生视频/Wan2.2_-KJ-6步加速文生视频_1950379943495647234.json、视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json、视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/5 个有
- `Int` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `ImpactInt` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `WanVideoScheduler` —— 2/5 个有
- `WanVideoSigmaToStep` —— 2/5 个有
- `DF_Integer` —— 1/5 个有
- `Float to Int` —— 1/5 个有
- `MathExpression_UTK` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
