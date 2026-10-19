---
name: unknown_workflow_video_lora_sampler_237
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.868889
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958727770622816258.json, 视频生成/图生视频/1960362345920983042.json, 视频生成/图生视频/1965302801381380098.json, 视频生成/图生视频/2026541463353434114.json, 视频生成/图生视频/1973775994349858817.json, 视频生成/图生视频/1952720631349579777.json, 视频生成/图生视频/1978989792249679873.json, 视频生成/图生视频/1964871891532005378.json, 视频生成/图生视频/2001550158074658818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_237

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1958727770622816258.json、视频生成/图生视频/1960362345920983042.json、视频生成/图生视频/1965302801381380098.json、视频生成/图生视频/2026541463353434114.json、视频生成/图生视频/1973775994349858817.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `MathExpression|pysssss` —— 8/9 个有
- `WanVideoImageToVideoMultiTalk` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `PreviewAudio` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `AudioCrop` —— 4/9 个有
- `Int` —— 4/9 个有
- `MaskPreview+` —— 4/9 个有
- `SeparateMasks` —— 4/9 个有
- `easy int` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `JWInteger` —— 3/9 个有
- `Audio Duration (mtb)` —— 2/9 个有
- `Note Plus (mtb)` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `GetAudioDurationFromAudio` —— 1/9 个有
- `ImageSmartSharpen+` —— 1/9 个有
- `InversionDemoLazyIndexSwitch` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `WanVideoImageToVideoEncode` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
