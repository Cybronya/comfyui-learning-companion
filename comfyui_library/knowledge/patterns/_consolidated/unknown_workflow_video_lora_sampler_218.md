---
name: unknown_workflow_video_lora_sampler_218
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9123
common_nodes: [CreateCFGScheduleFloatList, Float, GetImageSizeAndCount, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Comfy挑战赛6（心跳）Wan2.2图生视频+音频_1971183114510864385.json, 视频生成/图生视频/Comfy挑战赛7（不可能的菜肴）-图生视频_1974013871881105409.json, 视频生成/图生视频/KJ版Wan2.2新版高噪模型V210s以上_2021029797077454850.json, 视频生成/图生视频/Lightx2v 1030 差异模型高低噪自动提示词图生视频V1_1984646206687232002.json, 视频生成/图生视频/Wan2.2 20秒长视频+音频生成（Comfy挑战赛5 无限飞行）_1976203994194427906.json, 视频生成/图生视频/Wan2.2 四段续写长视频_2073212221412438017.json, 视频生成/图生视频/Wan2.2文生视频+音频 (1)_2066681308595712001.json, 视频生成/图生视频/Wan2.2文生视频+音频_2055171452390912002.json, 视频生成/图生视频/无限飞行 视频+音频_2026898938053271554.json, 视频生成/文生视频/Comfy挑战赛5（无限飞行）Wan2.2 20秒长视频+音频生成（100美元奖金）V2_1968636624055750658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_218

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Comfy挑战赛6（心跳）Wan2.2图生视频+音频_1971183114510864385.json、视频生成/图生视频/Comfy挑战赛7（不可能的菜肴）-图生视频_1974013871881105409.json、视频生成/图生视频/KJ版Wan2.2新版高噪模型V210s以上_2021029797077454850.json、视频生成/图生视频/Lightx2v 1030 差异模型高低噪自动提示词图生视频V1_1984646206687232002.json、视频生成/图生视频/Wan2.2 20秒长视频+音频生成（Comfy挑战赛5 无限飞行）_1976203994194427906.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Float`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `HunyuanVideoFoley` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `WanVideoImageToVideoEncode` —— 8/10 个有
- `LoadImage` —— 7/10 个有
- `SaveLatent` —— 7/10 个有
- `VAEEncode` —— 7/10 个有
- `VAELoader` —— 7/10 个有
- `LayerUtility: PurgeVRAM V2` —— 5/10 个有
- `easy showAnything` —— 5/10 个有
- `ImageFromBatch+` —— 4/10 个有
- `StringToFloatList` —— 4/10 个有
- `easy batchAnything` —— 4/10 个有
- `text_mul_replace` —— 4/10 个有
- `WanVideoEmptyEmbeds` —— 3/10 个有
- `LayerUtility: PurgeVRAM` —— 2/10 个有
- `AILab_MiniCPM_4_V` —— 1/10 个有
- `AILab_QwenVL` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `GetVideoComponents` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `ReplaceText` —— 1/10 个有
- `ShowText` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
