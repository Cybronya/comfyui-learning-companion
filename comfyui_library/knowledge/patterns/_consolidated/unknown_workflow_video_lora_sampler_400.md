---
name: unknown_workflow_video_lora_sampler_400
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6726
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json, 视频生成/图生视频/1972120402749222914.json, 视频生成/图生视频/1958218756659036162.json, 视频生成/图生视频/1971064636227391489.json, 视频生成/图生视频/2004504763003793409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_400

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/音频趋动 infinite talk wan2.1_2015430092859645953.json、视频生成/图生视频/1972120402749222914.json、视频生成/图生视频/1958218756659036162.json、视频生成/图生视频/1971064636227391489.json、视频生成/图生视频/2004504763003793409.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 4/5 个有
- `GetImageRangeFromBatch` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `VHS_LoadVideo` —— 4/5 个有
- `WanVideoEncode` —— 4/5 个有
- `JWIntegerToString` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `easy int` —— 2/5 个有
- `Audio Duration (mtb)` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `ColorMatch` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
