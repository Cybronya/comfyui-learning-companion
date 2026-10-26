---
name: unknown_workflow_video_lora_sampler_501
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9174
common_nodes: [CR SDXL Aspect Ratio, CR Text, Fast Groups Bypasser (rgthree), ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2运镜控制(KJ)_1957349808384176130.json, 视频生成/图生视频/Wan2.2长视频生成(KJ)15秒以上_1957714010304249858.json, 视频生成/图生视频/Wan2.2长视频生成20秒以上_1970311632809304066.json, 视频生成/图生视频/Wan2.2长视频生成_1969679472318443521.json, 视频生成/图生视频/一键生成飞行长视频(30秒以上)_1960259311396139009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_501

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2运镜控制(KJ)_1957349808384176130.json、视频生成/图生视频/Wan2.2长视频生成(KJ)15秒以上_1957714010304249858.json、视频生成/图生视频/Wan2.2长视频生成20秒以上_1970311632809304066.json、视频生成/图生视频/Wan2.2长视频生成_1969679472318443521.json、视频生成/图生视频/一键生成飞行长视频(30秒以上)_1960259311396139009.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CR SDXL Aspect Ratio`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 4/5 个有
- `DF_Int_to_Float` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `ImageBatch` —— 4/5 个有
- `ImageFromBatch+` —— 4/5 个有
- `LoadAudio` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `WanVideoClipVisionEncode` —— 4/5 个有
- `WanVideoLoraSelectMulti` —— 4/5 个有
- `ADE_CameraPoseBasic` —— 1/5 个有
- `WanVideoFunCameraEmbeds` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
