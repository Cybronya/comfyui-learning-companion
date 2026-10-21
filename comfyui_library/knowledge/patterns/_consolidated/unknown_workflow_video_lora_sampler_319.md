---
name: unknown_workflow_video_lora_sampler_319
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.926857
common_nodes: [CLIPVisionLoader, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_VideoCombine, WanVideoAddWanMoveTracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1999827613361242114.json, 视频生成/图生视频/1999117506138828801.json, 视频生成/图生视频/1999165322026418177.json, 视频生成/图生视频/1999179098159185922.json, 视频生成/图生视频/1999117926080933890.json, 视频生成/图生视频/1999366459300212737.json, 视频生成/图生视频/1999110831537258497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_319

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1999827613361242114.json、视频生成/图生视频/1999117506138828801.json、视频生成/图生视频/1999165322026418177.json、视频生成/图生视频/1999179098159185922.json、视频生成/图生视频/1999117926080933890.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `RepeatImageBatch` —— 6/7 个有
- `SplineEditor` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `WanVideoWanDrawWanMoveTracks` —— 6/7 个有
- `ImageConcanate` —— 5/7 个有
- `CR Prompt Text` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `FL_PathAnimator` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SeedVR2BlockSwap` —— 1/7 个有
- `SeedVR2ExtraArgs` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
