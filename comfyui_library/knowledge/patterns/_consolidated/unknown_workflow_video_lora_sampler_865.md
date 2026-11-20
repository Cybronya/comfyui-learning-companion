---
name: unknown_workflow_video_lora_sampler_865
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8255
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), H3SigmaRefiner, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3Easy, MiniMaxH3EasyMediaLoader, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minmax H3-VDN +SelfLift 采样直出1080P_2098822938639290370.json, 视频生成/文生视频/MiniMax H3 双采样全面升级版｜文戏不油｜武戏不糊_2099322604426457090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_865

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minmax H3-VDN +SelfLift 采样直出1080P_2098822938639290370.json、视频生成/文生视频/MiniMax H3 双采样全面升级版｜文戏不油｜武戏不糊_2099322604426457090.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CreateVideo` —— 1/2 个有
- `GetLatentSizeAndCount` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `easy imageChooser` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有
- `kkVideoFirstLastFrames` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
