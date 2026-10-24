---
name: unknown_workflow_video_lora_sampler_316
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.929857
common_nodes: [CLIPVisionLoader, LoadImage, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [视频生成/图生视频/WanMove-轨迹引导运动_1999719285188685825.json, 视频生成/图生视频/WanMove图生视频动作编辑_1999827613361242114.json, 视频生成/图生视频/WanMove运动轨迹控制V1（创意玩法）_2000263694896558082.json, 视频生成/图生视频/Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json, 视频生成/图生视频/Wanmove+Fill Nodes动与静轨迹控制V1（扭曲艺术）_1999117506138828801.json, 视频生成/图生视频/Wanmove+Fill+Nodes轨迹控制V1_1999165322026418177.json, 视频生成/图生视频/Wanmove多点轨迹运动指引图生视频V1_1999110831537258497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_316

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/WanMove-轨迹引导运动_1999719285188685825.json、视频生成/图生视频/WanMove图生视频动作编辑_1999827613361242114.json、视频生成/图生视频/WanMove运动轨迹控制V1（创意玩法）_2000263694896558082.json、视频生成/图生视频/Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json、视频生成/图生视频/Wanmove+Fill Nodes动与静轨迹控制V1（扭曲艺术）_1999117506138828801.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
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
- `WanVideoWanDrawWanMoveTracks`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `RepeatImageBatch` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `INTConstant` —— 5/7 个有
- `ImageConcanate` —— 5/7 个有
- `SplineEditor` —— 5/7 个有
- `CR Prompt Text` —— 4/7 个有
- `FL_PathAnimator` —— 4/7 个有
- `GetNode` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `LazySwitchKJ` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有
- `SeedVR2ExtraArgs` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
