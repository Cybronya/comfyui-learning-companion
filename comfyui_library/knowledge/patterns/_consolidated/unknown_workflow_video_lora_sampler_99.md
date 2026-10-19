---
name: unknown_workflow_video_lora_sampler_99
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.906933
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, Float, GetImageSizeAndCount, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1971183114510864385.json, 视频生成/图生视频/1974013871881105409.json, 视频生成/图生视频/2021029797077454850.json, 视频生成/图生视频/1968517306395570177.json, 视频生成/图生视频/1976203994194427906.json, 视频生成/图生视频/2073212221412438017.json, 视频生成/图生视频/2066681308595712001.json, 视频生成/图生视频/2055171452390912002.json, 视频生成/图生视频/1982245487325659137.json, 视频生成/图生视频/2026898938053271554.json, 视频生成/图生视频/1976156125466902529.json, 视频生成/图生视频/1980903199232184321.json, 视频生成/图生视频/1978368090293555201.json, 视频生成/图生视频/1980273017576185857.json, 视频生成/文生视频/1968636624055750658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_99

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1971183114510864385.json、视频生成/图生视频/1974013871881105409.json、视频生成/图生视频/2021029797077454850.json、视频生成/图生视频/1968517306395570177.json、视频生成/图生视频/1976203994194427906.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `Float`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `HunyuanVideoFoley` —— 13/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/15 个有
- `WanVideoImageToVideoEncode` —— 13/15 个有
- `LoadImage` —— 12/15 个有
- `SaveLatent` —— 12/15 个有
- `VAEEncode` —— 12/15 个有
- `VAELoader` —— 12/15 个有
- `easy showAnything` —— 9/15 个有
- `text_mul_replace` —— 9/15 个有
- `LayerUtility: PurgeVRAM V2` —— 5/15 个有
- `ImageFromBatch+` —— 4/15 个有
- `StringToFloatList` —— 4/15 个有
- `easy batchAnything` —— 4/15 个有
- `WanVideoEmptyEmbeds` —— 3/15 个有
- `AILab_MiniCPM_4_V` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `GetVideoComponents` —— 1/15 个有
- `LayerUtility: PurgeVRAM` —— 1/15 个有
- `LoadVideo` —— 1/15 个有
- `MathExpression|pysssss` —— 1/15 个有
- `ReplaceText` —— 1/15 个有
- `ShowText` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
