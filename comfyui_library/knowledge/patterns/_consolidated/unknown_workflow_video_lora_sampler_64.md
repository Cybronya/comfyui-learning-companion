---
name: unknown_workflow_video_lora_sampler_64
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.958778
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [Float to Int, SimpleMath+]
members: [视频生成/图生视频/1953496222059384834.json, 视频生成/图生视频/2014940591578157057.json, 视频生成/图生视频/1952022803912577026.json, 视频生成/图生视频/1952034725047250945.json, 视频生成/图生视频/1952358621646655489.json, 视频生成/图生视频/2054032452045295618.json, 视频生成/图生视频/2054464076696301569.json, 视频生成/图生视频/2054724195342405634.json, 视频生成/图生视频/2054371842873405441.json, 视频生成/图生视频/1952158327776202754.json, 视频生成/图生视频/2059875517922369538.json, 视频生成/图生视频/1952274805175341058.json, 视频生成/图生视频/1952625032197541890.json, 视频生成/图生视频/1952674570933309442.json, 视频生成/图生视频/2034089808573767681.json, 视频生成/图生视频/1952636876098342913.json, 视频生成/文生视频/1953496222059384834.json, 视频生成/文生视频/1952158294372765697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1953496222059384834.json、视频生成/图生视频/2014940591578157057.json、视频生成/图生视频/1952022803912577026.json、视频生成/图生视频/1952034725047250945.json、视频生成/图生视频/1952358621646655489.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 18 个 workflow 都包含：
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
- `INTConstant` —— 17/18 个有
- `WanVideoTorchCompileSettings` —— 17/18 个有
- `DownloadAndLoadWav2VecModel` —— 16/18 个有
- `Int` —— 16/18 个有
- `LoadAudio` —— 16/18 个有
- `LoadImage` —— 16/18 个有
- `MultiTalkModelLoader` —— 16/18 个有
- `MultiTalkWav2VecEmbeds` —— 16/18 个有
- `WanVideoImageToVideoEncode` —— 16/18 个有
- `Float to Int` —— 15/18 个有
- `ImageResizeKJv2` —— 15/18 个有
- `RH_GetAudioDuration` —— 15/18 个有
- `SimpleMath+` —— 15/18 个有
- `easy showAnything` —— 3/18 个有
- `CR Text Replace` —— 2/18 个有
- `PrimitiveBoolean` —— 2/18 个有
- `RH_Captioner` —— 2/18 个有
- `TextBox` —— 2/18 个有
- `WanVideoEmptyEmbeds` —— 2/18 个有
- `easy ifElse` —— 2/18 个有
- `Fast Groups Muter (rgthree)` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `LayerUtility: PurgeVRAM V2` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Float to Int、SimpleMath+
