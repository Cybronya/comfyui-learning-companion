---
name: unknown_workflow_video_lora_sampler_128
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.961357
common_nodes: [CreateCFGScheduleFloatList, DownloadAndLoadWav2VecModel, INTConstant, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wan2.2 文生视频+数字人_1956285868619255809.json, 视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json, 视频生成/图生视频/AIwood-wan2.2 Multitalk 图生视频版_1952034725047250945.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054032452045295618.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054464076696301569.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054724195342405634.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版《落花》_2054371842873405441.json, 视频生成/图生视频/wan2.2 图生视频+数字人_1956285883156758529.json, 视频生成/图生视频/wan2.2+Multitalk 图生视频_1952158327776202754.json, 视频生成/图生视频/wan2.2+Multitalk+图生视频版_2059875517922369538.json, 视频生成/图生视频/wan2.2-Multitalk图生视频_1952274805175341058.json, 视频生成/图生视频/【图生视频】wan2.2 Multitalk_1952625032197541890.json, 视频生成/图生视频/图生视频 -AIwood-wan2.2 Multitalk_2034089808573767681.json, 视频生成/图生视频/图生视频版_1952636876098342913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_128

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/wan2.2 文生视频+数字人_1956285868619255809.json、视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json、视频生成/图生视频/AIwood-wan2.2 Multitalk 图生视频版_1952034725047250945.json、视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054032452045295618.json、视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054464076696301569.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadWav2VecModel`
- `INTConstant`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 13/14 个有
- `Float to Int` —— 12/14 个有
- `ImageResizeKJv2` —— 12/14 个有
- `Int` —— 12/14 个有
- `LoadImage` —— 12/14 个有
- `RH_GetAudioDuration` —— 12/14 个有
- `SimpleMath+` —— 12/14 个有
- `WanVideoImageToVideoEncode` —— 12/14 个有
- `Audio Duration (mtb)` —— 2/14 个有
- `AudioSeparation` —— 2/14 个有
- `FloatConstant` —— 2/14 个有
- `MathExpression|pysssss` —— 2/14 个有
- `WanVideoEmptyEmbeds` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `CLIPVisionLoader` —— 1/14 个有
- `CR Text Replace` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `PrimitiveBoolean` —— 1/14 个有
- `RH_Captioner` —— 1/14 个有
- `TextBox` —— 1/14 个有
- `WanVideoClipVisionEncode` —— 1/14 个有
- `easy ifElse` —— 1/14 个有
- `easy int` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
