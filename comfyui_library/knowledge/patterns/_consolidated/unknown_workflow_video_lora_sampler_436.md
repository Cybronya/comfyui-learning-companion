---
name: unknown_workflow_video_lora_sampler_436
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.573143
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetNode, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json, 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json, 数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json, 数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json, 数字人/数字人/infinite Talk数字人_支持音色克隆_1959597341462441985.json, 数字人/数字人/wanvideo_infinitetalk_单人图像对口型（最强Z）_1965433292562550786.json, 数字人/数字人/wanvideo_infinitetalk_单人工作流_1988849254452039682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_436

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Wanvideo_infinitetalk_图片对口型_单人工作流_1974020465935167490.json、数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流-数字人-多人唱歌_2005284337660690434.json、数字人/数字人/Wanvideo_infinitetalk_图片对口型_双人工作流_1974013116696629250.json、数字人/数字人/Wanvideo_infinitetalk_视频对口型_单人工作流_1973646117596434433.json、数字人/数字人/infinite Talk数字人_支持音色克隆_1959597341462441985.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
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
- `AudioCrop` —— 6/7 个有
- `AudioSeparation` —— 6/7 个有
- `INTConstant` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `SimpleMath+` —— 3/7 个有
- `SoundFlow_GetLength` —— 3/7 个有
- `ToInt` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `easy int` —— 3/7 个有
- `Bjornulf_ShowFloat` —— 2/7 个有
- `Display Int (rgthree)` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `IndexTTSNode` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
