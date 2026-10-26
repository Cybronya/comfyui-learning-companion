---
name: unknown_workflow_video_lora_sampler_538
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.875
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, JWFloatToInteger, JWImageExtractFromBatch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SimpleMath+, SoundFlow_GetLength, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/图片对口型_2001210433275035650.json, 视频生成/图生视频/图片对口型_1966494606252814337.json, 视频生成/图生视频/图片对口型全自动多动态无限长度-单人 (Infinite talk）_1958863725044379649.json, 视频生成/图生视频/视频_图片对口型全自动无限长度-单人 (Infinite talk）_1957922626649911298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_538

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/图片对口型_2001210433275035650.json、视频生成/图生视频/图片对口型_1966494606252814337.json、视频生成/图生视频/图片对口型全自动多动态无限长度-单人 (Infinite talk）_1958863725044379649.json、视频生成/图生视频/视频_图片对口型全自动无限长度-单人 (Infinite talk）_1957922626649911298.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `JWFloatToInteger`
- `JWImageExtractFromBatch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_IntBinaryOperation` —— 3/4 个有
- `LoadWanVideoT5TextEncoder` —— 3/4 个有
- `PreviewAudio` —— 3/4 个有
- `WanVideoTextEncode` —— 3/4 个有
- `Any Switch (rgthree)` —— 2/4 个有
- `AudioCrop` —— 2/4 个有
- `Bool` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `Int` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `PrimitiveString` —— 2/4 个有
- `SaveAudio` —— 2/4 个有
- `ToBool` —— 2/4 个有
- `VHS_LoadAudioUpload` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `easy ifElse` —— 2/4 个有
- `Note _O` —— 1/4 个有
- `WanVideoImageToVideoEncode` —— 1/4 个有
- `WanVideoTextEncodeCached` —— 1/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/4 个有
- `WanVideoUni3C_embeds` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
