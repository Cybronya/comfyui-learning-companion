---
name: unknown_workflow_video_lora_sampler_838
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6135
common_nodes: [GetNode, ImageResizeKJv2, LoadWanVideoT5TextEncoder, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2075018380200996866.json, 视频生成/文生视频/03-14-01-WAN2.1-视频风格转换-ditto_1989939354082660353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_838

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2075018380200996866.json、视频生成/文生视频/03-14-01-WAN2.1-视频风格转换-ditto_1989939354082660353.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
