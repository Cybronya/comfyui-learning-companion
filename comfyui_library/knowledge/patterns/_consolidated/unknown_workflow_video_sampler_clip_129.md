---
name: unknown_workflow_video_sampler_clip_129
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7828
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1-Fun-视频驱动图片_1909246222736236546.json, 视频生成/图生视频/Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json, 视频生成/图生视频/Wan2.1_funcontrol14b_1948931774743814145.json, 视频生成/图生视频/图片+骨骼视频迁移姿势跳舞动作迁移视频迁移_1949337300036661249.json, 视频生成/图生视频/电商图片转视频_1922211911637614594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-Fun-视频驱动图片_1909246222736236546.json、视频生成/图生视频/Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json、视频生成/图生视频/Wan2.1_funcontrol14b_1948931774743814145.json、视频生成/图生视频/图片+骨骼视频迁移姿势跳舞动作迁移视频迁移_1949337300036661249.json、视频生成/图生视频/电商图片转视频_1922211911637614594.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 4/5 个有
- `Florence2Run` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `WanVideoControlEmbeds` —— 4/5 个有
- `WanVideoEncode` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `AIO_Preprocessor` —— 2/5 个有
- `Anything Everywhere` —— 2/5 个有
- `DisplayAny` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `KepStringLiteral` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `WanVideoUniAnimateDWPoseDetector` —— 2/5 个有
- `WanVideoUniAnimatePoseInput` —— 2/5 个有
- `CLIPVisionLoader` —— 1/5 个有
- `CR Upscale Image` —— 1/5 个有
- `ImageBlend` —— 1/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `ReActorFaceSwap` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
