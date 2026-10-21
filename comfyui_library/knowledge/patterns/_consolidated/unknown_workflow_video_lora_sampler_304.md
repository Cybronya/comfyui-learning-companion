---
name: unknown_workflow_video_lora_sampler_304
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.904571
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1963516764331266050.json, 视频生成/图生视频/2015692807259824129.json, 视频生成/图生视频/1980248252606013441.json, 视频生成/图生视频/1957840696807096321.json, 视频生成/图生视频/1957992360850468865.json, 视频生成/图生视频/1983589305073508353.json, 视频生成/图生视频/2028126776630710273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_304

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1963516764331266050.json、视频生成/图生视频/2015692807259824129.json、视频生成/图生视频/1980248252606013441.json、视频生成/图生视频/1957840696807096321.json、视频生成/图生视频/1957992360850468865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `ImageFromBatch+` —— 5/7 个有
- `JWIntegerToString` —— 2/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `MegaTTS3Run` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `RH_Suno_Single` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `SaveAudioMP3` —— 1/7 个有
- `String` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy anythingIndexSwitch` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
