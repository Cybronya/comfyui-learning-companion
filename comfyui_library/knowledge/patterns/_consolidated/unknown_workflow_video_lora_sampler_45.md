---
name: unknown_workflow_video_lora_sampler_45
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.957286
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1988149592183234562.json, 视频生成/图生视频/1990298374261927937.json, 视频生成/图生视频/2042473229025021954.json, 视频生成/图生视频/2038129720084140034.json, 视频生成/图生视频/2039686638024003585.json, 视频生成/图生视频/2038259769424744450.json, 视频生成/图生视频/2043221914818191361.json, 视频生成/图生视频/infinitetalk-workflow_2101559918137536513.json, 视频生成/图生视频/1958721721454981121.json, 视频生成/图生视频/1993155666919571457.json, 视频生成/图生视频/infinitetalk单人_1957826962256658434.json, 视频生成/图生视频/2044669894783934465.json, 视频生成/图生视频/1983851965690056706.json, 视频生成/图生视频/1987800864440168449.json, 视频生成/图生视频/infinitetalk单人数字人 横版_2082717087134470145.json, 视频生成/图生视频/1961786018880012290.json, 视频生成/图生视频/2080575708149145601.json, 视频生成/图生视频/1968146725170982914.json, 视频生成/图生视频/1999412008917364738.json, 视频生成/图生视频/2054517632375771138.json, 视频生成/图生视频/2044453798432739329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/1988149592183234562.json、视频生成/图生视频/1990298374261927937.json、视频生成/图生视频/2042473229025021954.json、视频生成/图生视频/2038129720084140034.json、视频生成/图生视频/2039686638024003585.json…）

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

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 20/21 个有
- `RH_GetAudioDuration` —— 20/21 个有
- `WanVideoTorchCompileSettings` —— 20/21 个有
- `easy showAnything` —— 20/21 个有
- `Int` —— 19/21 个有
- `ToInt` —— 19/21 个有
- `AudioCrop` —— 17/21 个有
- `PreviewImage` —— 2/21 个有
- `SoundFlow_TrimAudio` —— 2/21 个有
- `Audio Duration (mtb)` —— 1/21 个有
- `AudioCombine` —— 1/21 个有
- `CR SDXL Aspect Ratio` —— 1/21 个有
- `DF_Image_scale_to_side` —— 1/21 个有
- `Display Int (rgthree)` —— 1/21 个有
- `ImageBatchMulti` —— 1/21 个有
- `ImageFromBatch` —— 1/21 个有
- `JWInteger` —— 1/21 个有
- `JjkText` —— 1/21 个有
- `PreviewAudio` —— 1/21 个有
- `Text` —— 1/21 个有
- `kkGetImage` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
