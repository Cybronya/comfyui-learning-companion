---
name: unknown_workflow_video_sampler_vae_175
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.945
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTextEmbedBridge, HyVideoTorchCompileSettings, HyVideoVAELoader, ImageConcatMulti, ImageResizeKJv2, LoadImage, PreviewImage, TextEncodeHunyuanVideo_ImageToVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/Hunyuan Video Custom_1920756422236377089.json, 视频生成/图生视频/Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_175

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Hunyuan Video Custom_1920756422236377089.json、视频生成/图生视频/Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `HyVideoBlockSwap`
- `HyVideoDecode`
- `HyVideoEncode`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoTextEmbedBridge`
- `HyVideoTorchCompileSettings`
- `HyVideoVAELoader`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `HunyuanVideoFresca` —— 1/2 个有
- `HunyuanVideoSLG` —— 1/2 个有
- `Image Crop Face` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `Images to RGB` —— 1/2 个有
- `LayerMask: TransparentBackgroundUltra` —— 1/2 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
