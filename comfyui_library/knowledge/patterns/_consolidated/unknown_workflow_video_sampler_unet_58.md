---
name: unknown_workflow_video_sampler_unet_58
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.877667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json, 视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json, 视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json, 视频生成/文生视频/MiniMax H3最新音乐驱动多图参考MV生成工作流🐘承象_2087393176142303234.json, 视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json, 视频生成/文生视频/视频生成（文生_图生_参考生）Minimax-H3_2087564591730618370.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiNiMax H3 高质量工作流_2092902067592585217.json、视频生成/文生视频/MiniMax H3 Text to Video文生视频量化版本_2084179057368981506.json、视频生成/文生视频/MiniMax H3全能参考_2084306466529439745.json、视频生成/文生视频/MiniMax H3最新音乐驱动多图参考MV生成工作流🐘承象_2087393176142303234.json、视频生成/文生视频/MiniMax H3满血版 生视频【4步加速优化版+可出1080】_2085719967990898690.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `Label (rgthree)` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `LoadAudio` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerUtility: TextBox` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `ReservedVRAMSetter` —— 1/6 个有
- `SolAttnMiniMax` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
