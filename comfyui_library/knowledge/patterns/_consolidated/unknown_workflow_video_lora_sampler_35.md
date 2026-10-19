---
name: unknown_workflow_video_lora_sampler_35
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.889542
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1972516468346777602.json, 视频生成/图生视频/1972495972968361985.json, 视频生成/图生视频/1964938797580472321.json, 视频生成/图生视频/1964944086870446082.json, 视频生成/图生视频/1964938910965055490.json, 视频生成/图生视频/1964939637061992450.json, 视频生成/图生视频/1964922517129449473.json, 视频生成/图生视频/1964962466272825346.json, 视频生成/图生视频/1964938181672095745.json, 视频生成/图生视频/1966515358914031618.json, 视频生成/图生视频/2004808833312714753.json, 视频生成/图生视频/1963292040106840066.json, 视频生成/图生视频/1976470630323326977.json, 视频生成/图生视频/1950024658970173442.json, 视频生成/图生视频/1972111264942059521.json, 视频生成/图生视频/1972564669351260162.json, 视频生成/图生视频/1958374851545350145.json, 视频生成/图生视频/1952379981454356482.json, 视频生成/图生视频/1958329812857327618.json, 视频生成/图生视频/1950822532939186177.json, 视频生成/图生视频/1978124333073719297.json, 视频生成/图生视频/1988928364830404610.json, 视频生成/图生视频/1989169406058049538.json, 视频生成/文生视频/1969281370944139266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/1972516468346777602.json、视频生成/图生视频/1972495972968361985.json、视频生成/图生视频/1964938797580472321.json、视频生成/图生视频/1964944086870446082.json、视频生成/图生视频/1964938910965055490.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 23/24 个有
- `JWInteger` —— 23/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 23/24 个有
- `LoadImage` —— 23/24 个有
- `WanVideoBlockSwap` —— 23/24 个有
- `WanVideoImageToVideoEncode` —— 23/24 个有
- `WanVideoTorchCompileSettings` —— 23/24 个有
- `WanVideoSetBlockSwap` —— 22/24 个有
- `WanVideoSetLoRAs` —— 22/24 个有
- `Float` —— 18/24 个有
- `WanVideoScheduler` —— 18/24 个有
- `WanVideoSigmaToStep` —— 18/24 个有
- `ImageFromBatch+` —— 6/24 个有
- `LayerUtility: PurgeVRAM` —— 5/24 个有
- `StringToFloatList` —— 4/24 个有
- `LayerUtility: PurgeVRAM V2` —— 3/24 个有
- `MathExpression|pysssss` —— 3/24 个有
- `FloatToSigmas` —— 2/24 个有
- `RHHiddenNodes` —— 2/24 个有
- `CR Seed` —— 1/24 个有
- `GetNode` —— 1/24 个有
- `ImageScaleBy` —— 1/24 个有
- `Label (rgthree)` —— 1/24 个有
- `RIFE VFI` —— 1/24 个有
- `SetNode` —— 1/24 个有
- `WanVideoEmptyEmbeds` —— 1/24 个有
- `easy int` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
