---
name: unknown_workflow_controlnet_video_lora_18
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.591167
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_DuplicateImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/203_双人图像说话（WanMultitalk）（魔方）_1948788303240339458.json, 数字人/数字人/MV制作——抖音，汽水音乐，网易音乐签单_2046592658432331778.json, 数字人/数字人/wanvideo_multitalk+多角色对话工作流_1945059660426858498.json, 视频生成/图生视频/MV制作——Multitalk 声音驱动视频生成_1949675886216925185.json, 视频生成/图生视频/Multitalk双人对话--生成超长视频_1948575951367090178.json, 视频生成/图生视频/wanvideo_multitalk+多角色对话工作流_1973607511070781441.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_18

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/203_双人图像说话（WanMultitalk）（魔方）_1948788303240339458.json、数字人/数字人/MV制作——抖音，汽水音乐，网易音乐签单_2046592658432331778.json、数字人/数字人/wanvideo_multitalk+多角色对话工作流_1945059660426858498.json、视频生成/图生视频/MV制作——Multitalk 声音驱动视频生成_1949675886216925185.json、视频生成/图生视频/Multitalk双人对话--生成超长视频_1948575951367090178.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `LayerUtility: PurgeVRAM V2` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `WanVideoEnhanceAVideo` —— 5/6 个有
- `Audio Duration (mtb)` —— 4/6 个有
- `GroundingDinoModelLoader (segment anything)` —— 4/6 个有
- `GroundingDinoSAMSegment (segment anything)` —— 4/6 个有
- `GrowMaskWithBlur` —— 4/6 个有
- `Image To Mask` —— 4/6 个有
- `LayerUtility: PurgeVRAM` —— 4/6 个有
- `MaskToImage` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `PreviewAudio` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `SAMLoader` —— 4/6 个有
- `Separate Mask Components` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `LoadAudio` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `VHS_LoadAudioUpload` —— 3/6 个有
- `AudioCrop` —— 2/6 个有
- `RH_GetAudioDuration` —— 2/6 个有
- `Int` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `SeparateMasks` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `WanVideoTorchCompileSettings` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
