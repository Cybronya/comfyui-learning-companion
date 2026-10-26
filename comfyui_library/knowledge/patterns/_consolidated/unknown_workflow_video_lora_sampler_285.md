---
name: unknown_workflow_video_lora_sampler_285
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6195
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json, 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json, 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json, 数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json, 数字人/数字人/infinite Talk数字人_支持音色克隆_1959597341462441985.json, 数字人/数字人/wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786.json, 数字人/数字人/wanvideo_infinitetalk_单人工作流_1988849254452039682.json, 数字人/数字人/全网首发——Aiwood-infinitetalk_视频改口型工作流_1958066987350052865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_285

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json、数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json、数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json、数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json、数字人/数字人/infinite Talk数字人_支持音色克隆_1959597341462441985.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 7/8 个有
- `AudioSeparation` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `INTConstant` —— 6/8 个有
- `ImageConcatMulti` —— 5/8 个有
- `SimpleMath+` —— 4/8 个有
- `SoundFlow_GetLength` —— 4/8 个有
- `ToInt` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `easy int` —— 4/8 个有
- `Display Int (rgthree)` —— 3/8 个有
- `Bjornulf_ShowFloat` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Display Any (rgthree)` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `IndexTTSNode` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `WanVideoImageToVideoEncode` —— 1/8 个有
- `WanVideoTorchCompileSettings` —— 1/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/8 个有
- `WanVideoUni3C_embeds` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
