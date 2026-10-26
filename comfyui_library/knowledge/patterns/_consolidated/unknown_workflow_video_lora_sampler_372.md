---
name: unknown_workflow_video_lora_sampler_372
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.960857
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinitetalk图片单人对口型_1990376514787172354.json, 视频生成/图生视频/口播唱歌数字人InfiniteTalk 对口型_1970330754632851457.json, "视频生成/图生视频/图加音频生视频,非常丝滑，支持160秒_2044837678058835969.json", 视频生成/图生视频/图加音频生视频_2016326225295314946.json, 视频生成/图生视频/图加音频生视频——V1_2018257190561255426.json, 视频生成/图生视频/图生视频-基于InfiniteTalk_2005465061298761730.json, 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_372

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/infinitetalk图片单人对口型_1990376514787172354.json、视频生成/图生视频/口播唱歌数字人InfiniteTalk 对口型_1970330754632851457.json、视频生成/图生视频/图加音频生视频,非常丝滑，支持160秒_2044837678058835969.json、视频生成/图生视频/图加音频生视频_2016326225295314946.json、视频生成/图生视频/图加音频生视频——V1_2018257190561255426.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 6/7 个有
- `AudioSeparation` —— 6/7 个有
- `INTConstant` —— 5/7 个有
- `LoadWanVideoT5TextEncoder` —— 4/7 个有
- `WanVideoTextEncode` —— 4/7 个有
- `Anything Everywhere` —— 3/7 个有
- `WanVideoTextEncodeCached` —— 3/7 个有
- `Audio Duration (mtb)` —— 2/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `ttN seed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
