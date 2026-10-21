---
name: unknown_workflow_video_lora_sampler_291
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.975
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/infinitetalk-数字人_2101888402827337730.json, 视频生成/图生视频/1957952304787898369.json, 视频生成/图生视频/1957826997610446849.json, 视频生成/图生视频/1971453748994359297.json, 视频生成/图生视频/1958085210749415426.json, 视频生成/图生视频/1940924821561884673.json, 视频生成/图生视频/1941378778566389761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_291

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/infinitetalk-数字人_2101888402827337730.json、视频生成/图生视频/1957952304787898369.json、视频生成/图生视频/1957826997610446849.json、视频生成/图生视频/1971453748994359297.json、视频生成/图生视频/1958085210749415426.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
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
- `AudioCrop` —— 6/7 个有
- `AudioSeparation` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `PreviewAudio` —— 5/7 个有
- `SeparateMasks` —— 5/7 个有
- `MathExpression|pysssss` —— 4/7 个有
- `INTConstant` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `MaskPreview` —— 2/7 个有
- `MaskPreview+` —— 2/7 个有
- `StringToInt` —— 2/7 个有
- `Bjornulf_ShowFloat` —— 1/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `CM_FloatToInt` —— 1/7 个有
- `IndexTTSRun` —— 1/7 个有
- `JWFloat` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `VHS_LoadAudioUpload` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
