---
name: unknown_workflow_controlnet_video_lora_14
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.920833
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: [VHS_DuplicateImages]
members: [视频生成/图生视频/1941554640133767170.json, 视频生成/图生视频/1941548722545442818.json, 视频生成/图生视频/1947456088879828994.json, 视频生成/图生视频/1953061353666899969.json, 视频生成/图生视频/1942053669372379138.json, 视频生成/文生视频/1978251602106703873.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_14

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1941554640133767170.json、视频生成/图生视频/1941548722545442818.json、视频生成/图生视频/1947456088879828994.json、视频生成/图生视频/1953061353666899969.json、视频生成/图生视频/1942053669372379138.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PT_KeyframeCamera` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RepeatImageBatch` —— 4/6 个有
- `CreateCFGScheduleFloatList` —— 2/6 个有
- `VHS_DuplicateImages` —— 2/6 个有
- `GetImagesFromBatchIndexed` —— 1/6 个有
- `ImageBatch` —— 1/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `Int` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `WanVideoSetBlockSwap` —— 1/6 个有
- `WanVideoSetLoRAs` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：VHS_DuplicateImages
