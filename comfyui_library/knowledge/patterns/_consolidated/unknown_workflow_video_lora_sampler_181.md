---
name: unknown_workflow_video_lora_sampler_181
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8705
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [图片生成/图生图/新版轨迹控制-Wan-move_1998583110839230466.json, 视频生成/图生视频/03-19-01-WAN2.1-扭曲艺术-Wanmove+Fill Nodes动与静轨迹控制_2000440766998736897.json, 视频生成/图生视频/Wan move指定轨迹运动-指引-图生视频版本1_1999398013804179457.json, 视频生成/图生视频/Wan-Move轨迹控制运动_2015351351290630146.json, 视频生成/图生视频/Wan-Move：编辑曲线轨迹精准控制物体移动_1999379075955294209.json, 视频生成/图生视频/Wan-Move：编辑点轨迹控制动态和静态_1999823566369587201.json, 视频生成/图生视频/Wan-Move：通过潜在轨迹引导实现可控运动的视频生成_2000407963032485890.json, 视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json, 视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999117926080933890.json, 视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999366459300212737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_181

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/新版轨迹控制-Wan-move_1998583110839230466.json、视频生成/图生视频/03-19-01-WAN2.1-扭曲艺术-Wanmove+Fill Nodes动与静轨迹控制_2000440766998736897.json、视频生成/图生视频/Wan move指定轨迹运动-指引-图生视频版本1_1999398013804179457.json、视频生成/图生视频/Wan-Move轨迹控制运动_2015351351290630146.json、视频生成/图生视频/Wan-Move：编辑曲线轨迹精准控制物体移动_1999379075955294209.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `SplineEditor` —— 9/10 个有
- `RepeatImageBatch` —— 8/10 个有
- `INTConstant` —— 7/10 个有
- `ImageConcanate` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `WanVideoTorchCompileSettings` —— 6/10 个有
- `easy showAnything` —— 5/10 个有
- `FL_PathAnimator` —— 3/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `Text Multiline` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `Getter` —— 1/10 个有
- `HAIGC_VideoLoader` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `Setter` —— 1/10 个有
- `Text` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
