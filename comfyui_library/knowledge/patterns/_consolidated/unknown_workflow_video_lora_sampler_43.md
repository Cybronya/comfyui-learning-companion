---
name: unknown_workflow_video_lora_sampler_43
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.834174
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/(6+6)Wan2.2 Smooth Mix高动态文生视频(KJ版)_1978740744045400065.json, 视频生成/文生视频/(KJ版)Wan2.2 MiniCpm 4.5视频洗稿工作流V1_1961658398267916290.json, 视频生成/文生视频/(KJ版)Wan2.2 Nova文生视频V1_1969281370944139266.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度+MPS高低噪奖励模型加速版V1_1964924575370854402.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度HPS低噪加速版V1_1964929046893182977.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度HPS高噪MPS低噪加速版V1_1964934510620102657.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度MPS低噪加速版V1_1964929542555095041.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度MPS高噪HPS低噪加速版V1_1964927799280680961.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度加速版V1_1964919503211610114.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度双HPS加速版V1_1964931561881747457.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（光源版）_1950141714336014337.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（光线类型）_1950148142277771266.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（情绪）_1950200316404916225.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（时间光）_1950154187399192578.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（构图法）_1950159020893061122.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（镜头类型）_1950180748268584962.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（镜头距离）_1950165203683033089.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频加速版V1（镜头运动）_1950205913674244097.json, 视频生成/文生视频/(KJ版)Wan2.2 文生视频精准调度加速版V4（加速及质量提高）_1950086334457274370.json, 视频生成/文生视频/(Palingenesis版)Wan2.2 文生视频高动态加速版V1_1972111273070620674.json, 视频生成/文生视频/Wan2.2 文生视频HPS高噪MPS低噪加速版V1_1969009834282655745.json, 视频生成/文生视频/Wan2.2 精准调度文生视频加速版_1966009360197521409.json, 视频生成/文生视频/（自用）Wan2.2 Palingenesis文生视频加速版V1_1972489940305113089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/文生视频/(6+6)Wan2.2 Smooth Mix高动态文生视频(KJ版)_1978740744045400065.json、视频生成/文生视频/(KJ版)Wan2.2 MiniCpm 4.5视频洗稿工作流V1_1961658398267916290.json、视频生成/文生视频/(KJ版)Wan2.2 Nova文生视频V1_1969281370944139266.json、视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度+MPS高低噪奖励模型加速版V1_1964924575370854402.json、视频生成/文生视频/(KJ版)Wan2.2 文生视频SIMGA精准调度HPS低噪加速版V1_1964929046893182977.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 23 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 22/23 个有
- `VHS_VideoCombine` —— 22/23 个有
- `WanVideoTorchCompileSettings` —— 22/23 个有
- `Float` —— 13/23 个有
- `WanVideoScheduler` —— 13/23 个有
- `WanVideoSigmaToStep` —— 13/23 个有
- `Fast Groups Bypasser (rgthree)` —— 8/23 个有
- `ImageFromBatch+` —— 2/23 个有
- `AILab_MiniCPM_4_V` —— 1/23 个有
- `LayerUtility: PurgeVRAM` —— 1/23 个有
- `LoadImage` —— 1/23 个有
- `LoadVideo` —— 1/23 个有
- `RHHiddenNodes` —— 1/23 个有
- `SaveImage` —— 1/23 个有
- `StringToFloatList` —— 1/23 个有
- `TT_img_enc` —— 1/23 个有
- `VHS_LoadVideoFFmpeg` —— 1/23 个有
- `easy showAnything` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
