---
name: unknown_workflow_controlnet_video_lora_23
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.944833
common_nodes: [DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/202_单人图像说话（WanMultitalk）（魔方）_1948618754165997569.json, 数字人/数字人/multitalk数字人长视频生成（图片数字人）_1941654451621097473.json, 数字人/数字人/终极数字人 InfiniteTalk_1937407358828232705.json, 数字人/数字人/终极数字人 InfiniteTalk_2034291576809197569.json, 视频生成/图生视频/单人图像说话（WanMultitalk）（魔方）_1948265018342158337.json, 视频生成/图生视频/数字人加运镜_1951224914336526338.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_23

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/202_单人图像说话（WanMultitalk）（魔方）_1948618754165997569.json、数字人/数字人/multitalk数字人长视频生成（图片数字人）_1941654451621097473.json、数字人/数字人/终极数字人 InfiniteTalk_1937407358828232705.json、数字人/数字人/终极数字人 InfiniteTalk_2034291576809197569.json、视频生成/图生视频/单人图像说话（WanMultitalk）（魔方）_1948265018342158337.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 5/6 个有
- `WanVideoApplyNAG` —— 5/6 个有
- `WanVideoClipVisionEncode` —— 5/6 个有
- `WanVideoEnhanceAVideo` —— 5/6 个有
- `WanVideoTextEncodeSingle` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `AudioSeparation` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `WanVideoContextOptions` —— 4/6 个有
- `WanVideoImageToVideoEncode` —— 4/6 个有
- `WanVideoSLG` —— 4/6 个有
- `Audio Duration (mtb)` —— 3/6 个有
- `AudioCrop` —— 3/6 个有
- `RH_GetAudioDuration` —— 3/6 个有
- `WanVideoExperimentalArgs` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `RepeatImageBatch` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoImageToVideoMultiTalk` —— 2/6 个有
- `WanVideoTeaCache` —— 2/6 个有
- `FloatConstant` —— 1/6 个有
- `Int` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `WanVideoTextEncode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
