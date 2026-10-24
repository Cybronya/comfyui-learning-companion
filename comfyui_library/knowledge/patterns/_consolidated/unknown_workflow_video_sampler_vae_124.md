---
name: unknown_workflow_video_sampler_vae_124
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9666
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json, 视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json, 视频生成/文生视频/Wan文生视频工作流-KJ版_1894761032408313857.json, 视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json, 视频生成/文生视频/万相文生视频_1894627522200645634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_124

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json、视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json、视频生成/文生视频/Wan文生视频工作流-KJ版_1894761032408313857.json、视频生成/文生视频/wan2.1图生视频pusa姿态控制+加速lora_1948656923534077953.json、视频生成/文生视频/万相文生视频_1894627522200645634.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `Primitive string [Crystools]` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `CreateCFGScheduleFloatList` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
