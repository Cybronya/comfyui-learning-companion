---
name: unknown_workflow_video_lora_sampler_166
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.9355
common_nodes: [CLIPVisionLoader, LoadImage, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Move：编辑曲线轨迹精准控制物体移动_1999379075955294209.json, 视频生成/图生视频/Wan-Move：编辑点轨迹控制动态和静态_1999823566369587201.json, 视频生成/图生视频/Wan-Move：通过潜在轨迹引导实现可控运动的视频生成_2000407963032485890.json, 视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json, 视频生成/图生视频/WanMove-轨迹引导运动_1999719285188685825.json, 视频生成/图生视频/WanMove图生视频动作编辑_1999827613361242114.json, 视频生成/图生视频/WanMove运动轨迹控制V1（创意玩法）_2000263694896558082.json, 视频生成/图生视频/Wanmove+Fill Nodes动与静轨迹控制V1（扭曲艺术）_1999117506138828801.json, 视频生成/图生视频/Wanmove_轨迹运动_图生视频_1999179098159185922.json, 视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999117926080933890.json, 视频生成/图生视频/Wanmove图生视频轨迹控制运动_1999366459300212737.json, 视频生成/图生视频/Wanmove轨迹控制_2000380802502455298.json, 视频生成/图生视频/Wanmove轨迹控制运动_1999041056794628098.json, 视频生成/图生视频/Wanmove轨迹控制运动_1999430361350275074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_166

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/Wan-Move：编辑曲线轨迹精准控制物体移动_1999379075955294209.json、视频生成/图生视频/Wan-Move：编辑点轨迹控制动态和静态_1999823566369587201.json、视频生成/图生视频/Wan-Move：通过潜在轨迹引导实现可控运动的视频生成_2000407963032485890.json、视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json、视频生成/图生视频/WanMove-轨迹引导运动_1999719285188685825.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoAddWanMoveTracks`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 13/14 个有
- `SplineEditor` —— 13/14 个有
- `WanVideoSetBlockSwap` —— 13/14 个有
- `WanVideoSetLoRAs` —— 13/14 个有
- `WanVideoTextEncode` —— 13/14 个有
- `WanVideoWanDrawWanMoveTracks` —— 13/14 个有
- `RepeatImageBatch` —— 11/14 个有
- `INTConstant` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/14 个有
- `ImageConcanate` —— 7/14 个有
- `WanVideoTorchCompileSettings` —— 7/14 个有
- `easy showAnything` —— 6/14 个有
- `ImageResizeKJv2` —— 5/14 个有
- `CR Prompt Text` —— 3/14 个有
- `FL_PathAnimator` —— 3/14 个有
- `Text Multiline` —— 3/14 个有
- `Anything Everywhere3` —— 1/14 个有
- `GetNode` —— 1/14 个有
- `HAIGC_VideoLoader` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/14 个有
- `LazySwitchKJ` —— 1/14 个有
- `SetNode` —— 1/14 个有
- `Text` —— 1/14 个有
- `WanVideoTextEncodeCached` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
