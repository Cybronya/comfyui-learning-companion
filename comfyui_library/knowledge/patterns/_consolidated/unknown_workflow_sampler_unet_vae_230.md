---
name: unknown_workflow_sampler_unet_vae_230
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.925667
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SBAPI_MinimaxH3三分镜参考生成视频工作流_2114262243859845121.json, 图片生成/图生图/SBAPI_MinimaxH3三分镜参考生成视频工作流_2115291432847233026.json, 图片生成/图生图/VividMuse_MiniMax_H3_多参生视频_2084280381586628609.json, 图片生成/图生图/pika_h3_flex_ref2va多参模式_2116689235410513921.json, 视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json, 视频生成/文生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_230

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/SBAPI_MinimaxH3三分镜参考生成视频工作流_2114262243859845121.json、图片生成/图生图/SBAPI_MinimaxH3三分镜参考生成视频工作流_2115291432847233026.json、图片生成/图生图/VividMuse_MiniMax_H3_多参生视频_2084280381586628609.json、图片生成/图生图/pika_h3_flex_ref2va多参模式_2116689235410513921.json、视频生成/图生视频/SBAPI_MinimaxH3三分镜参考生成视频工作流_2085316887281496066.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `BasicScheduler` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `DF_String_Concatenate` —— 4/6 个有
- `DF_Text_Box` —— 4/6 个有
- `JWStringGetLine` —— 4/6 个有
- `JjkConcat` —— 4/6 个有
- `JjkShowText` —— 4/6 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 4/6 个有
- `ReplaceString` —— 4/6 个有
- `StringConstant` —— 4/6 个有
- `ManualSigmas` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
