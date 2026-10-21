---
name: unknown_workflow_video_lora_sampler_74
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.831389
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1991013397888180225.json, 视频生成/图生视频/2036380526440878082.json, 视频生成/图生视频/1984149436848865282.json, 视频生成/图生视频/1973249582245220353.json, 视频生成/图生视频/1986727820116307970.json, 视频生成/图生视频/1978653622206664706.json, 视频生成/图生视频/1972165369475559425.json, 视频生成/图生视频/1983833483145584642.json, 视频生成/图生视频/1972615288426520578.json, 视频生成/文生视频/1964924575370854402.json, 视频生成/文生视频/1964929046893182977.json, 视频生成/文生视频/1964934510620102657.json, 视频生成/文生视频/1964929542555095041.json, 视频生成/文生视频/1964927799280680961.json, 视频生成/文生视频/1964919503211610114.json, 视频生成/文生视频/1964931561881747457.json, 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2055563749574103041.json, 视频生成/文生视频/Wan2.2加速版文生视频 万相4步加速视频 图像与视频生成+全节点注释_2056813400818274305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_74

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1991013397888180225.json、视频生成/图生视频/2036380526440878082.json、视频生成/图生视频/1984149436848865282.json、视频生成/图生视频/1973249582245220353.json、视频生成/图生视频/1986727820116307970.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 18 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 17/18 个有
- `WanVideoScheduler` —— 17/18 个有
- `WanVideoSigmaToStep` —— 17/18 个有
- `WanVideoTorchCompileSettings` —— 17/18 个有
- `JWInteger` —— 16/18 个有
- `GetImageSizeAndCount` —— 15/18 个有
- `CR Prompt Text` —— 14/18 个有
- `INTConstant` —— 14/18 个有
- `WanVideoSetBlockSwap` —— 12/18 个有
- `WanVideoSetLoRAs` —— 12/18 个有
- `LoadImage` —— 10/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/18 个有
- `WanVideoEmptyEmbeds` —— 9/18 个有
- `WanVideoImageToVideoEncode` —— 9/18 个有
- `MathExpression|pysssss` —— 8/18 个有
- `Int` —— 7/18 个有
- `ImpactInt` —— 2/18 个有
- `LayerUtility: PurgeVRAM V2` —— 2/18 个有
- `easy seed` —— 2/18 个有
- `ConditioningSetArea` —— 1/18 个有
- `GridAnnotation` —— 1/18 个有
- `ImageResize+` —— 1/18 个有
- `LoadImagesFromURL` —— 1/18 个有
- `MuyeTextEditOutput` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
