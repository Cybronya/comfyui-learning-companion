---
name: unknown_workflow_video_lora_sampler_307
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.922857
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageConcanate, ImageConcatMulti, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PDIMAGE_LongerSize, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/1947482709851525122.json, 视频生成/图生视频/1935281267648954369.json, 视频生成/图生视频/1942037582668840961.json, 视频生成/图生视频/1935538353750069250.json, 视频生成/图生视频/1935677358408200194.json, 视频生成/图生视频/1935239165498032130.json, 视频生成/图生视频/1935550198397730818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_307

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1947482709851525122.json、视频生成/图生视频/1935281267648954369.json、视频生成/图生视频/1942037582668840961.json、视频生成/图生视频/1935538353750069250.json、视频生成/图生视频/1935677358408200194.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PDIMAGE_LongerSize`
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
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 6/7 个有
- `Primitive integer [Crystools]` —— 6/7 个有
- `Text Multiline` —— 4/7 个有
- `RH_Translator` —— 3/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
