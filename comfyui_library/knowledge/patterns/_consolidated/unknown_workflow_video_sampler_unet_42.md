---
name: unknown_workflow_video_sampler_unet_42
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8755
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/Minimax_H3二采优化速度-self_lift-多参考_2100933071129370625.json, 视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采 + Sage加速_2109787600222515201.json, 视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采｜Sage加速_2109751193818984450.json, 视频生成/图生视频/Minimax H3二采优化速度-self lift-多参考_2100096995984756738.json, 视频生成/图生视频/超快Minimax H3+self双采-音频驱动数字人-自动扩写-高质量match+B2549_2100842372438515713.json, 视频生成/图生视频/高画质Minimax H3+self双采-音频驱动数字人-自动扩写-高质量max+BF16_2100836207176536066.json, 视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json, 视频生成/文生视频/Minimax H3二采数字人-self lift-单图三人音频参考_2098822938328915970.json, 视频生成/文生视频/Minimax H3二采数字人-self lift-单图单人音频_2098822916216541186.json, 视频生成/文生视频/Minimax H3二采数字人-self lift-单图双人音频参考_2098822926341599234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Minimax_H3二采优化速度-self_lift-多参考_2100933071129370625.json、视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采 + Sage加速_2109787600222515201.json、视频生成/图生视频/Minimax H3 高质量高速度全能参考｜Self-lift 双采｜Sage加速_2109751193818984450.json、视频生成/图生视频/Minimax H3二采优化速度-self lift-多参考_2100096995984756738.json、视频生成/图生视频/超快Minimax H3+self双采-音频驱动数字人-自动扩写-高质量match+B2549_2100842372438515713.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
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
- `MiniMaxChunkFeedForward` —— 8/10 个有
- `MiniMaxLowVRAMAttention` —— 8/10 个有
- `SelfLiftH3Sampler` —— 8/10 个有
- `CR Prompt Text` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `SelfLiftAvatarH3Sampler` —— 2/10 个有
- `ShellAgentPluginOutputText` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
