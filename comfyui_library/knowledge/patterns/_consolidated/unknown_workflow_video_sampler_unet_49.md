---
name: unknown_workflow_video_sampler_unet_49
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.920778
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MiniMax_H3_Ref2VA_参考视频_动作迁移_2093701124254683138.json, 平台全量/Minimax H3 参考生视频 + 4步加速   T8大佬版工作流_2093728964891209729.json, 平台全量/Minimax-H3开源 参考图生视频 创意视频 短剧漫剧_2119373577618284545.json, 平台全量/Minimax-H3开源 参考图生视频 创意视频 短剧漫剧_2119383292913995778.json, 平台全量/Minimax-h3-T8转化版-4步极速-双时钟(80s极速出片)_2117396347371474946.json, 平台全量/Minimax_H3_参考生视频_+_4步加速_2117410195327512578.json, 平台全量/Minimax_H3_参考生视频_+_4步加速_2117485127935815681.json, 视频生成/图生视频/Minimax H3 参考生视频 + 4步加速_2093367813456089090.json, 视频生成/图生视频/minimaxH3原版4步配音版_2114914680555794433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/MiniMax_H3_Ref2VA_参考视频_动作迁移_2093701124254683138.json、平台全量/Minimax H3 参考生视频 + 4步加速   T8大佬版工作流_2093728964891209729.json、平台全量/Minimax-H3开源 参考图生视频 创意视频 短剧漫剧_2119373577618284545.json、平台全量/Minimax-H3开源 参考图生视频 创意视频 短剧漫剧_2119383292913995778.json、平台全量/Minimax-h3-T8转化版-4步极速-双时钟(80s极速出片)_2117396347371474946.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 8/9 个有
- `SolAttnMiniMax` —— 7/9 个有
- `ModelAttentionBackend` —— 6/9 个有
- `BasicScheduler` —— 5/9 个有
- `KSamplerSelect` —— 5/9 个有
- `LoadAudio` —— 5/9 个有
- `MiniMaxH3AVDecodeT8` —— 5/9 个有
- `MiniMaxH3AudioConditioningT8` —— 5/9 个有
- `MiniMaxH3BlockCacheT8` —— 4/9 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/9 个有
- `MiniMaxH3ReferenceToVideo` —— 4/9 个有
- `VAEDecode` —— 4/9 个有
- `VAEDecodeAudio` —— 4/9 个有
- `ExtendIntermediateSigmas` —— 3/9 个有
- `H3SigmaRefiner` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `MemoryCleaner` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `RHLLMChatNode` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
