---
name: unknown_workflow_lora_sampler_unet_48
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.884545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/LH-手办视频_2114202006498922497.json, 图片生成/图生图/LH-手办视频_2114212303322304514.json, 图片生成/图生图/SBAPI_MinimaxH3三分镜参考生成视频工作流_2114262243859845121.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086148083527798786.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086156036376977410.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085215256233725953.json, 视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1_2085648828052631554.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085258096615710722.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085265592797450241.json, 视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json, 视频生成/文生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/LH-手办视频_2114202006498922497.json、图片生成/图生图/LH-手办视频_2114212303322304514.json、图片生成/图生图/SBAPI_MinimaxH3三分镜参考生成视频工作流_2114262243859845121.json、视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086148083527798786.json、视频生成/图生视频/(8步加速-768P)Minimax参考生视频V1(第四版加速模型)_2086156036376977410.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
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
- `PrimitiveStringMultiline` —— 9/11 个有
- `PathchSageAttentionKJ` —— 8/11 个有
- `CR Prompt Text` —— 6/11 个有
- `DF_String_Concatenate` —— 3/11 个有
- `DF_Text_Box` —— 3/11 个有
- `JWStringGetLine` —— 3/11 个有
- `JjkConcat` —— 3/11 个有
- `JjkShowText` —— 3/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `ReplaceString` —— 3/11 个有
- `StringConstant` —— 3/11 个有
- `CR Text` —— 2/11 个有
- `VHS_VideoCombine` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
