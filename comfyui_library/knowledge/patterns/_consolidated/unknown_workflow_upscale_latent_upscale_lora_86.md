---
name: unknown_workflow_upscale_latent_upscale_lora_86
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9585
common_nodes: [BasicGuider, BasicScheduler, CreateVideo, H3SigmaRefiner, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, 孤海注释]
problems: []
missing: []
members: [平台全量/H3参考轨迹路径运镜工作流_2092260569507254273.json, 视频生成/文生视频/那颗星星 _ MinimaxH3 二采潜空间放大 极简版_2089560595371745281.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_86

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/H3参考轨迹路径运镜工作流_2092260569507254273.json、视频生成/文生视频/那颗星星 _ MinimaxH3 二采潜空间放大 极简版_2089560595371745281.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CreateVideo`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `GetLatentSizeAndCount` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `MiniMaxH3AVDecodeT8` —— 1/2 个有
- `MiniMaxH3EasyLoader` —— 1/2 个有
- `MiniMaxH3EasyModelAdapter` —— 1/2 个有
- `MiniMaxH3EasySecondPassConditioning` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `SolAttnMiniMax` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
