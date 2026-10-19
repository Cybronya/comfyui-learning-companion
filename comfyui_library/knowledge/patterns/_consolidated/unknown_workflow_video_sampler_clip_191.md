---
name: unknown_workflow_video_sampler_clip_191
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.684333
common_nodes: [Anything Everywhere, GetNode, Int, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, Seed Everywhere, SetNode, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950411115459207170.json, 视频生成/图生视频/1916125133394608130.json, 视频生成/图生视频/1932714999003369473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_191

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1950411115459207170.json、视频生成/图生视频/1916125133394608130.json、视频生成/图生视频/1932714999003369473.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `GetNode`
- `Int`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `Seed Everywhere`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `DisplayAny` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SaveLatent` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
