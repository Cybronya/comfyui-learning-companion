---
name: unknown_workflow_video_lora_sampler_485
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.951
common_nodes: [CLIPVisionLoader, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MAGREF单图参考图生视频_1935517982800150530.json, 视频生成/图生视频/b站开源动漫视频生成模型 ani全能视频S_1944781306624397314.json, 视频生成/图生视频/wan2.1 MAGREF 3倍加速图生视频_1941396132272750594.json, 视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json, 视频生成/图生视频/电商产品360旋转_1941330850711814145.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_485

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MAGREF单图参考图生视频_1935517982800150530.json、视频生成/图生视频/b站开源动漫视频生成模型 ani全能视频S_1944781306624397314.json、视频生成/图生视频/wan2.1 MAGREF 3倍加速图生视频_1941396132272750594.json、视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json、视频生成/图生视频/电商产品360旋转_1941330850711814145.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `WanVideoEnhanceAVideo` —— 4/5 个有
- `WanVideoTextEncode` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `DF_Integer` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `WanVideoSLG` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `WanVideoExperimentalArgs` —— 2/5 个有
- `easy imageRemBg` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `WanVideoSetBlockSwap` —— 1/5 个有
- `WanVideoSetLoRAs` —— 1/5 个有
- `WanVideoTextEncodeCached` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
