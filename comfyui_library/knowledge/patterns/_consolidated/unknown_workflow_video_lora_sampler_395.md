---
name: unknown_workflow_video_lora_sampler_395
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.900833
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1949454368652308481.json, 视频生成/文生视频/KJ工作流_2066489946755657729.json, 视频生成/文生视频/LSP足komg专用，白丝，WAN2.2文生图_2018061075089985538.json, 视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474.json, 视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394.json, 视频生成/文生视频/1936093650231152641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_395

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/1949454368652308481.json、视频生成/文生视频/KJ工作流_2066489946755657729.json、视频生成/文生视频/LSP足komg专用，白丝，WAN2.2文生图_2018061075089985538.json、视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2017851048295145474.json、视频生成/文生视频/WAN2.2-4步极速版_文生视频-KJ版工作流_2050481503284539394.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `WanVideoBlockSwap` —— 3/6 个有
- `CreateCFGScheduleFloatList` —— 2/6 个有
- `WanVideoEnhanceAVideo` —— 2/6 个有
- `ImpactInt` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
