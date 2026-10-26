---
name: unknown_workflow_video_sampler_vae_30
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.961667
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/IndexTTS 1.5 +InfiniteTalk数字人_1983435435332575234.json, 视频生成/图生视频/Infinite talk 唱歌数字人_1997484530254680066.json, 视频生成/图生视频/Infinite talk数字人_1987166609188040706.json, 视频生成/图生视频/InfiniteTalk 图片生成单人唱歌视频（不限生成时长）_1957828185982599170.json, 视频生成/图生视频/InfiniteTalk-图片唱歌 单人数字人工作流_2086309319305424897.json, 视频生成/图生视频/InfiniteTalk单人数字人对口型_1998953194820620290.json, 视频生成/图生视频/InfiniteTalk图片对口型工作流_2070420975967100929.json, 视频生成/图生视频/InfiniteTalk数字人双人对口型_1998964761461186561.json, 视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json, 视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2044647085147951105.json, 视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2073622937676115969.json, 视频生成/图生视频/多角色数字人 InfiniteTalk 多人对口型 说话对话唱歌_2029363209500626945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/IndexTTS 1.5 +InfiniteTalk数字人_1983435435332575234.json、视频生成/图生视频/Infinite talk 唱歌数字人_1997484530254680066.json、视频生成/图生视频/Infinite talk数字人_1987166609188040706.json、视频生成/图生视频/InfiniteTalk 图片生成单人唱歌视频（不限生成时长）_1957828185982599170.json、视频生成/图生视频/InfiniteTalk-图片唱歌 单人数字人工作流_2086309319305424897.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 11/12 个有
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `LoadWanVideoT5TextEncoder` —— 8/12 个有
- `WanVideoTextEncode` —— 8/12 个有
- `PreviewImage` —— 7/12 个有
- `WanVideoLoraSelectMulti` —— 7/12 个有
- `PreviewAudio` —— 5/12 个有
- `WanVideoLoraSelect` —— 5/12 个有
- `INTConstant` —— 4/12 个有
- `ImageResizeKJv2` —— 4/12 个有
- `LayerMask: MaskPreview` —— 4/12 个有
- `SeparateMasks` —— 4/12 个有
- `WanVideoTextEncodeCached` —— 4/12 个有
- `GetImageSizeAndCount` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `IndexTTSNode` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `VHS_LoadVideo` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
