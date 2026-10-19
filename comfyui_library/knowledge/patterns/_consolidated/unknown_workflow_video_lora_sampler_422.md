---
name: unknown_workflow_video_lora_sampler_422
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9596
common_nodes: [CLIPVisionLoader, ImageConcanate, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoUniAnimateDWPoseDetector, WanVideoUniAnimatePoseInput, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1913792299430572033.json, 视频生成/图生视频/1913638133471346689.json, 视频生成/图生视频/1913658373089492993.json, 视频生成/图生视频/1914528048430153729.json, 视频生成/图生视频/1914272039954280449.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_422

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1913792299430572033.json、视频生成/图生视频/1913638133471346689.json、视频生成/图生视频/1913658373089492993.json、视频生成/图生视频/1914528048430153729.json、视频生成/图生视频/1914272039954280449.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageConcanate`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoUniAnimateDWPoseDetector`
- `WanVideoUniAnimatePoseInput`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Crop Face` —— 4/5 个有
- `ImageListToImageBatch` —— 4/5 个有
- `ImpactImageBatchToImageList` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `Load RetinaFace` —— 4/5 个有
- `ReActorFaceSwap` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `GPENO Face Restoration` —— 3/5 个有
- `JWImageResizeByLongerSide` —— 3/5 个有
- `Note Plus (mtb)` —— 3/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
