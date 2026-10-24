---
name: unknown_workflow_video_lora_sampler_196
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9661
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinitetalk图片单人对口型_1990376514787172354.json, 视频生成/图生视频/口播唱歌数字人InfiniteTalk 对口型_1970330754632851457.json, 视频生成/图生视频/唱歌数字人infinitetalk优化版一比一支持_2023308778170490881.json, 视频生成/图生视频/对嘴型·数字人·影视·唱歌·讲话对口型·超自然现实有喘息细节_2015414691312443393.json, 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json, 视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V2.0_1968840482644217858.json, 视频生成/图生视频/粤语唱歌数字人infinitetalk优化版一比一支持_1961790376648622081.json, 视频生成/图生视频/粤语唱歌数字人infinitetalk优化版一比一支持_1964962986404270082.json, 视频生成/图生视频/粤语唱歌数字人infinitetalk优化版一比一支持_1968298118544535553.json, 音频生成/音频生成/infinitetalk优化版一比一音色数字人_1958195688268054529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_196

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/infinitetalk图片单人对口型_1990376514787172354.json、视频生成/图生视频/口播唱歌数字人InfiniteTalk 对口型_1970330754632851457.json、视频生成/图生视频/唱歌数字人infinitetalk优化版一比一支持_2023308778170490881.json、视频生成/图生视频/对嘴型·数字人·影视·唱歌·讲话对口型·超自然现实有喘息细节_2015414691312443393.json、视频生成/图生视频/目前最新最火InfiniteTalk数字人对口型，适合口播唱歌 V1.0_1961819630828503041.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `AudioSeparation` —— 9/10 个有
- `INTConstant` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `IndexTTSRun` —— 5/10 个有
- `MultiLinePromptIndex` —— 5/10 个有
- `SaveAudioMP3` —— 5/10 个有
- `Audio Duration (mtb)` —— 3/10 个有
- `ImageFromBatch+` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `GetImageSizeAndCount` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `ttN seed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
