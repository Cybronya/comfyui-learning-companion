---
name: unknown_workflow_lora_sampler_unet_21
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.890714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json, 视频生成/图生视频/h3  4步多图自用_2088590941430046722.json, 视频生成/图生视频/加速升级版！ MiniMax-H3 图生视频！_2088799409717997570.json, 视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json, 视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json, 视频生成/图生视频/速度逆天！Minimax多图全能参考T8双采样8步加速版_2085471982044401665.json, 视频生成/文生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json、视频生成/图生视频/h3  4步多图自用_2088590941430046722.json、视频生成/图生视频/加速升级版！ MiniMax-H3 图生视频！_2088799409717997570.json、视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json、视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `DF_String_Concatenate` —— 2/7 个有
- `DF_Text_Box` —— 2/7 个有
- `JWStringGetLine` —— 2/7 个有
- `JjkConcat` —— 2/7 个有
- `JjkShowText` —— 2/7 个有
- `ReplaceString` —— 2/7 个有
- `StringConstant` —— 2/7 个有
- `AnyBooleanSwitch` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `SpectrumSDXL` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
