---
name: unknown_workflow_video_lora_sampler_204
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.929
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1952544816922071041.json, 视频生成/图生视频/1958374851545350145.json, 视频生成/图生视频/2021029797077454850.json, 视频生成/图生视频/1984649451941806082.json, 视频生成/图生视频/1968517306395570177.json, 视频生成/图生视频/1978124333073719297.json, 视频生成/图生视频/1988928364830404610.json, 视频生成/图生视频/1989169406058049538.json, 视频生成/文生视频/1969281370944139266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_204

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1952544816922071041.json、视频生成/图生视频/1958374851545350145.json、视频生成/图生视频/2021029797077454850.json、视频生成/图生视频/1984649451941806082.json、视频生成/图生视频/1968517306395570177.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 8/9 个有
- `JWInteger` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `WanVideoBlockSwap` —— 8/9 个有
- `WanVideoImageToVideoEncode` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `Float` —— 6/9 个有
- `WanVideoScheduler` —— 6/9 个有
- `WanVideoSigmaToStep` —— 6/9 个有
- `LayerUtility: PurgeVRAM V2` —— 4/9 个有
- `MathExpression|pysssss` —— 4/9 个有
- `StringToFloatList` —— 3/9 个有
- `FloatToSigmas` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `RHHiddenNodes` —— 2/9 个有
- `easy int` —— 2/9 个有
- `ImageScaleBy` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `WanVideoEmptyEmbeds` —— 1/9 个有
- `WanVideoTeaCache` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
