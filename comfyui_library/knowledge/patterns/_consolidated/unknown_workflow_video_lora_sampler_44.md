---
name: unknown_workflow_video_lora_sampler_44
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.897435
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(Insight版)Wan2.2 Lightx2v权重差异调度图生视频加速版V1_1972516468346777602.json, 视频生成/图生视频/(Insight版)Wan2.2 图生视频加速版V1_1972495972968361985.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS高噪MPS低噪加速版V1_1964944086870446082.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS低噪加速版V1_1964938910965055490.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964939637061992450.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度加速版V1_1964922517129449473.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度双HPS加速版V1_1964962466272825346.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度双MPS加速版V1_1964938181672095745.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频breast弹弹V2_1966515358914031618.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_2004808833312714753.json, 视频生成/图生视频/(KJ版)Wan2.2+Pusa图生视频加速版V1_1963292040106840066.json, 视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速_1976470630323326977.json, 视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速版V5（加速及质量提高）_1950024658970173442.json, 视频生成/图生视频/(Palingenesis版)Wan2.2 图生视频加速版V1_1972111264942059521.json, 视频生成/图生视频/(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1972564669351260162.json, 视频生成/图生视频/001-(KJ版)Wan2.2高质量图生视频-优调版_1958374851545350145.json, 视频生成/图生视频/Lightx2v 1030 差异模型高低噪图生视频V1(手动提示词)_1984649451941806082.json, 视频生成/图生视频/Wan 图生视频breast弹弹_1968517306395570177.json, 视频生成/图生视频/Wan2.2 kijai 4步lora 快速图生视频极速版_1978124333073719297.json, 视频生成/图生视频/Wan2.2图生视频-老照片动起来V2_1988928364830404610.json, 视频生成/图生视频/wan2.2老照片动起来复活版-图生美女视频_1989169406058049538.json, 视频生成/图生视频/【导演版】AI 短剧视频生成器——图到视频一键生成_1984149436848865282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_44

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/(Insight版)Wan2.2 Lightx2v权重差异调度图生视频加速版V1_1972516468346777602.json、视频生成/图生视频/(Insight版)Wan2.2 图生视频加速版V1_1972495972968361985.json、视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json、视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS高噪MPS低噪加速版V1_1964944086870446082.json、视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS低噪加速版V1_1964938910965055490.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 23 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `WanVideoBlockSwap` —— 22/23 个有
- `WanVideoSetBlockSwap` —— 21/23 个有
- `WanVideoSetLoRAs` —— 21/23 个有
- `WanVideoTorchCompileSettings` —— 21/23 个有
- `Float` —— 20/23 个有
- `WanVideoScheduler` —— 20/23 个有
- `WanVideoSigmaToStep` —— 20/23 个有
- `LayerUtility: PurgeVRAM V2` —— 4/23 个有
- `MathExpression|pysssss` —— 4/23 个有
- `LayerUtility: PurgeVRAM` —— 3/23 个有
- `StringToFloatList` —— 3/23 个有
- `FloatToSigmas` —— 2/23 个有
- `ImageFromBatch+` —— 2/23 个有
- `CR Seed` —— 1/23 个有
- `ConditioningSetArea` —— 1/23 个有
- `GetNode` —— 1/23 个有
- `ImageScaleBy` —— 1/23 个有
- `Int` —— 1/23 个有
- `Label (rgthree)` —— 1/23 个有
- `MuyeTextEditOutput` —— 1/23 个有
- `RHHiddenNodes` —— 1/23 个有
- `RIFE VFI` —— 1/23 个有
- `SetNode` —— 1/23 个有
- `easy int` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
