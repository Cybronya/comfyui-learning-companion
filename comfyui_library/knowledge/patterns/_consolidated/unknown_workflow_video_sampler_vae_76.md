---
name: unknown_workflow_video_sampler_vae_76
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.740286
common_nodes: [DrawViTPose, GetImageSizeAndCount, ImageResizeKJv2, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json, 视频生成/图生视频/Wan2.2 Animate姿势参考图生视频_1980564316481044481.json, 视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json, 视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json, 视频生成/图生视频/wanvideo_WanAnimate_v2-kj-小鸟摇_1977738504492961794.json, 视频生成/图生视频/全能图片V12 + WanAnimate，让你穿着勇士队球衣开跳库里之歌_1992409563280330754.json, 视频生成/图生视频/白用更新动作迁移_2051920241860591618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_76

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json、视频生成/图生视频/Wan2.2 Animate姿势参考图生视频_1980564316481044481.json、视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json、视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json、视频生成/图生视频/wanvideo_WanAnimate_v2-kj-小鸟摇_1977738504492961794.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `DrawViTPose`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 6/7 个有
- `DownloadAndLoadSAM2Model` —— 6/7 个有
- `DrawMaskOnImage` —— 6/7 个有
- `GrowMaskWithBlur` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `Sam2Segmentation` —— 6/7 个有
- `PrimitiveInt` —— 5/7 个有
- `VHS_VideoInfo` —— 5/7 个有
- `CLIPVisionLoader` —— 4/7 个有
- `CR Text` —— 4/7 个有
- `ImageFromBatch+` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `WanVideoClipVisionEncode` —— 4/7 个有
- `WanVideoLoraSelect` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `WanVideoContextOptions` —— 3/7 个有
- `WanVideoLoraSelectMulti` —— 3/7 个有
- `WanVideoSetLoRAs` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `RH_Nano_Banana2_Image2Image` —— 1/7 个有
- `SDPoseOODLoader` —— 1/7 个有
- `SDPoseOODProcessor` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
