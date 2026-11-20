---
name: unknown_workflow_video_lora_sampler_300
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.957
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MAGREF_wrapper_r2v-1Image-2Image-3Image-Y-Workflow_1936253127727173633.json, 视频生成/图生视频/MAGREF_wrapper_r2v-Y_1936010847577624578.json, 视频生成/图生视频/Wan-I2V-AccVid加速图生视频_1927906787679158274.json, 视频生成/图生视频/wan-AccVideo-I2V图生视频_1927959918765031425.json, 视频生成/图生视频/三图参考-MAGREF图生视频_1935232906484973570.json, 视频生成/图生视频/多图参考-MAGREF图生视频_1935199966057136129.json, 视频生成/图生视频/多图参考-MAGREF图生视频_1935527745462140929.json, 视频生成/图生视频/多图参考MAGREF图生视频_1936714907976912898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_300

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MAGREF_wrapper_r2v-1Image-2Image-3Image-Y-Workflow_1936253127727173633.json、视频生成/图生视频/MAGREF_wrapper_r2v-Y_1936010847577624578.json、视频生成/图生视频/Wan-I2V-AccVid加速图生视频_1927906787679158274.json、视频生成/图生视频/wan-AccVideo-I2V图生视频_1927959918765031425.json、视频生成/图生视频/三图参考-MAGREF图生视频_1935232906484973570.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `WanVideoEnhanceAVideo` —— 7/8 个有
- `ImageConcanate` —— 6/8 个有
- `ImageConcatMulti` —— 6/8 个有
- `Primitive integer [Crystools]` —— 6/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `ImageScaleDownToSize` —— 5/8 个有
- `DF_Get_image_size` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `Text Multiline` —— 4/8 个有
- `easy imageRemBg` —— 4/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `WanVideoTeaCache` —— 3/8 个有
- `WanVideoVACEModelSelect` —— 3/8 个有
- `GetImageSize` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RMBG` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
