---
name: unknown_workflow_video_lora_sampler_444
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.854
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk With Sa2VA 多人_1988439303661469698.json, 视频生成/图生视频/InfiniteTalk单人数字人工作流_1957827307850530818.json, 视频生成/图生视频/InfiniteTalk单人数字人工作流_1957977430084481025.json, 视频生成/图生视频/InfiniteTalk图生视频数字人V3-个人使用版_1969944110868164610.json, 视频生成/图生视频/InfiniteTalk对口型_1958082253886803970.json, 视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json, 视频生成/图生视频/wanvideo_infinitetalk_单人工作流_1958061014984118274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_444

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk With Sa2VA 多人_1988439303661469698.json、视频生成/图生视频/InfiniteTalk单人数字人工作流_1957827307850530818.json、视频生成/图生视频/InfiniteTalk单人数字人工作流_1957977430084481025.json、视频生成/图生视频/InfiniteTalk图生视频数字人V3-个人使用版_1969944110868164610.json、视频生成/图生视频/InfiniteTalk对口型_1958082253886803970.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
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
- `AudioCrop` —— 6/7 个有
- `AudioSeparation` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `INTConstant` —— 5/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `WanVideoTorchCompileSettings` —— 3/7 个有
- `GetImageSizeAndCount` —— 2/7 个有
- `GetNode` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `MaskPreview+` —— 1/7 个有
- `PixaromaLabel` —— 1/7 个有
- `PixaromaResolution` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `Sa2VANodeTpl` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
