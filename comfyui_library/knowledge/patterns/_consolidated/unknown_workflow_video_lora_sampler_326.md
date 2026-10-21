---
name: unknown_workflow_video_lora_sampler_326
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.970571
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950852674944180226.json, 视频生成/图生视频/1978672767467982850.json, 视频生成/图生视频/1950178102964084737.json, 视频生成/图生视频/2038129014153420801.json, 视频生成/图生视频/2053740152681447425.json, 视频生成/图生视频/1950037890026881025.json, 视频生成/文生视频/1950063356758638593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_326

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1950852674944180226.json、视频生成/图生视频/1978672767467982850.json、视频生成/图生视频/1950178102964084737.json、视频生成/图生视频/2038129014153420801.json、视频生成/图生视频/2053740152681447425.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoadImage` —— 6/7 个有
- `WanVideoImageToVideoEncode` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `CreateCFGScheduleFloatList` —— 5/7 个有
- `GetImageSizeAndCount` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `ImageResizeKJv2` —— 5/7 个有
- `ImpactInt` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `Text` —— 2/7 个有
- `RH_Translator` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `WanVideoContextOptions` —— 1/7 个有
- `WanVideoEmptyEmbeds` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
