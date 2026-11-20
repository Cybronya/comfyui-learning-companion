---
name: unknown_workflow_video_sampler_vae_136
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84275
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, RIFE VFI, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json, 平台全量/Unianimate转绘跳舞视频_1926976453735272449.json, 视频生成/图生视频/360度旋转效果Wan2.1_1922551848883077121.json, 视频生成/文生视频/【丝滑补帧】Wan2.1 图生视频  KJ加强表情自然不崩脸_1927553770740146177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_136

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json、平台全量/Unianimate转绘跳舞视频_1926976453735272449.json、视频生成/图生视频/360度旋转效果Wan2.1_1922551848883077121.json、视频生成/文生视频/【丝滑补帧】Wan2.1 图生视频  KJ加强表情自然不崩脸_1927553770740146177.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `WanVideoExperimentalArgs` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoTeaCache` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `ReActorFaceSwap` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/4 个有
- `WanVideoUniAnimatePoseInput` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
