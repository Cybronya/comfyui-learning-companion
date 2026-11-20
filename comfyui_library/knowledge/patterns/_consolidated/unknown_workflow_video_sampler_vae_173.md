---
name: unknown_workflow_video_sampler_vae_173
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.939667
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, HyVideoBlockSwap, HyVideoDecode, HyVideoEncode, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoTextEmbedBridge, HyVideoTorchCompileSettings, HyVideoVAELoader, ImageConcatMulti, ImageResizeKJv2, LoadImage, PreviewImage, TextEncodeHunyuanVideo_ImageToVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/Hunyuan Video Custom_1920756422236377089.json, 平台全量/【两张照片秒变情侣甜蜜视频】手把手教你搭建混元Custom工作流_1935587393103921153.json, 视频生成/图生视频/Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Hunyuan Video Custom_1920756422236377089.json、平台全量/【两张照片秒变情侣甜蜜视频】手把手教你搭建混元Custom工作流_1935587393103921153.json、视频生成/图生视频/Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
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
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `HunyuanVideoFresca` —— 1/3 个有
- `HunyuanVideoSLG` —— 1/3 个有
- `Image Crop Face` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `Images to RGB` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerMask: TransparentBackgroundUltra` —— 1/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有
- `LayerUtility: TextBox` —— 1/3 个有
- `RMBG` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
