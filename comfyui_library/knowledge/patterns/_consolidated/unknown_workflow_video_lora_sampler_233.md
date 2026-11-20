---
name: unknown_workflow_video_lora_sampler_233
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.909778
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageConcanate, ImageConcatMulti, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, PDIMAGE_LongerSize, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/MAGREF最强图像编辑加速6图版V1_1935302402784559106.json, 视频生成/图生视频/LightX2V RANK128人&物体高一致性 双图融合超级加速视频生成_1947482709851525122.json, 视频生成/图生视频/MAGREF 人+物体一致性LightX2V 5步超级加速视频编辑V1_1935281267648954369.json, 视频生成/图生视频/MAGREF+LIGHTX2V保留图像id生成视频（双图）+视频放大_1942037582668840961.json, 视频生成/图生视频/MAGREF+LightX2V 超级加速视频编辑_1935538353750069250.json, 视频生成/图生视频/MAGREF+light2V快速视频编辑模型_1935677358408200194.json, 视频生成/图生视频/MAGREF双人一致性LightX2V 5步超级加速视频编辑V1_1935239165498032130.json, 视频生成/图生视频/MAGREF图像编辑支持NAG负面提示词_1935507618146484226.json, 视频生成/图生视频/WAN MAGREF 电商带货实战，人&物体高度一致性LightX2V 超级加速视频生成_1935550198397730818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_233

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/MAGREF最强图像编辑加速6图版V1_1935302402784559106.json、视频生成/图生视频/LightX2V RANK128人&物体高一致性 双图融合超级加速视频生成_1947482709851525122.json、视频生成/图生视频/MAGREF 人+物体一致性LightX2V 5步超级加速视频编辑V1_1935281267648954369.json、视频生成/图生视频/MAGREF+LIGHTX2V保留图像id生成视频（双图）+视频放大_1942037582668840961.json、视频生成/图生视频/MAGREF+LightX2V 超级加速视频编辑_1935538353750069250.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `WanVideoTextEncode` —— 8/9 个有
- `JWInteger` —— 7/9 个有
- `Primitive integer [Crystools]` —— 7/9 个有
- `Text Multiline` —— 5/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `RH_Translator` —— 3/9 个有
- `ImageBatchMulti` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `WanVideoApplyNAG` —— 1/9 个有
- `WanVideoTextEncodeSingle` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
