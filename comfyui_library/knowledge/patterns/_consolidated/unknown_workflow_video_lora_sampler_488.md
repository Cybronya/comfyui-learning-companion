---
name: unknown_workflow_video_lora_sampler_488
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.615167
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Uni3c虚拟相机运镜_2013132244591841281.json, 平台全量/虚拟镜头视频运镜控制_1942097929782063105.json, 视频生成/图生视频/2025-06-04 wanvideo_ATI_1929480166395822081.json, 视频生成/图生视频/Z-uni3c虚拟相机工作流_1991800857396195330.json, 视频生成/图生视频/uni3c虚拟相机工作流_1941553575740993537.json, 视频生成/图生视频/模仿运镜uni3c虚拟相机_1983014964149530626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_488

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Uni3c虚拟相机运镜_2013132244591841281.json、平台全量/虚拟镜头视频运镜控制_1942097929782063105.json、视频生成/图生视频/2025-06-04 wanvideo_ATI_1929480166395822081.json、视频生成/图生视频/Z-uni3c虚拟相机工作流_1991800857396195330.json、视频生成/图生视频/uni3c虚拟相机工作流_1941553575740993537.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `WanVideoEncode` —— 5/6 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/6 个有
- `WanVideoUni3C_embeds` —— 5/6 个有
- `AppendStringsToList` —— 1/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `SplineEditor` —— 1/6 个有
- `WanVideoATITracks` —— 1/6 个有
- `WanVideoATITracksVisualize` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
