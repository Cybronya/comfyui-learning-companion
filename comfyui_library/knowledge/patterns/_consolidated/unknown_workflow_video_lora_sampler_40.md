---
name: unknown_workflow_video_lora_sampler_40
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.88725
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(Insight版)Wan2.2 Lightx2v权重差异调度图生视频加速版V1_1972516468346777602.json, 视频生成/图生视频/(Insight版)Wan2.2 图生视频加速版V1_1972495972968361985.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS高噪MPS低噪加速版V1_1964944086870446082.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS低噪加速版V1_1964938910965055490.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964939637061992450.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度加速版V1_1964922517129449473.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度双HPS加速版V1_1964962466272825346.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度双MPS加速版V1_1964938181672095745.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频breast弹弹V2_1966515358914031618.json, 视频生成/图生视频/(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_2004808833312714753.json, 视频生成/图生视频/(KJ版)Wan2.2+Pusa图生视频加速版V1_1963292040106840066.json, 视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速_1976470630323326977.json, 视频生成/图生视频/(KJ版)Wan2.2图生视频精准调度加速版V5（加速及质量提高）_1950024658970173442.json, 视频生成/图生视频/(Palingenesis版)Wan2.2 图生视频加速版V1_1972111264942059521.json, 视频生成/图生视频/(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1972564669351260162.json, 视频生成/图生视频/001-(KJ版)Wan2.2高质量图生视频-优调版_1958374851545350145.json, 视频生成/图生视频/KJ流+KJ新版Lightx2v图生视频_1952379981454356482.json, 视频生成/图生视频/KJ流+图生视频 -恶灵骑士_1958329812857327618.json, 视频生成/图生视频/Lightx2v 1030 差异模型高低噪图生视频V1(手动提示词)_1984649451941806082.json, 视频生成/图生视频/Wan 图生视频breast弹弹_1968517306395570177.json, 视频生成/图生视频/Wan2.2图生视频-老照片动起来V2_1988928364830404610.json, 视频生成/图生视频/wan2.2老照片动起来复活版-图生美女视频_1989169406058049538.json, 视频生成/图生视频/【导演版】AI 短剧视频生成器——图到视频一键生成_1984149436848865282.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/(Insight版)Wan2.2 Lightx2v权重差异调度图生视频加速版V1_1972516468346777602.json、视频生成/图生视频/(Insight版)Wan2.2 图生视频加速版V1_1972495972968361985.json、视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS低噪加速版V1_1964938797580472321.json、视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度HPS高噪MPS低噪加速版V1_1964944086870446082.json、视频生成/图生视频/(KJ版)Wan2.2 图生视频SIMGA精准调度MPS低噪加速版V1_1964938910965055490.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
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
- `WanVideoBlockSwap` —— 23/24 个有
- `WanVideoSetBlockSwap` —— 22/24 个有
- `WanVideoSetLoRAs` —— 22/24 个有
- `WanVideoTorchCompileSettings` —— 22/24 个有
- `Float` —— 20/24 个有
- `WanVideoScheduler` —— 20/24 个有
- `WanVideoSigmaToStep` —— 20/24 个有
- `LayerUtility: PurgeVRAM` —— 4/24 个有
- `LayerUtility: PurgeVRAM V2` —— 4/24 个有
- `ImageFromBatch+` —— 3/24 个有
- `MathExpression|pysssss` —— 3/24 个有
- `StringToFloatList` —— 2/24 个有
- `CR Seed` —— 1/24 个有
- `ConditioningSetArea` —— 1/24 个有
- `FloatToSigmas` —— 1/24 个有
- `GetNode` —— 1/24 个有
- `ImageScaleBy` —— 1/24 个有
- `Int` —— 1/24 个有
- `MuyeTextEditOutput` —— 1/24 个有
- `RHHiddenNodes` —— 1/24 个有
- `RIFE VFI` —— 1/24 个有
- `SetNode` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
