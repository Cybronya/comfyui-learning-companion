---
name: unknown_workflow_video_lora_sampler_318
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88425
common_nodes: [CR Prompt Text, Float, GetImageSizeAndCount, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, SaveLatent, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 control控制_1966742439342059521.json, 视频生成/图生视频/【高质量+加速】(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_1982245487325659137.json, 视频生成/图生视频/（4+4-光鸟）KJ版Wan2.2优调版图生视频V1_1976156125466902529.json, 视频生成/图生视频/（4+4）KJ版Wan2.2 LightX2V1022高噪模型优调版图生视频V1_1980903199232184321.json, 视频生成/图生视频/（4+4）KJ版Wan2.2 LightX2V新版高噪模型优调版图生视频V2_1978368090293555201.json, 视频生成/图生视频/（4+4）KJ版Wan2.2优调版图生视频实验版V2（LightX2v+Rcm）_1980273017576185857.json, 视频生成/文生视频/(KJ版)Wan2.2+Foley精调版文生视频V1_1970702549865164802.json, 视频生成/文生视频/Comfy挑战赛6（心跳）Wan2.2文生视频+音频_1971180956935720962.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_318

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2 control控制_1966742439342059521.json、视频生成/图生视频/【高质量+加速】(KJ版)Wan2.2 图生视频（加速+质量提高）精准调度版_1982245487325659137.json、视频生成/图生视频/（4+4-光鸟）KJ版Wan2.2优调版图生视频V1_1976156125466902529.json、视频生成/图生视频/（4+4）KJ版Wan2.2 LightX2V1022高噪模型优调版图生视频V1_1980903199232184321.json、视频生成/图生视频/（4+4）KJ版Wan2.2 LightX2V新版高噪模型优调版图生视频V2_1978368090293555201.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CR Prompt Text`
- `Float`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `SaveLatent`
- `VAEEncode`
- `VAELoader`
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
- `CreateCFGScheduleFloatList` —— 7/8 个有
- `HunyuanVideoFoley` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `text_mul_replace` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `WanVideoImageToVideoEncode` —— 6/8 个有
- `WanVideoEmptyEmbeds` —— 2/8 个有
- `PreviewImage` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `StringToFloatList` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `WanVideoContextOptions` —— 1/8 个有
- `WanVideoControlEmbeds` —— 1/8 个有
- `WanVideoEncode` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
