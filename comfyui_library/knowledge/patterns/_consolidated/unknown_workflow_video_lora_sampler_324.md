---
name: unknown_workflow_video_lora_sampler_324
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.902
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生(URL)视频-高动态卡通动漫_1986727820116307970.json, 视频生成/图生视频/图生视频KJ版Wan2.2新版高噪模型V210s以上_1978653622206664706.json, 视频生成/图生视频/图生视频加速版Wan2.2 (Palingenesis版)_1972165369475559425.json, 视频生成/图生视频/图生视频加速版Wan2.2_1983833483145584642.json, 视频生成/图生视频/图生视频加速版Wan2.2高动态卡通动漫_1972615288426520578.json, 视频生成/图生视频/图生视频加速版高质量Lightx2v+1030+差异模型高低噪图生视频V1(手动提示词)_1984923228604940289.json, 视频生成/图生视频/（自用）KJ版Wan2.2图生视频超级加速版V3（大幅度提高速度）_1952588298072068097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_324

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/图生(URL)视频-高动态卡通动漫_1986727820116307970.json、视频生成/图生视频/图生视频KJ版Wan2.2新版高噪模型V210s以上_1978653622206664706.json、视频生成/图生视频/图生视频加速版Wan2.2 (Palingenesis版)_1972165369475559425.json、视频生成/图生视频/图生视频加速版Wan2.2_1983833483145584642.json、视频生成/图生视频/图生视频加速版Wan2.2高动态卡通动漫_1972615288426520578.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWInteger`
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
- `Float` —— 6/7 个有
- `GetImageSizeAndCount` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `WanVideoScheduler` —— 6/7 个有
- `WanVideoSigmaToStep` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `MathExpression|pysssss` —— 5/7 个有
- `WanVideoSetBlockSwap` —— 4/7 个有
- `WanVideoSetLoRAs` —— 4/7 个有
- `Int` —— 3/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `GridAnnotation` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoadImagesFromURL` —— 1/7 个有
- `LoadLatent` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SaveLatent` —— 1/7 个有
- `math_calculate` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
