---
name: unknown_workflow_video_lora_sampler_78
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.956286
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json, 视频生成/图生视频/Wan2.1 InfiniteTalk 单人版_1990298374261927937.json, 视频生成/图生视频/Wan双人对口型不需要遮罩_2042473229025021954.json, 视频生成/图生视频/infinitetalk 单人音频驱动 对口型 数字人_2038129720084140034.json, 视频生成/图生视频/infinitetalk 对口型 数字人 单人音频驱动_2039686638024003585.json, 视频生成/图生视频/infinitetalk 音频驱动 对口型 数字人_2038259769424744450.json, 视频生成/图生视频/infinitetalk 音频驱动 对口型 数字人_2043221914818191361.json, 视频生成/图生视频/infinitetalk-workflow_2101559918137536513.json, 视频生成/图生视频/infinitetalk单人-I2V-720p-竖屏_1958721721454981121.json, 视频生成/图生视频/infinitetalk单人-表达式科技AIGC_1993155666919571457.json, 视频生成/图生视频/infinitetalk单人_1957826962256658434.json, 视频生成/图生视频/infinitetalk单人_2044669894783934465.json, 视频生成/图生视频/infinitetalk单人图像对口型_1983851965690056706.json, 视频生成/图生视频/infinitetalk单人图像数字人_1987800864440168449.json, 视频生成/图生视频/infinitetalk单人数字人 横版_2082717087134470145.json, 视频生成/图生视频/infinitetalk单人数字人_1961786018880012290.json, 视频生成/图生视频/infinitetalk图生视频数字人口播_2080575708149145601.json, 视频生成/图生视频/infinitetalk改进版单人数字人对口型_1999412008917364738.json, 视频生成/图生视频/【CQ808】infinitetalk单人对口型_2054517632375771138.json, 视频生成/图生视频/单人数字人对口型说话工作流（infinitetalk）_2044453798432739329.json, 音频生成/音频生成/数字人（图片对口型）＋声音克隆（单人_双人）_2013652200806944769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json、视频生成/图生视频/Wan2.1 InfiniteTalk 单人版_1990298374261927937.json、视频生成/图生视频/Wan双人对口型不需要遮罩_2042473229025021954.json、视频生成/图生视频/infinitetalk 单人音频驱动 对口型 数字人_2038129720084140034.json、视频生成/图生视频/infinitetalk 对口型 数字人 单人音频驱动_2039686638024003585.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 21 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 20/21 个有
- `Int` —— 20/21 个有
- `RH_GetAudioDuration` —— 20/21 个有
- `ToInt` —— 20/21 个有
- `WanVideoTorchCompileSettings` —— 20/21 个有
- `AudioCrop` —— 18/21 个有
- `Audio Duration (mtb)` —— 1/21 个有
- `AudioCombine` —— 1/21 个有
- `CR SDXL Aspect Ratio` —— 1/21 个有
- `DF_Image_scale_to_side` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `JWInteger` —— 1/21 个有
- `JjkText` —— 1/21 个有
- `PreviewAudio` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `SaveAudio` —— 1/21 个有
- `SoundFlow_TrimAudio` —— 1/21 个有
- `Text` —— 1/21 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/21 个有
- `easy indexTTSAudioMerge` —— 1/21 个有
- `easy indexTTSEmotionVector` —— 1/21 个有
- `easy indexTTSGenerateSimple` —— 1/21 个有
- `kkGetImage` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
