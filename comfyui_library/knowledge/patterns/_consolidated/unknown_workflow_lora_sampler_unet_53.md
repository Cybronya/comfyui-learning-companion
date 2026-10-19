---
name: unknown_workflow_lora_sampler_unet_53
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.870667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3长视频MV_context_lightx2v_长视频_2089359079314644994.json, 视频生成/图生视频/minimax_h3_多人对话参考+lightx2v正式版_2086399612306415617.json, 视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_53

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/H3长视频MV_context_lightx2v_长视频_2089359079314644994.json、视频生成/图生视频/minimax_h3_多人对话参考+lightx2v正式版_2086399612306415617.json、视频生成/图生视频/【遇见AI】Minimax H3 长视频连续衔接插件 H3 Motion Context REF2V_2090326053301612546.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioInfoNode` —— 2/3 个有
- `MiniMaxH3MotionContext` —— 2/3 个有
- `MiniMaxH3MotionContextLoadLatent` —— 2/3 个有
- `MiniMaxH3MotionContextSaveLatent` —— 2/3 个有
- `MiniMaxH3MotionContextTrim` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `H3SigmaRefiner` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `MmuuaiGroupBypass` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
