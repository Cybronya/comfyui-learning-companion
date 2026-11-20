---
name: unknown_workflow_lora_sampler_unet_325
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8395
common_nodes: [AudioInfoNode, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, VRGDG_MiniMaxH3AudioDrive, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/H3长视频MV_context_lightx2v_长视频_2089359079314644994.json, 视频生成/图生视频/minimax_h3_多人对话参考+lightx2v正式版_2086399612306415617.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_325

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3长视频MV_context_lightx2v_长视频_2089359079314644994.json、视频生成/图生视频/minimax_h3_多人对话参考+lightx2v正式版_2086399612306415617.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioInfoNode`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `MiniMaxH3MotionContext` —— 1/2 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/2 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/2 个有
- `MiniMaxH3MotionContextTrim` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MmuuaiGroupBypass` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
