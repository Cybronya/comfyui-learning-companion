---
name: unknown_workflow_video_sampler_vae_14
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.95375
common_nodes: [CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AI数字人-动物_2084929827878031362.json, 视频生成/图生视频/Infinite Talk数字人图生视频流V2极速版_2073246385209700353.json, 视频生成/图生视频/Infinite Talk数字人图生视频流双人版_2073246674415349762.json, 视频生成/图生视频/Infinite talk 唱歌数字人_1997484530254680066.json, 视频生成/图生视频/Infinite+Talk图生视频数字人（双人版）_1958063092703907841.json, 视频生成/图生视频/InfiniteTalk 双人版对话图片数字人不限时长_1960601741647634434.json, 视频生成/图生视频/InfiniteTalk单人数字人对口型_1998953194820620290.json, 视频生成/图生视频/InfiniteTalk图片对口型工作流_2070420975967100929.json, 视频生成/图生视频/InfiniteTalk数字人双人对口型_1998964761461186561.json, 视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2044647085147951105.json, 视频生成/图生视频/多人对口型 图生视频 数字人 InfiniteTalk 音频驱动 动作模仿_2073622937676115969.json, 视频生成/图生视频/多角色数字人 InfiniteTalk 多人对口型 说话对话唱歌_2029363209500626945.json, 视频生成/图生视频/数字人-InfiniteTalk-单人对口型工作流_2051262997816983554.json, 视频生成/图生视频/数字人-InfiniteTalk-多人对口型工作流_2051497728395489282.json, 视频生成/文生视频/图生视频 数字人 InfiniteTalk 多人对口型 动作模仿_2044640516272295938.json, 音频生成/音频生成/标准版图生单多人讲话工作流_2030914032869318658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/AI数字人-动物_2084929827878031362.json、视频生成/图生视频/Infinite Talk数字人图生视频流V2极速版_2073246385209700353.json、视频生成/图生视频/Infinite Talk数字人图生视频流双人版_2073246674415349762.json、视频生成/图生视频/Infinite talk 唱歌数字人_1997484530254680066.json、视频生成/图生视频/Infinite+Talk图生视频数字人（双人版）_1958063092703907841.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `AudioCrop` —— 15/16 个有
- `AudioSeparation` —— 15/16 个有
- `DownloadAndLoadWav2VecModel` —— 15/16 个有
- `LoadWanVideoT5TextEncoder` —— 12/16 个有
- `WanVideoTextEncode` —— 12/16 个有
- `WanVideoTorchCompileSettings` —— 11/16 个有
- `PreviewAudio` —— 10/16 个有
- `PreviewImage` —— 10/16 个有
- `WanVideoLoraSelect` —— 8/16 个有
- `WanVideoLoraSelectMulti` —— 8/16 个有
- `LayerMask: MaskPreview` —— 6/16 个有
- `SeparateMasks` —— 6/16 个有
- `JWInteger` —— 4/16 个有
- `WanVideoTextEncodeCached` —— 4/16 个有
- `CR Prompt Text` —— 3/16 个有
- `easy cleanGpuUsed` —— 2/16 个有
- `Audio Duration` —— 1/16 个有
- `ComfyMathExpression` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `LogicUtil_CeilNode` —— 1/16 个有
- `Wav2VecModelLoader` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
