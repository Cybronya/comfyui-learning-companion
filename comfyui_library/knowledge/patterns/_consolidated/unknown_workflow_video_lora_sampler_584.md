---
name: unknown_workflow_video_lora_sampler_584
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9475
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, Int, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/infinitetalk_Wan2.1-单人数字人_1958727770622816258.json, 视频生成/图生视频/infinitetalk单人图片数字人_1960362345920983042.json, 视频生成/图生视频/wan2.1_infinitetalk_双人数字人口播长视频版_1973775994349858817.json, 视频生成/图生视频/wan2.2-Multitalk-万能数字人_1952720631349579777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_584

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/infinitetalk_Wan2.1-单人数字人_1958727770622816258.json、视频生成/图生视频/infinitetalk单人图片数字人_1960362345920983042.json、视频生成/图生视频/wan2.1_infinitetalk_双人数字人口播长视频版_1973775994349858817.json、视频生成/图生视频/wan2.2-Multitalk-万能数字人_1952720631349579777.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Int`
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
- `CR Text` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `WanVideoImageToVideoMultiTalk` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `Audio Duration (mtb)` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `ImageSmartSharpen+` —— 1/4 个有
- `InversionDemoLazyIndexSwitch` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `WanVideoImageToVideoEncode` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
