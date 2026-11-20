---
name: unknown_workflow_video_lora_sampler_529
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.921
common_nodes: [CLIPVisionLoader, INTConstant, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [视频生成/图生视频/Wanmove+Fill+Nodes轨迹控制V1_1999165322026418177.json, 视频生成/图生视频/Wanmove多点轨迹运动指引图生视频V1_1999110831537258497.json, 视频生成/图生视频/Wanmove轨迹控制运动视频_2007414676862279682.json, 视频生成/图生视频/图生视频 视频轨迹控制 WanMove_1996588686689058818.json, 视频生成/图生视频/图生视频 运动轨迹控制 WanMove_1990436660024414209.json, 视频生成/图生视频/图生视频 运动轨迹控制 WanMove_2059086932885467138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_529

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wanmove+Fill+Nodes轨迹控制V1_1999165322026418177.json、视频生成/图生视频/Wanmove多点轨迹运动指引图生视频V1_1999110831537258497.json、视频生成/图生视频/Wanmove轨迹控制运动视频_2007414676862279682.json、视频生成/图生视频/图生视频 视频轨迹控制 WanMove_1996588686689058818.json、视频生成/图生视频/图生视频 运动轨迹控制 WanMove_1990436660024414209.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RepeatImageBatch`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `SplineEditor` —— 5/6 个有
- `SeedVR2BlockSwap` —— 4/6 个有
- `SeedVR2ExtraArgs` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `Int` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `RIFE VFI` —— 3/6 个有
- `SeedVR2GGUF` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `FL_PathAnimator` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `LayerUtility: TextBox` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
