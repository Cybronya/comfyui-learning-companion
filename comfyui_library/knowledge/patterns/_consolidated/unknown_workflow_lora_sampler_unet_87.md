---
name: unknown_workflow_lora_sampler_unet_87
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.867875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json, 视频生成/图生视频/miniMAXH3全能参考_2084803672076279809.json, 视频生成/图生视频/minimax_h3_lightx2v正式版 参考模式_2085761824204607490.json, 视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json, 视频生成/图生视频/速度逆天！Minimax多图全能参考T8双采样8步加速版_2085471982044401665.json, 视频生成/文生视频/8步加速Mini Max H3图生视频_2084136196300697601.json, 视频生成/文生视频/MinimaxH3参考8步生成视频工作流_2087040392687611906.json, 视频生成/文生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_87

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json、视频生成/图生视频/miniMAXH3全能参考_2084803672076279809.json、视频生成/图生视频/minimax_h3_lightx2v正式版 参考模式_2085761824204607490.json、视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json、视频生成/图生视频/速度逆天！Minimax多图全能参考T8双采样8步加速版_2085471982044401665.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `DF_String_Concatenate` —— 2/8 个有
- `DF_Text_Box` —— 2/8 个有
- `JWStringGetLine` —— 2/8 个有
- `JjkConcat` —— 2/8 个有
- `JjkShowText` —— 2/8 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/8 个有
- `ReplaceString` —— 2/8 个有
- `StringConstant` —— 2/8 个有
- `PrimitiveInt` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
