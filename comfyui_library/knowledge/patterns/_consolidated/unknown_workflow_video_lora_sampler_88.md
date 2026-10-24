---
name: unknown_workflow_video_lora_sampler_88
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.959562
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json, 视频生成/图生视频/AIwood-wan2.2 Multitalk 图生视频版_1952034725047250945.json, 视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054032452045295618.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054464076696301569.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054724195342405634.json, 视频生成/图生视频/wan2.2 Multitalk 图生视频版《落花》_2054371842873405441.json, 视频生成/图生视频/wan2.2+Multitalk 图生视频_1952158327776202754.json, 视频生成/图生视频/wan2.2+Multitalk+图生视频版_2059875517922369538.json, 视频生成/图生视频/wan2.2-Multitalk图生视频_1952274805175341058.json, 视频生成/图生视频/【图生视频】wan2.2 Multitalk_1952625032197541890.json, 视频生成/图生视频/【视频】Wan2.2首尾帧一键生成视频_1952674570933309442.json, 视频生成/图生视频/图生视频 -AIwood-wan2.2 Multitalk_2034089808573767681.json, 视频生成/图生视频/图生视频版_1952636876098342913.json, 视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json, 视频生成/文生视频/Wan2.2+Multitalk 文生视频_1952158294372765697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_88

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json、视频生成/图生视频/AIwood-wan2.2 Multitalk 图生视频版_1952034725047250945.json、视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json、视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054032452045295618.json、视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054464076696301569.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 16 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadWav2VecModel` —— 15/16 个有
- `INTConstant` —— 15/16 个有
- `LoadAudio` —— 15/16 个有
- `MultiTalkModelLoader` —— 15/16 个有
- `MultiTalkWav2VecEmbeds` —— 15/16 个有
- `WanVideoTorchCompileSettings` —— 15/16 个有
- `Float to Int` —— 14/16 个有
- `Int` —— 14/16 个有
- `LoadImage` —— 14/16 个有
- `RH_GetAudioDuration` —— 14/16 个有
- `SimpleMath+` —— 14/16 个有
- `WanVideoImageToVideoEncode` —— 14/16 个有
- `ImageResizeKJv2` —— 13/16 个有
- `easy showAnything` —— 3/16 个有
- `CR Text Replace` —— 2/16 个有
- `PrimitiveBoolean` —— 2/16 个有
- `RH_Captioner` —— 2/16 个有
- `TextBox` —— 2/16 个有
- `WanVideoEmptyEmbeds` —— 2/16 个有
- `easy ifElse` —— 2/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `LayerUtility: PurgeVRAM V2` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
