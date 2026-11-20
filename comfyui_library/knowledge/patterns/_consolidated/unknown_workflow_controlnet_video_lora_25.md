---
name: unknown_workflow_controlnet_video_lora_25
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.957833
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2_multitalk数字人（动作幅度较大）_1953061353666899969.json, 视频生成/图生视频/wanvideo_multitalk_test_01_1936354882708475905.json, 视频生成/图生视频/wanvideo_multitalk_test_01g_1936629963053256706.json, 视频生成/图生视频/图片+音频驱动数字人（PT单图运镜控制数字人自由运镜）_1942053669372379138.json, 视频生成/图生视频/开源顶流MultiTalk Kijai版单人工作流_1936154909266055170.json, 视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/WAN2.2_multitalk数字人（动作幅度较大）_1953061353666899969.json、视频生成/图生视频/wanvideo_multitalk_test_01_1936354882708475905.json、视频生成/图生视频/wanvideo_multitalk_test_01g_1936629963053256706.json、视频生成/图生视频/图片+音频驱动数字人（PT单图运镜控制数字人自由运镜）_1942053669372379138.json、视频生成/图生视频/开源顶流MultiTalk Kijai版单人工作流_1936154909266055170.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

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
- `CreateCFGScheduleFloatList` —— 5/6 个有
- `VHS_DuplicateImages` —— 4/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `Int` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PT_KeyframeCamera` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `RepeatImageBatch` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `WanVideoSetBlockSwap` —— 1/6 个有
- `WanVideoSetLoRAs` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
