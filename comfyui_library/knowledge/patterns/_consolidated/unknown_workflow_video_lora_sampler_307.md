---
name: unknown_workflow_video_lora_sampler_307
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.856571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Easy, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minmax H3-VDN +SelfLift 采样直出1080P_2098822938639290370.json, 视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098588498583445506.json, 视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2109663330502795265.json, 视频生成/文生视频/MiniMax H3 双采样全面升级版｜文戏不油｜武戏不糊_2099322604426457090.json, 视频生成/文生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098012326409621505.json, 视频生成/文生视频/文戏-提示词练习_2098925401614671874.json, 视频生成/文生视频/极简双采_2102955651466096641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_307

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minmax H3-VDN +SelfLift 采样直出1080P_2098822938639290370.json、视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098588498583445506.json、视频生成/图生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2109663330502795265.json、视频生成/文生视频/MiniMax H3 双采样全面升级版｜文戏不油｜武戏不糊_2099322604426457090.json、视频生成/文生视频/文不油 武不糊！MINIMAXH3 双采样V3  全面升级！_2098012326409621505.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyMediaLoader`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetLatentSizeAndCount` —— 6/7 个有
- `ModelAttentionBackend` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `CreateVideo` —— 1/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/7 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `easy imageChooser` —— 1/7 个有
- `easy promptConcat` —— 1/7 个有
- `kkVideoFirstLastFrames` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
