---
name: unknown_workflow_video_sampler_vae_68
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.926625
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/API-数字人-InfiniteTalk-单人对口型工作流_2059537663195172866.json, 数字人/数字人/I2V-InfiniteTalk双人数字人_2002787606607872002.json, 数字人/数字人/InfiniteTalk 图片生成单人唱歌视频（不限生成时长、批次提示词）_1958583900547268610.json, 数字人/数字人/InfiniteTalk数字人图生语音视频_1964942874242633729.json, 数字人/数字人/数字人-InfiniteTalk-单人对口型工作流_1978436503875555329.json, 视频生成/图生视频/I2V-InfiniteTalk双人数字人_1985223003455823873.json, 视频生成/图生视频/InfiniTetalk 双人音频+图片数字人 配音必备神器_1998620412286238722.json, 视频生成/图生视频/双人_多人数字人对话对口型_2055645162226896897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_68

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/API-数字人-InfiniteTalk-单人对口型工作流_2059537663195172866.json、数字人/数字人/I2V-InfiniteTalk双人数字人_2002787606607872002.json、数字人/数字人/InfiniteTalk 图片生成单人唱歌视频（不限生成时长、批次提示词）_1958583900547268610.json、数字人/数字人/InfiniteTalk数字人图生语音视频_1964942874242633729.json、数字人/数字人/数字人-InfiniteTalk-单人对口型工作流_1978436503875555329.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelectMulti` —— 6/8 个有
- `Audio Duration (mtb)` —— 5/8 个有
- `ImageResizeKJv2` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Getter` —— 4/8 个有
- `LayerUtility: PurgeVRAM V2` —— 4/8 个有
- `MathExpression|pysssss` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `Setter` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `PreviewAudio` —— 3/8 个有
- `QZ_ResolutionPreset` —— 3/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `WanVideoLoraSelect` —— 2/8 个有
- `INTConstant` —— 1/8 个有
- `ImageCASharpening+` —— 1/8 个有
- `ImageFromBatch+` —— 1/8 个有
- `Int` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `VHS_VideoInfoLoaded` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
