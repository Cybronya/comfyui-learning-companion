---
name: unknown_workflow_sampler_vae_20
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.677706
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/H3 快速单图参考视频_2119876573464715266.json, 平台全量/MINIMAX-H3多参_2085070521007435777.json, 平台全量/MiniMAX-H3 -4图10秒服装带货王｜官方4步直出_2117906185696403458.json, 平台全量/MiniMax H3多图参考生视频_2117256618483216386.json, 平台全量/MiniMaxH3全能参考生视频_2121110307115458562.json, 平台全量/Minmax多参考生成视频R2V_2102928965102039041.json, 平台全量/Minmax多参考生成视频R2V_2103670515260022785.json, 平台全量/Minmax多参考生成视频R2V_2104845464511270913.json, 平台全量/minimaxh3 9图3视频3音频一采 4步lora_2093166490710265857.json, 平台全量/minimaxh3 9图3视频3音频一采 8步lora_2093205556940070914.json, 视频生成/图生视频/FastH3 Omni参考生视频极速版_2115782285361500161.json, 视频生成/图生视频/MiniMax H3-全能参考  三图版+一视频_2094421879401574401.json, 视频生成/图生视频/MiniMax H3：参考生视频（加速）_2096113080844513282.json, 视频生成/图生视频/MiniMax-H3 极限复杂场景 _ 高速运动大动态 _ 高质感无画面劣化  抗形变模糊工作流  （工作版）_2108809186309136386.json, 视频生成/图生视频/MiniMax-H3 高速大动态 速度快 不模糊_2114541691175784450.json, 视频生成/图生视频/MiniMax-H3_高速大动态_无劣化抗形变模糊工作流_工作版_2113780111102271490.json, 视频生成/图生视频/MiniMax-H3_高速大动态_速度快_不模糊_2114884603973554178.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/H3 快速单图参考视频_2119876573464715266.json、平台全量/MINIMAX-H3多参_2085070521007435777.json、平台全量/MiniMAX-H3 -4图10秒服装带货王｜官方4步直出_2117906185696403458.json、平台全量/MiniMax H3多图参考生视频_2117256618483216386.json、平台全量/MiniMaxH3全能参考生视频_2121110307115458562.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 15/17 个有
- `LoraLoaderModelOnly` —— 14/17 个有
- `BasicScheduler` —— 12/17 个有
- `PrimitiveBoolean` —— 12/17 个有
- `ModelAttentionBackend` —— 11/17 个有
- `LoadAudio` —— 10/17 个有
- `MiniMaxH3SigmaShift` —— 10/17 个有
- `GetNode` —— 9/17 个有
- `SetNode` —— 9/17 个有
- `VHS_LoadVideo` —— 9/17 个有
- `BlockSparseAttention` —— 8/17 个有
- `ComfySwitchNode` —— 8/17 个有
- `PrimitiveInt` —— 6/17 个有
- `ManualSigmas` —— 5/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/17 个有
- `Fast Bypasser (rgthree)` —— 4/17 个有
- `GetVideoComponents` —— 4/17 个有
- `LoadVideo` —— 4/17 个有
- `MiniMaxChunkFeedForward` —— 4/17 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/17 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/17 个有
- `MiniMaxLowVRAMAttention` —— 4/17 个有
- `ModelPreviewOverrideKJ` —— 4/17 个有
- `SplitSigmas` —— 4/17 个有
- `VRAM_Debug` —— 4/17 个有
- `easy ifElse` —— 4/17 个有
- `布尔孤海` —— 4/17 个有
- `MiniMaxH3HybridLoader` —— 2/17 个有
- `SolAttnPatch` —— 2/17 个有
- `VedaSparseAttention` —— 2/17 个有
- `EmptyImage` —— 1/17 个有
- `PreviewImage` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
