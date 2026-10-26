---
name: unknown_workflow_video_sampler_unet_17
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.879687
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, ResolutionSelector, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-match-真人感自动扩写_2099747367561027586.json, 视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-手动提示词-match_2099732844124917762.json, 视频生成/图生视频/Minimax_H3音频驱动数字人-b25-49-match-真人感自动扩写_2100401840990023682.json, 视频生成/图生视频/动态图形特效--B25-49-音频驱动-match-提示词自动扩写_2100218651189268481.json, 视频生成/图生视频/动态图形特效--BF16-音频驱动-max-提示词自动扩写_2100218674220199938.json, 视频生成/图生视频/单人口播特调--Minimax H3音频驱动数字人-b25-49-真人感自动扩写_2099757704570032130.json, 视频生成/图生视频/双采极速！动态图形特效--B25-49-音频驱动-match-提示词自动扩写_2100851572338159617.json, 视频生成/图生视频/双采极速！动态图形特效--BF16-音频驱动-高质量max-提示词自动扩写_2100851579585912833.json, 视频生成/图生视频/多图参考生成视频Minimax+H3 极致满血1K-10秒 双bf16-+sage加速_2090611037820243970.json, 视频生成/图生视频/超快Minimax H3+self双采-音频驱动数字人-自动扩写-高质量match+B2549_2100842372438515713.json, 视频生成/图生视频/高画质Minimax H3+self双采-音频驱动数字人-自动扩写-高质量max+BF16_2100836207176536066.json, 视频生成/图生视频/高质量-Minimax H3音频驱动数字人BF16-max-真人感自动扩写_2099744481288478722.json, 视频生成/文生视频/动作打斗自动扩写！多参考Minimax H3-B25-49-高质量768P打斗lora_2095856171046494210.json, 视频生成/文生视频/动作打斗自动扩写！多参考Minimax H3-BF16-高质量768P打斗lora_2095856177950318593.json, 视频生成/文生视频/动作打斗自动扩写！多参考Minimax H3-Dasiwa-高质量768P打斗lora_2095856160921444353.json, 音频生成/音频生成/Minimax_H3音频驱动数字人-b25-49-match-真人感自动扩写_2100490323058315265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-match-真人感自动扩写_2099747367561027586.json、视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-手动提示词-match_2099732844124917762.json、视频生成/图生视频/Minimax_H3音频驱动数字人-b25-49-match-真人感自动扩写_2100401840990023682.json、视频生成/图生视频/动态图形特效--B25-49-音频驱动-match-提示词自动扩写_2100218651189268481.json、视频生成/图生视频/动态图形特效--BF16-音频驱动-max-提示词自动扩写_2100218674220199938.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 14/16 个有
- `ShellAgentPluginOutputText` —— 14/16 个有
- `easy showAnything` —— 14/16 个有
- `LoraLoaderModelOnly` —— 13/16 个有
- `BasicGuider` —— 12/16 个有
- `LoadAudio` —— 12/16 个有
- `RandomNoise` —— 12/16 个有
- `SamplerCustomAdvanced` —— 12/16 个有
- `TrimAudioDuration` —— 12/16 个有
- `LayerUtility: PurgeVRAM V2` —— 10/16 个有
- `ConditioningZeroOut` —— 4/16 个有
- `Qwen3ASRLoader` —— 4/16 个有
- `Qwen3ASRTranscribe` —— 4/16 个有
- `SelfLiftAvatarH3Sampler` —— 4/16 个有
- `RHMiniMaxH3T2VATextEncode` —— 3/16 个有
- `H3SigmaRefiner` —— 2/16 个有
- `MiniMaxChunkFeedForward` —— 2/16 个有
- `MiniMaxLowVRAMAttention` —— 2/16 个有
- `PrimitiveStringMultiline` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
