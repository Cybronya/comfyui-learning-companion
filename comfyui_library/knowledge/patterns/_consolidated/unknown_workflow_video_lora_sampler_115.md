---
name: unknown_workflow_video_lora_sampler_115
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.796154
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, JWStringConcat, LoadWanVideoT5TextEncoder, ShowText|pysssss, TextConcat, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: [ImageFromBatch+, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, CR Prompt Text]
members: [图片生成/文生图/1959964511526662146.json, 视频生成/图生视频/1950813995445977090.json, 视频生成/图生视频/1950934552208416770.json, 视频生成/图生视频/1950823826609348610.json, 视频生成/图生视频/1953756753928355841.json, 视频生成/图生视频/1954077934976061442.json, 视频生成/图生视频/1952585965787385858.json, 视频生成/图生视频/1958457023132286977.json, 视频生成/图生视频/1956010463471566849.json, 视频生成/图生视频/1970020251171758081.json, 视频生成/图生视频/1956567836586070018.json, 视频生成/图生视频/1963544329490092033.json, 视频生成/文生视频/1953756767052288002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_115

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1959964511526662146.json、视频生成/图生视频/1950813995445977090.json、视频生成/图生视频/1950934552208416770.json、视频生成/图生视频/1950823826609348610.json、视频生成/图生视频/1953756753928355841.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 13 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWStringConcat`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `TextConcat`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
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
- `GetImageSizeAndCount` —— 12/13 个有
- `JWInteger` —— 12/13 个有
- `RH_LLMAPI_NODE` —— 12/13 个有
- `WanVideoTorchCompileSettings` —— 12/13 个有
- `ImageFromBatch+` —— 9/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/13 个有
- `LayerUtility: PurgeVRAM` —— 9/13 个有
- `LoadImage` —— 9/13 个有
- `RH_Captioner` —— 9/13 个有
- `WanVideoImageToVideoEncode` —— 9/13 个有
- `FloatToSigmas` —— 4/13 个有
- `StringToFloatList` —— 4/13 个有
- `WanVideoEmptyEmbeds` —— 4/13 个有
- `LoadLatent` —— 2/13 个有
- `SaveImage` —— 2/13 个有
- `GLM_Text_Chat` —— 1/13 个有
- `Int` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoadVideo` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `SaveLatent` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：ImageFromBatch+、LayerUtility: PurgeVRAM V2、MathExpression|pysssss、CR Prompt Text
