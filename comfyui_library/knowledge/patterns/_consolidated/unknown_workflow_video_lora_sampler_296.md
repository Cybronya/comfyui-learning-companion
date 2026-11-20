---
name: unknown_workflow_video_lora_sampler_296
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.966625
common_nodes: [CreateCFGScheduleFloatList, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json, 视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json, 视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json, 视频生成/图生视频/MultiTalk对口型（万相实现）_1937838193955749889.json, 视频生成/图生视频/Multitalk--唱歌数字人_1936361924722593793.json, 视频生成/图生视频/WAN2.2_multitalk数字人（动作幅度较大）_1953061353666899969.json, 视频生成/图生视频/wanvideo_multitalk_test_01_1936354882708475905.json, 视频生成/文生视频/wanvideo_multitalk_test_01g_1978251602106703873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_296

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json、视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json、视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json、视频生成/图生视频/MultiTalk对口型（万相实现）_1937838193955749889.json、视频生成/图生视频/Multitalk--唱歌数字人_1936361924722593793.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 7/8 个有
- `WanVideoBlockSwap` —— 7/8 个有
- `DownloadAndLoadWav2VecModel` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `MultiTalkModelLoader` —— 6/8 个有
- `MultiTalkWav2VecEmbeds` —— 6/8 个有
- `AudioCrop` —— 5/8 个有
- `AudioSeparation` —— 5/8 个有
- `CLIPVisionLoader` —— 5/8 个有
- `ImageResizeKJv2` —— 5/8 个有
- `WanVideoClipVisionEncode` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 5/8 个有
- `WanVideoContextOptions` —— 4/8 个有
- `WanVideoSetBlockSwap` —— 4/8 个有
- `WanVideoSetLoRAs` —— 4/8 个有
- `GetImageSizeAndCount` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `VHS_DuplicateImages` —— 3/8 个有
- `WanVideoEncode` —— 3/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/8 个有
- `WanVideoUni3C_embeds` —— 3/8 个有
- `Audio Duration (mtb)` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `Int` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `JWIntegerToString` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `TextInput_` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
