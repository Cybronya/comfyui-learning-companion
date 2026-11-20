---
name: unknown_workflow_video_upscale_lora_12
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.601
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, ImageResizeKJ, ImageSmartSharpen+, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SeargePromptText, SetNode, ShowText|pysssss, SimpleCondition+, VHS_VideoCombine, Video_Upscale_With_Model, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【FusionX】图生视频-kj 8步加速版_1935512780151914497.json, 视频生成/图生视频/🈚️i2v图生视频-kj版-wan 2.1 fusionX_1934976240954875906.json, 视频生成/图生视频/🈚️运镜控制-图生视频+Lightx2v+Fun-wan-720p_1947363483677511682.json, 视频生成/图生视频/🈚️首尾帧-FLF2V-kj-Lightx2v-wan-720p_1947347376895840258.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/【FusionX】图生视频-kj 8步加速版_1935512780151914497.json、视频生成/图生视频/🈚️i2v图生视频-kj版-wan 2.1 fusionX_1934976240954875906.json、视频生成/图生视频/🈚️运镜控制-图生视频+Lightx2v+Fun-wan-720p_1947363483677511682.json、视频生成/图生视频/🈚️首尾帧-FLF2V-kj-Lightx2v-wan-720p_1947347376895840258.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageResizeKJ`
- `ImageSmartSharpen+`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SeargePromptText`
- `SetNode`
- `ShowText|pysssss`
- `SimpleCondition+`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `WanVideoClipVisionEncode` —— 3/4 个有
- `WanVideoFreeInitArgs` —— 3/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `WanVideoEasyCache` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `WanVideoSetRadialAttention` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ADE_CameraPoseBasic` —— 1/4 个有
- `CameraPoseVisualizer` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoadWanVideoClipTextEncoder` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `WanVideoFunCameraEmbeds` —— 1/4 个有
- `WanVideoMagCache` —— 1/4 个有
- `WanVideoTeaCache` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
