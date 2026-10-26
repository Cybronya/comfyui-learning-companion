---
name: unknown_workflow_video_sampler_vae_87
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.965333
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json, 视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json, 视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json, 视频生成/文生视频/万相2.1文生视频，可控性超强_1907671581512855554.json, 视频生成/文生视频/万相文生视频_1894627522200645634.json, 视频生成/文生视频/无限素材wanvideo2_2_1959121598613762050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_87

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/Wan2.1阿里通义万相文生视频工作流_1894927081615339521.json、视频生成/文生视频/Wan2.2文生视频工作流4步急速版_2045802208008081409.json、视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json、视频生成/文生视频/万相2.1文生视频，可控性超强_1907671581512855554.json、视频生成/文生视频/万相文生视频_1894627522200645634.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 4/6 个有
- `CreateCFGScheduleFloatList` —— 2/6 个有
- `Primitive string [Crystools]` —— 2/6 个有
- `WanVideoLoraSelect` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
