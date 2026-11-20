---
name: unknown_workflow_lora_sampler_unet_145
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.872667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/H3 V5_2120038364878565378.json, 平台全量/H3_Character_Swap_v1_Ref2VA_2111488682741030914.json, 平台全量/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2115084874603384833.json, 视频生成/图生视频/单人换视频中的单人（简单提示词)_2113259206127210498.json, 视频生成/文生视频/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2086280720103858177.json, 视频生成/文生视频/MiniMax H3加速优化版  全能参考（人物_场景_音频）_2085671993520771073.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_145

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/H3 V5_2120038364878565378.json、平台全量/H3_Character_Swap_v1_Ref2VA_2111488682741030914.json、平台全量/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2115084874603384833.json、视频生成/图生视频/单人换视频中的单人（简单提示词)_2113259206127210498.json、视频生成/文生视频/MiniMax H3加速优化版  全能参考(9图  _ 3音频 _ 3视频)_2086280720103858177.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/6 个有
- `VAEDecodeAudio` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `Fast Groups Muter (rgthree)` —— 3/6 个有
- `GetVideoComponents` —— 3/6 个有
- `JjkText` —— 3/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `RTXVideoSuperResolution` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `BlockSparseAttention` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
