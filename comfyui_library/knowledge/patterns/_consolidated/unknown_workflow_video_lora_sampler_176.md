---
name: unknown_workflow_video_lora_sampler_176
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8869
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, WanVideoWanDrawWanMoveTracks]
problems: []
missing: []
members: [视频生成/图生视频/2000440766998736897.json, 视频生成/图生视频/1999398013804179457.json, 视频生成/图生视频/2015351351290630146.json, 视频生成/图生视频/1999379075955294209.json, 视频生成/图生视频/1999823566369587201.json, 视频生成/图生视频/2000407963032485890.json, 视频生成/图生视频/1999283559233974273.json, 视频生成/图生视频/1999719285188685825.json, 视频生成/图生视频/2000263694896558082.json, 视频生成/图生视频/1999310460828647425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_176

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2000440766998736897.json、视频生成/图生视频/1999398013804179457.json、视频生成/图生视频/2015351351290630146.json、视频生成/图生视频/1999379075955294209.json、视频生成/图生视频/1999823566369587201.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

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
- `SplineEditor` —— 8/10 个有
- `ImageConcanate` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `RepeatImageBatch` —— 7/10 个有
- `INTConstant` —— 6/10 个有
- `FL_PathAnimator` —— 5/10 个有
- `CR Prompt Text` —— 4/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `WanVideoTorchCompileSettings` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `Getter` —— 1/10 个有
- `HAIGC_VideoLoader` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `LazySwitchKJ` —— 1/10 个有
- `Primitive integer [Crystools]` —— 1/10 个有
- `Setter` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `Text` —— 1/10 个有
- `Text Multiline` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
