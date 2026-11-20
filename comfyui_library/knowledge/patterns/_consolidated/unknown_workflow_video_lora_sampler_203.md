---
name: unknown_workflow_video_lora_sampler_203
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9141
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, SplineEditor, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [图片生成/图生图/新版轨迹控制-Wan-move_1998583110839230466.json, 数字人/数字人/Wanmove轨迹控制运动_1999275955468238849.json, 视频生成/图生视频/Wan-Move轨迹控制运动_2015351351290630146.json, 视频生成/图生视频/Wan-Move：通过潜在轨迹引导实现可控运动的视频生成_2000407963032485890.json, 视频生成/图生视频/WanMove-轨迹引导运动_1999719285188685825.json, 视频生成/图生视频/Wanmove轨迹控制_2000380802502455298.json, 视频生成/图生视频/Wanmove轨迹控制运动_1999041056794628098.json, 视频生成/图生视频/Wanmove轨迹控制运动_1999430361350275074.json, 视频生成/图生视频/Wanmove轨迹控制运动视频_2007414676862279682.json, 视频生成/图生视频/图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_203

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/新版轨迹控制-Wan-move_1998583110839230466.json、数字人/数字人/Wanmove轨迹控制运动_1999275955468238849.json、视频生成/图生视频/Wan-Move轨迹控制运动_2015351351290630146.json、视频生成/图生视频/Wan-Move：通过潜在轨迹引导实现可控运动的视频生成_2000407963032485890.json、视频生成/图生视频/WanMove-轨迹引导运动_1999719285188685825.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RepeatImageBatch`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoAddWanMoveTracks`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `WanVideoWanDrawWanMoveTracks`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `INTConstant` —— 5/10 个有
- `easy showAnything` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `CR SDXL Aspect Ratio` —— 1/10 个有
- `FL_PathAnimator` —— 1/10 个有
- `Getter` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `LayerUtility: TextBox` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `Setter` —— 1/10 个有
- `Text` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
