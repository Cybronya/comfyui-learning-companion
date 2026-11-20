---
name: unknown_workflow_video_lora_sampler_265
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9547
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/infinitetalk_视频改口型工作流_1993958117922848769.json, 数字人/数字人/InfiniteTalk-多人无限时长数字人生成工作流_1957766648377831426.json, 数字人/数字人/全网首发——Aiwood-infinitetalk_视频改口型工作流_1958066987350052865.json, 视频生成/图生视频/InfiniteTalk单人数字人工作流_1957818036982050817.json, 视频生成/图生视频/MultiTalk 单人+运镜_1936573145107304450.json, 视频生成/图生视频/MultiTalk对口型（万相实现）+uni3C运镜控制_1937801479434735618.json, 视频生成/图生视频/MultiTalk对口型（万相实现）_1937838193955749889.json, 视频生成/图生视频/PT娃导单图运镜控制串联版_1941554640133767170.json, 视频生成/图生视频/PT娃导单图运镜控制流单节点版_1941548722545442818.json, 视频生成/图生视频/WAN2.1+数字人运镜控制+视频放大_1947456088879828994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_265

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/infinitetalk_视频改口型工作流_1993958117922848769.json、数字人/数字人/InfiniteTalk-多人无限时长数字人生成工作流_1957766648377831426.json、数字人/数字人/全网首发——Aiwood-infinitetalk_视频改口型工作流_1958066987350052865.json、视频生成/图生视频/InfiniteTalk单人数字人工作流_1957818036982050817.json、视频生成/图生视频/MultiTalk 单人+运镜_1936573145107304450.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 9/10 个有
- `WanVideoImageToVideoEncode` —— 8/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/10 个有
- `WanVideoUni3C_embeds` —— 7/10 个有
- `INTConstant` —— 6/10 个有
- `LoadImage` —— 6/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `WanVideoContextOptions` —— 6/10 个有
- `WanVideoEncode` —— 6/10 个有
- `WanVideoImageToVideoMultiTalk` —— 4/10 个有
- `CreateCFGScheduleFloatList` —— 3/10 个有
- `PT_KeyframeCamera` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `RepeatImageBatch` —— 3/10 个有
- `Display Any (rgthree)` —— 2/10 个有
- `Display Int (rgthree)` —— 2/10 个有
- `ImageConcatMulti` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `SoundFlow_GetLength` —— 2/10 个有
- `ToInt` —— 2/10 个有
- `easy int` —— 2/10 个有
- `GetImagesFromBatchIndexed` —— 1/10 个有
- `ImageBatch` —— 1/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `ImageUpscaleWithModel` —— 1/10 个有
- `RIFE VFI` —— 1/10 个有
- `UpscaleModelLoader` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
