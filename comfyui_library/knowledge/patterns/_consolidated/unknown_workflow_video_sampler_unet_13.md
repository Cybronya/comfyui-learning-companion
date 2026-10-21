---
name: unknown_workflow_video_sampler_unet_13
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.872043
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采 + Sage加速_2109787600222515201.json, 视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采｜Sage加速_2109751193818984450.json, 视频生成/图生视频/Minimax H3二采优化速度-self lift-多参考_2100096995984756738.json, 视频生成/图生视频/超快Minimax H3+self双采-音频驱动数字人-自动扩写-高质量match+B2549_2100842372438515713.json, 视频生成/图生视频/高画质Minimax H3+self双采-音频驱动数字人-自动扩写-高质量max+BF16_2100836207176536066.json, 视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json, 视频生成/文生视频/Minimax H3二采数字人-self lift-单图三人音频参考_2098822938328915970.json, 视频生成/文生视频/Minimax H3二采数字人-self lift-单图单人音频_2098822916216541186.json, 视频生成/文生视频/Minimax H3二采数字人-self lift-单图双人音频参考_2098822926341599234.json, 视频生成/文生视频/Minimax+H3-self-lift双采-仅sage加速-25步max质量_2098041547420954626.json, 视频生成/文生视频/selfift双采BF16max-多宫格单图专用-三音色参考_2105995712277344257.json, 视频生成/文生视频/selfift双采BF16max-多宫格单图专用-单音色参考_2106002184415567874.json, 视频生成/文生视频/selfift双采BF16max-多宫格单图专用-双音色参考_2106002191558463489.json, 视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json, 视频生成/文生视频/高质量打斗Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098058645392154625.json, 视频生成/文生视频/高质量打斗Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098058666183315458.json, 视频生成/文生视频/高质量高速度Minimax H3-self-lift双采-BF16+sage加速25步max_2098043041310404610.json, 视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098043805441286146.json, 视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098043798923333634.json, 视频生成/文生视频/高速度低显存Minimax+H3-self-lift双采-4步lora-6步-均衡版_2097983381266067458.json, 视频生成/文生视频/高速度低显存Minimax+H3-self-lift双采-4步lora-8步-质量版_2097983391957340162.json, 视频生成/文生视频/高速度低显存Minimax+H3-self-lift双采-8步lora-10步-均衡版_2097983402602491905.json, 视频生成/文生视频/高速度低显存Minimax+H3-self-lift双采-8步lora-12步-质量版_2097983412752703489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采 + Sage加速_2109787600222515201.json、视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采｜Sage加速_2109751193818984450.json、视频生成/图生视频/Minimax H3二采优化速度-self lift-多参考_2100096995984756738.json、视频生成/图生视频/超快Minimax H3+self双采-音频驱动数字人-自动扩写-高质量match+B2549_2100842372438515713.json、视频生成/图生视频/高画质Minimax H3+self双采-音频驱动数字人-自动扩写-高质量max+BF16_2100836207176536066.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `SelfLiftH3Sampler` —— 21/23 个有
- `MiniMaxChunkFeedForward` —— 15/23 个有
- `MiniMaxLowVRAMAttention` —— 15/23 个有
- `LoadAudio` —— 12/23 个有
- `LoraLoaderModelOnly` —— 10/23 个有
- `CR Prompt Text` —— 2/23 个有
- `RH_LLMAPI_Pro_Node` —— 2/23 个有
- `SelfLiftAvatarH3Sampler` —— 2/23 个有
- `ShellAgentPluginOutputText` —— 2/23 个有
- `TrimAudioDuration` —— 2/23 个有
- `easy showAnything` —— 2/23 个有
- `LoraLoaderBypassModelOnly` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
