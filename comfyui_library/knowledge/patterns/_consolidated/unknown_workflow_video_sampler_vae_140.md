---
name: unknown_workflow_video_sampler_vae_140
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9475
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1894927081615339521.json, 视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json, 视频生成/文生视频/1894761032408313857.json, 视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1894927081615339521.json、视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json、视频生成/文生视频/1894761032408313857.json、视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 3/4 个有
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Int` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `Primitive string [Crystools]` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
