---
name: unknown_workflow_video_lora_sampler_205
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7847
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/文字转音频+对口型+图生视频+标准1080P_1970453209825374209.json, 数字人/数字人/慕斯AI_InfiniteTalk_数字人口播_图生视频_2112165352271597570.json, 视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json, 视频生成/图生视频/I2V-林小茶_2047141901102489601.json, 视频生成/图生视频/V4.1（demo2）_2051961839407386625.json, 视频生成/图生视频/X_I2V（V1.1.1）_2048682075724718081.json, 视频生成/图生视频/手串替换_2054096337670557697.json, 视频生成/图生视频/手串生活方式短视频不露脸稳定版_2060540846868619266.json, 视频生成/图生视频/手串生活版_v5.2_原稿精准字幕版_2062041921597562882.json, 视频生成/图生视频/鸿茅药酒志_2054799806060605442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_205

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/文字转音频+对口型+图生视频+标准1080P_1970453209825374209.json、数字人/数字人/慕斯AI_InfiniteTalk_数字人口播_图生视频_2112165352271597570.json、视频生成/图生视频/D_I2V（V1.1.1）_2047149486551605249.json、视频生成/图生视频/I2V-林小茶_2047141901102489601.json、视频生成/图生视频/V4.1（demo2）_2051961839407386625.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MelBandRoFormerModelLoader` —— 9/10 个有
- `MelBandRoFormerSampler` —— 9/10 个有
- `WanVideoPassImagesFromSamples` —— 9/10 个有
- `FB_Qwen3TTSVoiceClone` —— 8/10 个有
- `GetImageSize` —— 8/10 个有
- `ResizeImagesByLongerEdge` —— 8/10 个有
- `Text` —— 8/10 个有
- `GetNode` —— 6/10 个有
- `PreviewAny` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `WanVideoTorchCompileSettings` —— 6/10 个有
- `Wav2VecModelLoader` —— 5/10 个有
- `PreviewAudio` —— 4/10 个有
- `CR Prompt Text` —— 1/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/10 个有
- `GIMMVFI_interpolate` —— 1/10 个有
- `HAIGC_VideoSubtitleTimestampPro` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `IndexTTS2Run` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有
- `WanVideoDecode` —— 1/10 个有
- `ZML_TextInput` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
