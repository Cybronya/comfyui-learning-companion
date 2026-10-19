---
name: unknown_workflow_video_lora_sampler_621
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.635333
common_nodes: [BasicScheduler, CLIPLoader, GetNode, JjkText, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_h3_去油&光影保持（自用）_2102671994377560065.json, 视频生成/图生视频/poster animation_2094321304538279938.json, 视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_621

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Minimax_h3_去油&光影保持（自用）_2102671994377560065.json、视频生成/图生视频/poster animation_2094321304538279938.json、视频生成/图生视频/动态壁纸生成-Minimax_h3_2095801933113155586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `MiniMaxH3SigmaShift` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `H3SigmaRefiner` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/3 个有
- `QwenH3PromptLocal` —— 1/3 个有
- `T8LLMProviderConfig` —— 1/3 个有
- `Text` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
