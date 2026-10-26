---
name: unknown_workflow_video_lora_sampler_244
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.894
common_nodes: [CLIPVisionLoader, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [视频生成/图生视频/03-19-01-WAN2.1-扭曲艺术-Wanmove+Fill Nodes动与静轨迹控制_2000440766998736897.json, 视频生成/图生视频/Wan move指定轨迹运动-指引-图生视频版本1_1999398013804179457.json, 视频生成/图生视频/Wan-Move：编辑曲线轨迹精准控制物体移动_1999379075955294209.json, 视频生成/图生视频/Wan-Move：编辑点轨迹控制动态和静态_1999823566369587201.json, 视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json, 视频生成/图生视频/WanMove运动轨迹控制V1（创意玩法）_2000263694896558082.json, 视频生成/图生视频/Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json, 视频生成/图生视频/Wanmove+Fill Nodes动与静轨迹控制V1（扭曲艺术）_1999117506138828801.json, 视频生成/图生视频/Wanmove+Fill+Nodes轨迹控制V1_1999165322026418177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_244

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/03-19-01-WAN2.1-扭曲艺术-Wanmove+Fill Nodes动与静轨迹控制_2000440766998736897.json、视频生成/图生视频/Wan move指定轨迹运动-指引-图生视频版本1_1999398013804179457.json、视频生成/图生视频/Wan-Move：编辑曲线轨迹精准控制物体移动_1999379075955294209.json、视频生成/图生视频/Wan-Move：编辑点轨迹控制动态和静态_1999823566369587201.json、视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `FL_PathAnimator` —— 6/9 个有
- `INTConstant` —— 6/9 个有
- `RepeatImageBatch` —— 6/9 个有
- `SplineEditor` —— 6/9 个有
- `CR Prompt Text` —— 5/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `easy showAnything` —— 2/9 个有
- `HAIGC_VideoLoader` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `LazySwitchKJ` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `SeedVR2` —— 1/9 个有
- `SeedVR2BlockSwap` —— 1/9 个有
- `SeedVR2ExtraArgs` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `WanVideoTorchCompileSettings` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
