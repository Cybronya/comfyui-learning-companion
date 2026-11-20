---
name: unknown_workflow_video_lora_sampler_502
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.637
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/KJ_Wan_Video_21_InfiniteTalk_1965986400816590849.json, 数字人/数字人/慕斯AI_InfiniteTalk_数字人口播_图生视频_2112165352271597570.json, 视频生成/图生视频/IndexTTS 1.5 +InfiniteTalk数字人_1983435435332575234.json, 视频生成/图生视频/数字人 InfiniTetalk 音频+图片GGUF_2012499953494528001.json, 视频生成/图生视频/无限时长多人数字人-InfiniteTalkd多人图生视频_1958125817404542978.json, 视频生成/图生视频/无限时长音乐数字人-InfiniteTalk单人图生视频_1958125770365423618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_502

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/KJ_Wan_Video_21_InfiniteTalk_1965986400816590849.json、数字人/数字人/慕斯AI_InfiniteTalk_数字人口播_图生视频_2112165352271597570.json、视频生成/图生视频/IndexTTS 1.5 +InfiniteTalk数字人_1983435435332575234.json、视频生成/图生视频/数字人 InfiniTetalk 音频+图片GGUF_2012499953494528001.json、视频生成/图生视频/无限时长多人数字人-InfiniteTalkd多人图生视频_1958125817404542978.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `WanVideoDecode` —— 5/6 个有
- `INTConstant` —— 3/6 个有
- `AudioCrop` —— 2/6 个有
- `IndexTTSNode` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `CeilNode` —— 1/6 个有
- `Int` —— 1/6 个有
- `JWIntegerToString` —— 1/6 个有
- `LoadAudioFromUrl` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `WanVideoPassImagesFromSamples` —— 1/6 个有
- `easy mathInt` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
