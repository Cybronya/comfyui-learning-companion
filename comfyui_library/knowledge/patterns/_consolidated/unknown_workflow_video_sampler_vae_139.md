---
name: unknown_workflow_video_sampler_vae_139
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.548
common_nodes: [Float, GetNode, ImpactSwitch, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生视频-FusionX_1940962816096681985.json, 视频生成/图生视频/图生视频-FusionX_1967535082640642050.json, 视频生成/图生视频/首尾帧视频-FusionX_1943253779137372162.json, 视频生成/图生视频/首尾帧视频-FusionX_1967512042116616194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_139

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/图生视频-FusionX_1940962816096681985.json、视频生成/图生视频/图生视频-FusionX_1967535082640642050.json、视频生成/图生视频/首尾帧视频-FusionX_1943253779137372162.json、视频生成/图生视频/首尾帧视频-FusionX_1967512042116616194.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `Float`
- `GetNode`
- `ImpactSwitch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageMaskScaleAsV2` —— 2/4 个有
- `LoadWanVideoClipTextEncoder` —— 2/4 个有
- `WanVideoClipVisionEncode` —— 2/4 个有
- `WanVideoImageToVideoEncode` —— 2/4 个有
- `WanVideoVACEEncode` —— 2/4 个有
- `WanVideoVACEStartToEndFrame` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
