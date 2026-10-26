---
name: unknown_workflow_video_lora_sampler_695
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.651667
common_nodes: [BasicGuider, BasicScheduler, FeiHouEasyH3RH, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, KSamplerSelect, LTXVConcatAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, SetNode, UniBlockSwap, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, VRAM_Debug, easy clearCacheAll, easy ifElse]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3全能参考：电影质量V2_2095725291497938946.json, 视频生成/文生视频/MinimaxH3全能参考：电影质量V3（浅空间放大版）_2094139603556069377.json, 视频生成/文生视频/MinimaxH3全能参考：高画质电影感V2_2094095183708246018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_695

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3全能参考：电影质量V2_2095725291497938946.json、视频生成/文生视频/MinimaxH3全能参考：电影质量V3（浅空间放大版）_2094139603556069377.json、视频生成/文生视频/MinimaxH3全能参考：高画质电影感V2_2094095183708246018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UniBlockSwap`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy clearCacheAll`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `MiniMaxH3BlockCacheT8` —— 2/3 个有
- `MiniMaxLowVRAMAttention` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `SplitSigmas` —— 2/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `RandomSeedNoise` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAEEncodeAudio` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
