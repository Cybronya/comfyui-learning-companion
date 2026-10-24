---
name: unknown_workflow_video_upscale_latent_upscale_50
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.90825
common_nodes: [BasicGuider, BasicScheduler, Fast Groups Bypasser (rgthree), H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, MiniMaxH3EasySecondPassConditioning, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/高质量数字人-minimaxh3_2104411993309532161.json, 视频生成/图生视频/高质量数字人-minimaxh3_2106364556749656066.json, 视频生成/文生视频/MINIMAXH3-去油-双采样 （CHIH）_2099542288576892929.json, 视频生成/文生视频/MiniMax_H3_全模式双采样_精简流_优化版_2094975644068302850.json, 视频生成/文生视频/Minimax-H3多参-单采优化-兼顾速度，质量与打斗_2104867248606371842.json, 视频生成/文生视频/Mnimaxh3 极简流分块二采 支持种子固定_2102681029466214402.json, 视频生成/文生视频/最强去油全模式精简流+独立双采样 MINIMAXH3_2094672915202662401.json, 视频生成/文生视频/高质量全模式精简流+独立双采样 MINIMAXH3_2090235980585455617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_50

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/高质量数字人-minimaxh3_2104411993309532161.json、视频生成/图生视频/高质量数字人-minimaxh3_2106364556749656066.json、视频生成/文生视频/MINIMAXH3-去油-双采样 （CHIH）_2099542288576892929.json、视频生成/文生视频/MiniMax_H3_全模式双采样_精简流_优化版_2094975644068302850.json、视频生成/文生视频/Minimax-H3多参-单采优化-兼顾速度，质量与打斗_2104867248606371842.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3EasySecondPassConditioning`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `LoadAudio` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `MiniMaxH3EasyModelAdapter` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `VAELoader` —— 7/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `GoohaiMinimaxH3TiledSampler` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `LTXVAudioVAEEncode` —— 2/8 个有
- `MiniMaxH3EasyMediaLoader` —— 2/8 个有
- `SetLatentNoiseMask` —— 2/8 个有
- `SolidMask` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `MiniMaxH3EasyLoader` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
