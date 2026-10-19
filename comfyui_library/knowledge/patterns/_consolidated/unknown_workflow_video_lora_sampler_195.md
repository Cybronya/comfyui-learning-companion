---
name: unknown_workflow_video_lora_sampler_195
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8975
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1991013397888180225.json, 视频生成/图生视频/2036380526440878082.json, 视频生成/图生视频/1984149436848865282.json, 视频生成/图生视频/1973249582245220353.json, 视频生成/图生视频/1986727820116307970.json, 视频生成/图生视频/1978653622206664706.json, 视频生成/图生视频/1972165369475559425.json, 视频生成/图生视频/1983833483145584642.json, 视频生成/图生视频/1972615288426520578.json, 视频生成/图生视频/1984923228604940289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_195

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1991013397888180225.json、视频生成/图生视频/2036380526440878082.json、视频生成/图生视频/1984149436848865282.json、视频生成/图生视频/1973249582245220353.json、视频生成/图生视频/1986727820116307970.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 9/10 个有
- `GetImageSizeAndCount` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `WanVideoScheduler` —— 9/10 个有
- `WanVideoSigmaToStep` —— 9/10 个有
- `CR Prompt Text` —— 8/10 个有
- `INTConstant` —— 8/10 个有
- `JWInteger` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `MathExpression|pysssss` —— 6/10 个有
- `Int` —— 5/10 个有
- `WanVideoSetBlockSwap` —— 4/10 个有
- `WanVideoSetLoRAs` —— 4/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `ConditioningSetArea` —— 1/10 个有
- `GridAnnotation` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `LoadImagesFromURL` —— 1/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `math_calculate` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
