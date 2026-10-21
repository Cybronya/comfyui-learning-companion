---
name: unknown_workflow_video_lora_sampler_296
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.823857
common_nodes: [CR Text, CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImpactInt, LoadWanVideoT5TextEncoder, Seed (rgthree), SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [CR Text, Note Plus (mtb), SimpleMath+, Seed (rgthree), LayerUtility: ImageScaleByAspectRatio V2]
members: [视频生成/图生视频/1972199974152957954.json, 视频生成/图生视频/1972673116709298177.json, 视频生成/图生视频/1972843772218396673.json, 视频生成/文生视频/1972186550123556865.json, 视频生成/文生视频/1972199974152957954.json, 视频生成/文生视频/1972673116709298177.json, 视频生成/文生视频/1972686604550774785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_296

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1972199974152957954.json、视频生成/图生视频/1972673116709298177.json、视频生成/图生视频/1972843772218396673.json、视频生成/文生视频/1972186550123556865.json、视频生成/文生视频/1972199974152957954.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImpactInt`
- `LoadWanVideoT5TextEncoder`
- `Seed (rgthree)`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `UpscaleModelLoader` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `WanVideoImageToVideoEncode` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `Note Plus (mtb)` —— 4/7 个有
- `INTConstant` —— 3/7 个有
- `ImageScaleToMegapixels` —— 3/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `Anything Everywhere` —— 2/7 个有
- `WanVideoEmptyEmbeds` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Note Plus (mtb)、SimpleMath+、Seed (rgthree)、LayerUtility: ImageScaleByAspectRatio V2
