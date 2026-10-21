---
name: unknown_workflow_video_lora_sampler_451
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9076
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, SplineEditor, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2071858962642857985.json, 视频生成/图生视频/2007470369120198658.json, 视频生成/图生视频/2008000096457203714.json, 视频生成/图生视频/1999451312800624642.json, 视频生成/文生视频/Wan-Move潜在轨迹引导视频生成_1998898965116542977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_451

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2071858962642857985.json、视频生成/图生视频/2007470369120198658.json、视频生成/图生视频/2008000096457203714.json、视频生成/图生视频/1999451312800624642.json、视频生成/文生视频/Wan-Move潜在轨迹引导视频生成_1998898965116542977.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `RepeatImageBatch` —— 4/5 个有
- `WanVideoAddWanMoveTracks` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `WanVideoWanDrawWanMoveTracks` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `CR Text` —— 1/5 个有
- `ImpactInt` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `WanVideoATITracks` —— 1/5 个有
- `WanVideoATITracksVisualize` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
