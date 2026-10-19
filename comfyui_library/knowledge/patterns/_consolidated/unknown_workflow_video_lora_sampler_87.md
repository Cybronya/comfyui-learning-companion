---
name: unknown_workflow_video_lora_sampler_87
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.893312
common_nodes: [BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, ResolutionSelector, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3动作增强修复双采（包含脸部修复和高动态修复）_2098315228005093378.json, 视频生成/图生视频/Minimax H3超真实最强数字人_2102034695067365378.json, 视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-match-真人感自动扩写_2099747367561027586.json, 视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-手动提示词-match_2099732844124917762.json, 视频生成/图生视频/Minimax_H3音频驱动数字人-b25-49-match-真人感自动扩写_2100401840990023682.json, 视频生成/图生视频/动态图形特效--B25-49-音频驱动-match-提示词自动扩写_2100218651189268481.json, 视频生成/图生视频/动态图形特效--BF16-音频驱动-max-提示词自动扩写_2100218674220199938.json, 视频生成/图生视频/单人口播特调--Minimax H3音频驱动数字人-b25-49-真人感自动扩写_2099757704570032130.json, 视频生成/图生视频/双采极速！动态图形特效--B25-49-音频驱动-match-提示词自动扩写_2100851572338159617.json, 视频生成/图生视频/双采极速！动态图形特效--BF16-音频驱动-高质量max-提示词自动扩写_2100851579585912833.json, 视频生成/图生视频/高质量-Minimax H3音频驱动数字人BF16-max-手动提示词_2099743464232669186.json, 视频生成/图生视频/高质量-Minimax H3音频驱动数字人BF16-max-真人感自动扩写_2099744481288478722.json, 视频生成/文生视频/动作打斗自动扩写！多参考Minimax H3-B25-49-高质量768P打斗lora_2095856171046494210.json, 视频生成/文生视频/动作打斗自动扩写！多参考Minimax H3-BF16-高质量768P打斗lora_2095856177950318593.json, 视频生成/文生视频/动作打斗自动扩写！多参考Minimax H3-Dasiwa-高质量768P打斗lora_2095856160921444353.json, 音频生成/音频生成/Minimax_H3音频驱动数字人-b25-49-match-真人感自动扩写_2100490323058315265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_87

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Minimax H3动作增强修复双采（包含脸部修复和高动态修复）_2098315228005093378.json、视频生成/图生视频/Minimax H3超真实最强数字人_2102034695067365378.json、视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-match-真人感自动扩写_2099747367561027586.json、视频生成/图生视频/Minimax H3音频驱动数字人-b25-49-手动提示词-match_2099732844124917762.json、视频生成/图生视频/Minimax_H3音频驱动数字人-b25-49-match-真人感自动扩写_2100401840990023682.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 14/16 个有
- `RandomNoise` —— 14/16 个有
- `SamplerCustomAdvanced` —— 14/16 个有
- `LoadAudio` —— 13/16 个有
- `RH_LLMAPI_Pro_Node` —— 12/16 个有
- `ShellAgentPluginOutputText` —— 12/16 个有
- `TrimAudioDuration` —— 12/16 个有
- `easy showAnything` —— 12/16 个有
- `LayerUtility: PurgeVRAM V2` —— 7/16 个有
- `Qwen3ASRLoader` —— 4/16 个有
- `Qwen3ASRTranscribe` —— 4/16 个有
- `RHMiniMaxH3T2VATextEncode` —— 3/16 个有
- `ConditioningZeroOut` —— 2/16 个有
- `SelfLiftAvatarH3Sampler` —— 2/16 个有
- `LTXVConcatAVLatent` —— 1/16 个有
- `LTXVSeparateAVLatent` —— 1/16 个有
- `MinimaxH3LatentUpscaler3D` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
