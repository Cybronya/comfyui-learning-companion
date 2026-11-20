---
name: unknown_workflow_video_lora_sampler_317
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.880667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, Fast Groups Bypasser (rgthree), H3SigmaRefiner, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/文不油_武不糊！MINIMAXH3_双采样V3_全面升级！_2118111267121618946.json, 平台全量/文武全能 MINIMAXH3 双采样V4_2115296750738169857.json, 平台全量/文武全能 MINIMAXH3 双采样V4_2119632947182657538.json, 视频生成/图生视频/Mnimaxh3 极简流分块二采 支持种子固定_2104508927865085954.json, 视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098588498583445506.json, 视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2109663330502795265.json, 视频生成/文生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098012326409621505.json, 视频生成/文生视频/文戏-提示词练习_2098925401614671874.json, 视频生成/文生视频/极简双采_2102955651466096641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_317

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/文不油_武不糊！MINIMAXH3_双采样V3_全面升级！_2118111267121618946.json、平台全量/文武全能 MINIMAXH3 双采样V4_2115296750738169857.json、平台全量/文武全能 MINIMAXH3 双采样V4_2119632947182657538.json、视频生成/图生视频/Mnimaxh3 极简流分块二采 支持种子固定_2104508927865085954.json、视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098588498583445506.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `GetLatentSizeAndCount` —— 8/9 个有
- `MiniMaxChunkFeedForward` —— 8/9 个有
- `MiniMaxH3EasyMediaLoader` —— 8/9 个有
- `MiniMaxLowVRAMAttention` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `SelfLiftH3Sampler` —— 6/9 个有
- `GoohaiMinimaxH3TiledSampler` —— 3/9 个有
- `LTXVConcatAVLatent` —— 3/9 个有
- `LTXVSeparateAVLatent` —— 3/9 个有
- `MiniMaxH3EasySecondPassConditioning` —— 3/9 个有
- `MinimaxH3LatentUpscaler3D` —— 3/9 个有
- `SplitSigmas` —— 3/9 个有
- `BlockSparseAttention` —— 2/9 个有
- `SelfLiftAvatarH3Sampler` —— 2/9 个有
- `JDCN_VHSFileMover` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `Vignette` —— 1/9 个有
- `easy saveText` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
