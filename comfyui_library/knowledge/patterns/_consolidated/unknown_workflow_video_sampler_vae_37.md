---
name: unknown_workflow_video_sampler_vae_37
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.816909
common_nodes: [ImageResizeKJ, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1-Fun-Reward-LoRAs_1910678693197611009.json, 平台全量/Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265.json, 平台全量/Wan2.1-Fun-视频转绘_1906003085112561666.json, 平台全量/Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658.json, 平台全量/Wan2.1-Fun-首尾帧_1905531418771132418.json, 平台全量/【Wan2.1系列】一张照片复刻爆款手势舞全流程丨深度+姿势+边缘控制生成视频_1921087918020968449.json, 视频生成/图生视频/Wan2.1-Fun-视频驱动图片_1909246222736236546.json, 视频生成/图生视频/Wan2.1-UniAnimate-视频驱动图片_1913807733877895170.json, 视频生成/图生视频/Wan2.1_funcontrol14b_1948931774743814145.json, 视频生成/图生视频/图片+骨骼视频迁移姿势跳舞动作迁移视频迁移_1949337300036661249.json, 视频生成/图生视频/电商图片转视频_1922211911637614594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_37

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Wan2.1-Fun-Reward-LoRAs_1910678693197611009.json、平台全量/Wan2.1-Fun-视频转绘(线类+深度)_1906981394893963265.json、平台全量/Wan2.1-Fun-视频转绘_1906003085112561666.json、平台全量/Wan2.1-Fun-视频转绘（图生视频）_1906019294621126658.json、平台全量/Wan2.1-Fun-首尾帧_1905531418771132418.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `WanVideoBlockSwap` —— 10/11 个有
- `WanVideoControlEmbeds` —— 10/11 个有
- `WanVideoEncode` —— 10/11 个有
- `WanVideoEnhanceAVideo` —— 10/11 个有
- `WanVideoSLG` —— 10/11 个有
- `WanVideoClipVisionEncode` —— 9/11 个有
- `WanVideoImageToVideoEncode` —— 9/11 个有
- `WanVideoLoraSelect` —— 9/11 个有
- `AIO_Preprocessor` —— 8/11 个有
- `Florence2ModelLoader` —— 8/11 个有
- `Florence2Run` —— 8/11 个有
- `LoadWanVideoClipTextEncoder` —— 8/11 个有
- `WanVideoTorchCompileSettings` —— 8/11 个有
- `KepStringLiteral` —— 6/11 个有
- `LayerUtility: PurgeVRAM` —— 6/11 个有
- `GetNode` —— 4/11 个有
- `ImageBlend` —— 4/11 个有
- `PreviewImage` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `GetImageSizeAndCount` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `Anything Everywhere` —— 2/11 个有
- `CLIPVisionLoader` —— 2/11 个有
- `DisplayAny` —— 2/11 个有
- `ImagePadForOutpaint` —— 2/11 个有
- `ImageResize+` —— 2/11 个有
- `WanVideoEmptyEmbeds` —— 2/11 个有
- `WanVideoUniAnimateDWPoseDetector` —— 2/11 个有
- `WanVideoUniAnimatePoseInput` —— 2/11 个有
- `CR Upscale Image` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/11 个有
- `RIFE VFI` —— 1/11 个有
- `ReActorFaceSwap` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
