---
name: unknown_workflow_sampler_unet_vae_116
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.824444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084908134719643649.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084998635074445314.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2085402316232019969.json, 视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json, 视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json, 视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json, 视频生成/文生视频/3-MiniMax-H3-参考生视频工作流-V2_2084639172459065346.json, 视频生成/文生视频/DG_H3 文生视频 BF16高质量_2085624042417123330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_116

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V4_2084169977384497154.json、视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084908134719643649.json、视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084998635074445314.json、视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2085402316232019969.json、视频生成/文生视频/1-Aiden-minimax-文生视频_2097381153186607106.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `MiniMaxH3ImageToVideo` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `CR Prompt Text` —— 6/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `MiniMaxH3BlockCacheT8` —— 4/9 个有
- `ModelAttentionBackend` —— 4/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/9 个有
- `MiniMaxH3SigmaShift` —— 3/9 个有
- `LoadImage` —— 2/9 个有
- `MiniMaxH3ContextIR` —— 2/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `MiniMaxH3AVDecodeT8` —— 1/9 个有
- `MiniMaxH3ReferenceToVideo` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `VHS_LoadAudioUpload` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
