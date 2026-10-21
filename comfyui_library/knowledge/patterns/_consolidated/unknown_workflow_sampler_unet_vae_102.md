---
name: unknown_workflow_sampler_unet_vae_102
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.818375
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax H3 文生视频标准版_2094294196017524737.json, 视频生成/文生视频/Minimax H3 极速文生视频_2085290047233945602.json, 视频生成/文生视频/Minimax H3-t2v 官方提示词文生视频_2085182661756276737.json, 视频生成/文生视频/Minimax H3-t2v 官方版文生视频_2084192379581583362.json, 视频生成/文生视频/Minimax H3视频模型文生视频_2084169698551361537.json, 视频生成/文生视频/Minimax H3高质量融合模型10Eros-图生视频BF16加速_2086859043209039874.json, 视频生成/文生视频/Minimax文生视频高质量极速版_2084997026189758466.json, 视频生成/文生视频/智能版minimax+H3+开源版+文生视频+T2VA文生_2084150373744472066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_102

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/Minimax H3 文生视频标准版_2094294196017524737.json、视频生成/文生视频/Minimax H3 极速文生视频_2085290047233945602.json、视频生成/文生视频/Minimax H3-t2v 官方提示词文生视频_2085182661756276737.json、视频生成/文生视频/Minimax H3-t2v 官方版文生视频_2084192379581583362.json、视频生成/文生视频/Minimax H3视频模型文生视频_2084169698551361537.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3BlockCacheT8` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CacheDiT_Model_Optimizer` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/8 个有
- `MiniMaxH3SigmaShift` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
