---
name: unknown_workflow_lora_sampler_unet_97
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.884333
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, GetImageSizeAndCount, GetNode, H3SigmaRefiner, JWFloatToString, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, PrimitiveFloat, ResolutionSelector, SaveVideo, Seed Everywhere, SelfLiftAvatarH3Sampler, SetNode, StringFunction|pysssss, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-动作迁移模仿编辑替换-Minnimax-H3-官方_2086019093680975873.json, 平台全量/视频-视频编辑转绘-Minnimax-H3-官方_2084654421836910594.json, 视频生成/图生视频/视频-参考图生视频(参考视频提示词)-Minnimax-H3-官方_2084949188688834562.json, 视频生成/图生视频/视频-参考图生视频-Minnimax-H3-官方_2085425356214988802.json, 视频生成/图生视频/视频-图生视频-Minnimax-H3-官方_2084294289139527681.json, 视频生成/图生视频/视频-尾帧生视频-Minnimax-H3-官方_2084644226586988545.json, 视频生成/图生视频/视频-数字人对口型图生视频-Minnimax-H3-官方_2084679389672984578.json, 视频生成/图生视频/视频-首尾帧生视频-Minnimax-H3-官方_2084301293325209602.json, 视频生成/文生视频/视频-文生视频-Minnimax-H3-官方_2084278517126221825.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_97

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/视频-动作迁移模仿编辑替换-Minnimax-H3-官方_2086019093680975873.json、平台全量/视频-视频编辑转绘-Minnimax-H3-官方_2084654421836910594.json、视频生成/图生视频/视频-参考图生视频(参考视频提示词)-Minnimax-H3-官方_2084949188688834562.json、视频生成/图生视频/视频-参考图生视频-Minnimax-H3-官方_2085425356214988802.json、视频生成/图生视频/视频-图生视频-Minnimax-H3-官方_2084294289139527681.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `GetImageSizeAndCount`
- `GetNode`
- `H3SigmaRefiner`
- `JWFloatToString`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveVideo`
- `Seed Everywhere`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `StringFunction|pysssss`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `RH_LLMAPI_NODE` —— 8/9 个有
- `llama_cpp_instruct_adv` —— 7/9 个有
- `llama_cpp_model_loader` —— 7/9 个有
- `llama_cpp_parameters` —— 7/9 个有
- `MiniMaxH3ReferenceToVideo` —— 5/9 个有
- `MiniMaxH3ImageToVideo` —— 4/9 个有
- `CM_FloatToInt` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `PreviewAudio` —— 2/9 个有
- `Text Contains` —— 2/9 个有
- `Text Input Switch` —— 2/9 个有
- `VHS_VideoInfoLoaded` —— 2/9 个有
- `AILab_MiniCPM_4_V` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `Qwen3ASRLoader_DFT` —— 1/9 个有
- `Qwen3ASRTranscribe_DFT` —— 1/9 个有
- `Qwen3_VQA_Plus` —— 1/9 个有
- `SoundFlow_GetLength` —— 1/9 个有
- `TextGenerateV2` —— 1/9 个有
- `TrimAudioDuration` —— 1/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/9 个有
- `VideoInfoLoaded` —— 1/9 个有
- `easy promptReplace` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
