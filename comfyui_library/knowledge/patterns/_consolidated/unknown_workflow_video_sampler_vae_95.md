---
name: unknown_workflow_video_sampler_vae_95
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.54
common_nodes: [Float, GetNode, ImpactSwitch, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频延长-FusionX_1945398701865017345.json, 平台全量/视频延长-FusionX_1967535478931120129.json, 视频生成/图生视频/图生视频-FusionX_1940962816096681985.json, 视频生成/图生视频/图生视频-FusionX_1967535082640642050.json, 视频生成/图生视频/首尾帧视频-FusionX_1943253779137372162.json, 视频生成/图生视频/首尾帧视频-FusionX_1967512042116616194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_95

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/视频延长-FusionX_1945398701865017345.json、平台全量/视频延长-FusionX_1967535478931120129.json、视频生成/图生视频/图生视频-FusionX_1940962816096681985.json、视频生成/图生视频/图生视频-FusionX_1967535082640642050.json、视频生成/图生视频/首尾帧视频-FusionX_1943253779137372162.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 6 个 workflow 都包含：
- `Float`
- `GetNode`
- `ImpactSwitch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `LoadImage` —— 4/6 个有
- `LoadWanVideoClipTextEncoder` —— 4/6 个有
- `WanVideoClipVisionEncode` —— 4/6 个有
- `WanVideoImageToVideoEncode` —— 4/6 个有
- `ImageBatchMultiple+` —— 2/6 个有
- `ImageFromBatch+` —— 2/6 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoVACEEncode` —— 2/6 个有
- `WanVideoVACEStartToEndFrame` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
