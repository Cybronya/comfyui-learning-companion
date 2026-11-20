---
name: unknown_workflow_video_lora_sampler_518
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9515
common_nodes: [CLIPVisionLoader, ImageConcanate, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MAGREF_wrapper_r2v-1Image-2Image-3Image-Y-Workflow_1936253127727173633.json, 视频生成/图生视频/MAGREF_wrapper_r2v-Y_1936010847577624578.json, 视频生成/图生视频/三图参考-MAGREF图生视频_1935232906484973570.json, 视频生成/图生视频/多图参考-MAGREF图生视频_1935199966057136129.json, 视频生成/图生视频/多图参考-MAGREF图生视频_1935527745462140929.json, 视频生成/图生视频/多图参考MAGREF图生视频_1936714907976912898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_518

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MAGREF_wrapper_r2v-1Image-2Image-3Image-Y-Workflow_1936253127727173633.json、视频生成/图生视频/MAGREF_wrapper_r2v-Y_1936010847577624578.json、视频生成/图生视频/三图参考-MAGREF图生视频_1935232906484973570.json、视频生成/图生视频/多图参考-MAGREF图生视频_1935199966057136129.json、视频生成/图生视频/多图参考-MAGREF图生视频_1935527745462140929.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleDownToSize` —— 5/6 个有
- `Primitive integer [Crystools]` —— 5/6 个有
- `DF_Get_image_size` —— 4/6 个有
- `GetImageSizeAndCount` —— 4/6 个有
- `Text Multiline` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `easy imageRemBg` —— 4/6 个有
- `WanVideoTeaCache` —— 3/6 个有
- `WanVideoVACEModelSelect` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `RMBG` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
