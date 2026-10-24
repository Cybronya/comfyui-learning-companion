---
name: unknown_workflow_video_lora_sampler_127
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.814167
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, JWStringConcat, LoadWanVideoT5TextEncoder, ShowText|pysssss, TextConcat, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650.json, 图片生成/文生图/视频-文生视频wan2.2-最强过审_1959964511526662146.json, 视频生成/图生视频/(KJ版)Wan2.2+提示词工具+GLM4.5视频扩写图生视频加速版V1_1950813995445977090.json, 视频生成/图生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1950934552208416770.json, 视频生成/图生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1950823826609348610.json, 视频生成/图生视频/(KJ版4步版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1953756753928355841.json, 视频生成/图生视频/(本地解码KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1954077934976061442.json, 视频生成/图生视频/(（自用）KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1952585965787385858.json, 视频生成/图生视频/Comfy挑战赛第一期自动化视频猫猫转身（每周100美金）_1958457023132286977.json, 视频生成/图生视频/Wan2.2 6步差异模型Sigma调度3迭代图生视频动态加速版V3_1956010463471566849.json, 视频生成/图生视频/图生视频（Wan2.2-V2）高动态加速版_1956567836586070018.json, 视频生成/文生视频/（自用）Wan2.2+提示词工具+无API视频扩写3分镜文生视频加速版V1_1952587209671159809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_127

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/wan2.2图生视频自主prompt＋AI扩写＋API指令融合_1955216249916571650.json、图片生成/文生图/视频-文生视频wan2.2-最强过审_1959964511526662146.json、视频生成/图生视频/(KJ版)Wan2.2+提示词工具+GLM4.5视频扩写图生视频加速版V1_1950813995445977090.json、视频生成/图生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写3分镜图生视频加速版V1_1950934552208416770.json、视频生成/图生视频/(KJ版)Wan2.2+提示词工具+无API视频扩写图生视频加速版V1_1950823826609348610.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWStringConcat`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `TextConcat`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `RH_LLMAPI_NODE` —— 11/12 个有
- `Wan22PromptSelector` —— 11/12 个有
- `JWInteger` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/12 个有
- `LayerUtility: PurgeVRAM` —— 10/12 个有
- `RH_Captioner` —— 10/12 个有
- `WanVideoImageToVideoEncode` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `GetImageSizeAndCount` —— 9/12 个有
- `ImageFromBatch+` —— 9/12 个有
- `FloatToSigmas` —— 3/12 个有
- `LoadLatent` —— 3/12 个有
- `SaveImage` —— 3/12 个有
- `StringToFloatList` —— 3/12 个有
- `Int` —— 2/12 个有
- `MathExpression|pysssss` —— 2/12 个有
- `SaveLatent` —— 2/12 个有
- `WanVideoEmptyEmbeds` —— 2/12 个有
- `GLM_Text_Chat` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `LoadVideo` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
