---
name: unknown_workflow_video_lora_sampler_102
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8958
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, Fast Groups Bypasser (rgthree), H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Mnimaxh3 极简流分块二采 支持种子固定_2104508927865085954.json, 视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098588498583445506.json, 视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2109663330502795265.json, 视频生成/图生视频/最强去油全模式精简流+独立双采样 MINIMAXH3_2095036845418700801.json, 视频生成/图生视频/最强去油全模式精简流+独立双采样_MINIMAXH3_2095322121126891521.json, 视频生成/图生视频/最强去油全模式精简流+独立双采样_MINIMAXH3_2095425902569152514.json, 视频生成/图生视频/高质量数字人-minimaxh3_2104411993309532161.json, 视频生成/图生视频/高质量数字人-minimaxh3_2106364556749656066.json, 视频生成/文生视频/MINIMAXH3-去油-双采样 （CHIH）_2099542288576892929.json, 视频生成/文生视频/MiniMax_H3_全模式双采样_精简流_优化版_2094975644068302850.json, 视频生成/文生视频/Minimax-H3多参-单采优化-兼顾速度，质量与打斗_2104867248606371842.json, 视频生成/文生视频/Mnimaxh3 极简流分块二采 支持种子固定_2102681029466214402.json, 视频生成/文生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098012326409621505.json, 视频生成/文生视频/文戏-提示词练习_2098925401614671874.json, 视频生成/文生视频/极简双采_2102955651466096641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/Mnimaxh3 极简流分块二采 支持种子固定_2104508927865085954.json、视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098588498583445506.json、视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2109663330502795265.json、视频生成/图生视频/最强去油全模式精简流+独立双采样 MINIMAXH3_2095036845418700801.json、视频生成/图生视频/最强去油全模式精简流+独立双采样_MINIMAXH3_2095322121126891521.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 14/15 个有
- `LoadImage` —— 14/15 个有
- `VAEDecodeAudio` —— 13/15 个有
- `VHS_LoadVideo` —— 12/15 个有
- `LTXVConcatAVLatent` —— 10/15 个有
- `LTXVSeparateAVLatent` —— 10/15 个有
- `MiniMaxH3EasySecondPassConditioning` —— 10/15 个有
- `MinimaxH3LatentUpscaler3D` —— 10/15 个有
- `ModelAttentionBackend` —— 10/15 个有
- `SplitSigmas` —— 10/15 个有
- `Seed (rgthree)` —— 9/15 个有
- `MiniMaxH3EasyMediaLoader` —— 7/15 个有
- `ConditioningZeroOut` —— 5/15 个有
- `GetLatentSizeAndCount` —— 5/15 个有
- `GoohaiMinimaxH3TiledSampler` —— 5/15 个有
- `MiniMaxChunkFeedForward` —— 5/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/15 个有
- `MiniMaxLowVRAMAttention` —— 5/15 个有
- `ModelPreviewOverrideKJ` —— 5/15 个有
- `SelfLiftH3Sampler` —— 5/15 个有
- `LTXVAudioVAEEncode` —— 2/15 个有
- `SetLatentNoiseMask` —— 2/15 个有
- `SolidMask` —— 2/15 个有
- `TrimAudioDuration` —— 2/15 个有
- `Text` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
