---
name: unknown_workflow_video_lora_sampler_311
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.958429
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936253127727173633.json, 视频生成/图生视频/1936010847577624578.json, 视频生成/图生视频/1927906787679158274.json, 视频生成/图生视频/1935232906484973570.json, 视频生成/图生视频/1935199966057136129.json, 视频生成/图生视频/1935527745462140929.json, 视频生成/图生视频/1936714907976912898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_311

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1936253127727173633.json、视频生成/图生视频/1936010847577624578.json、视频生成/图生视频/1927906787679158274.json、视频生成/图生视频/1935232906484973570.json、视频生成/图生视频/1935199966057136129.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
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
- `ImageConcanate` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `Primitive integer [Crystools]` —— 6/7 个有
- `WanVideoEnhanceAVideo` —— 6/7 个有
- `ImageScaleDownToSize` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `DF_Get_image_size` —— 4/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `Text Multiline` —— 4/7 个有
- `easy imageRemBg` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `WanVideoTeaCache` —— 3/7 个有
- `WanVideoVACEModelSelect` —— 3/7 个有
- `GetImageSize` —— 2/7 个有
- `RMBG` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
