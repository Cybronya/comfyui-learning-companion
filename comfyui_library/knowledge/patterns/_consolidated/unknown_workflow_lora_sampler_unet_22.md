---
name: unknown_workflow_lora_sampler_unet_22
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.882714
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, GetImageSizeAndCount, GetNode, H3SigmaRefiner, JWFloatToString, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, PrimitiveFloat, RH_LLMAPI_NODE, ResolutionSelector, SaveVideo, Seed Everywhere, SelfLiftAvatarH3Sampler, SetNode, StringFunction|pysssss, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy anythingIndexSwitch, easy int, easy positive, easy saveText, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/视频-参考图生视频(参考视频提示词)-Minnimax-H3-官方_2084949188688834562.json, 视频生成/图生视频/视频-参考图生视频-Minnimax-H3-官方_2085425356214988802.json, 视频生成/图生视频/视频-图生视频-Minnimax-H3-官方_2084294289139527681.json, 视频生成/图生视频/视频-尾帧生视频-Minnimax-H3-官方_2084644226586988545.json, 视频生成/图生视频/视频-数字人对口型图生视频-Minnimax-H3-官方_2084679389672984578.json, 视频生成/图生视频/视频-首尾帧生视频-Minnimax-H3-官方_2084301293325209602.json, 视频生成/文生视频/视频-文生视频-Minnimax-H3-官方_2084278517126221825.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_22

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/视频-参考图生视频(参考视频提示词)-Minnimax-H3-官方_2084949188688834562.json、视频生成/图生视频/视频-参考图生视频-Minnimax-H3-官方_2085425356214988802.json、视频生成/图生视频/视频-图生视频-Minnimax-H3-官方_2084294289139527681.json、视频生成/图生视频/视频-尾帧生视频-Minnimax-H3-官方_2084644226586988545.json、视频生成/图生视频/视频-数字人对口型图生视频-Minnimax-H3-官方_2084679389672984578.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `RH_LLMAPI_NODE`
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
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Int` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `MiniMaxH3ImageToVideo` —— 4/7 个有
- `MiniMaxH3ReferenceToVideo` —— 3/7 个有
- `Text Contains` —— 2/7 个有
- `Text Input Switch` —— 2/7 个有
- `AILab_MiniCPM_4_V` —— 1/7 个有
- `CM_FloatToInt` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `ImageBatchMulti` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `Qwen3ASRLoader_DFT` —— 1/7 个有
- `Qwen3ASRTranscribe_DFT` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/7 个有
- `easy promptReplace` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
