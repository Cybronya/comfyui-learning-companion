---
name: unknown_workflow_controlnet_video_lora_17
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.945167
common_nodes: [DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/202_单人图像说话（WanMultitalk）（魔方）_1948618754165997569.json, 数字人/数字人/multitalk数字人长视频生成（图片数字人）_1941654451621097473.json, 数字人/数字人/终极数字人 InfiniteTalk_1937407358828232705.json, 数字人/数字人/终极数字人 InfiniteTalk_2034291576809197569.json, 视频生成/图生视频/Ai女友唱歌对口型=Multitalk=艾橘溪_1937138982268379137.json, 视频生成/图生视频/单人图像说话（WanMultitalk）（魔方）_1948265018342158337.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/202_单人图像说话（WanMultitalk）（魔方）_1948618754165997569.json、数字人/数字人/multitalk数字人长视频生成（图片数字人）_1941654451621097473.json、数字人/数字人/终极数字人 InfiniteTalk_1937407358828232705.json、数字人/数字人/终极数字人 InfiniteTalk_2034291576809197569.json、视频生成/图生视频/Ai女友唱歌对口型=Multitalk=艾橘溪_1937138982268379137.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

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
- `WanVideoClipVisionEncode` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `AudioSeparation` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `WanVideoApplyNAG` —— 4/6 个有
- `WanVideoContextOptions` —— 4/6 个有
- `WanVideoEnhanceAVideo` —— 4/6 个有
- `WanVideoImageToVideoEncode` —— 4/6 个有
- `WanVideoSLG` —— 4/6 个有
- `WanVideoTextEncodeSingle` —— 4/6 个有
- `JWInteger` —— 3/6 个有
- `RH_GetAudioDuration` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `Audio Duration (mtb)` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `RepeatImageBatch` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoExperimentalArgs` —— 2/6 个有
- `WanVideoImageToVideoMultiTalk` —— 2/6 个有
- `WanVideoTeaCache` —— 2/6 个有
- `WanVideoTextEncode` —— 2/6 个有
- `Int` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
