---
name: unknown_workflow_video_lora_sampler_553
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94825
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, INTConstant, Int, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, RHHiddenNodes, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/KJ+radial+Fastwan+lightx高低+自动扩词极速万相wan2.2_1950062965963841538.json, 视频生成/图生视频/万相2.2+KJ+multitalk+radial+Fastwan+lightx644)图生视数字人_1952381797537648642.json, 视频生成/图生视频/万相2.2+KJ+multitalk+克隆音色图生视数字人_1952389394525294594.json, 视频生成/图生视频/最强万相wan2.2首尾帧KJ+CineSca+MTV-Crafter+自动扩词_1950597048527704066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_553

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/KJ+radial+Fastwan+lightx高低+自动扩词极速万相wan2.2_1950062965963841538.json、视频生成/图生视频/万相2.2+KJ+multitalk+radial+Fastwan+lightx644)图生视数字人_1952381797537648642.json、视频生成/图生视频/万相2.2+KJ+multitalk+克隆音色图生视数字人_1952389394525294594.json、视频生成/图生视频/最强万相wan2.2首尾帧KJ+CineSca+MTV-Crafter+自动扩词_1950597048527704066.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `INTConstant`
- `Int`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `PIP_StringConcatenation` —— 3/4 个有
- `Wan22PromptSelector` —— 3/4 个有
- `WanVideoSetRadialAttention` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `DownloadAndLoadWav2VecModel` —— 2/4 个有
- `Float to Int` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `MultiTalkModelLoader` —— 2/4 个有
- `MultiTalkWav2VecEmbeds` —— 2/4 个有
- `RH_GetAudioDuration` —— 2/4 个有
- `AudioSeparation` —— 1/4 个有
- `IndexTTSRun` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
