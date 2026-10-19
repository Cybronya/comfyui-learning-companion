---
name: unknown_workflow_video_lora_sampler_137
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.788333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936345879362310145.json, 视频生成/图生视频/1936304565509607426.json, 视频生成/图生视频/1936341490123837441.json, 视频生成/图生视频/1940606353897402370.json, 视频生成/图生视频/1937864518498455553.json, 视频生成/图生视频/1940356622893953026.json, 视频生成/图生视频/1937674986381295618.json, 视频生成/图生视频/1945034637402099713.json, 视频生成/文生视频/1936951987776704514.json, 视频生成/文生视频/1947944588175650817.json, 视频生成/文生视频/1937688906760654850.json, 音频生成/音频生成/Multitalk+aniwan数字人，可说话演讲可唱歌_1949746352932741121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_137

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1936345879362310145.json、视频生成/图生视频/1936304565509607426.json、视频生成/图生视频/1936341490123837441.json、视频生成/图生视频/1940606353897402370.json、视频生成/图生视频/1937864518498455553.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWIntegerToString` —— 11/12 个有
- `WanVideoClipVisionEncode` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `PrimitiveInt` —— 9/12 个有
- `easy cleanGpuUsed` —— 9/12 个有
- `Audio Duration (mtb)` —— 8/12 个有
- `JWInteger` —— 8/12 个有
- `LayerUtility: PurgeVRAM` —— 8/12 个有
- `PrimitiveFloat` —— 8/12 个有
- `TextInput_` —— 8/12 个有
- `WanVideoEncode` —— 6/12 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/12 个有
- `WanVideoUni3C_embeds` —— 6/12 个有
- `ImageResizeKJ` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `LayerUtility: PurgeVRAM V2` —— 4/12 个有
- `WanVideoContextOptions` —— 4/12 个有
- `CR Text` —— 3/12 个有
- `VHS_DuplicateImages` —— 3/12 个有
- `WanVideoTorchCompileSettings` —— 3/12 个有
- `INTConstant` —— 2/12 个有
- `Int` —— 2/12 个有
- `WanVideoEasyCache` —— 2/12 个有
- `WanVideoEnhanceAVideo` —— 2/12 个有
- `WanVideoExperimentalArgs` —— 2/12 个有
- `WanVideoFreeInitArgs` —— 2/12 个有
- `WanVideoSLG` —— 2/12 个有
- `WanVideoSetRadialAttention` —— 2/12 个有
- `easy anythingIndexSwitch` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `PreviewAudio` —— 1/12 个有
- `RH_Captioner` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
