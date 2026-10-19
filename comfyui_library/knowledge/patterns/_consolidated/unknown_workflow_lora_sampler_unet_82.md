---
name: unknown_workflow_lora_sampler_unet_82
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.752
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, INTConstant, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MultiTextConcatenate, PrimitiveFloat, RH_LLMAPI_Pro_Node, RH_Utils, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, ShowAnything|Mie, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy saveText, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 REF2VA-全能参考自动提示词生视频-(8步加速-768P)_2085919158885244930.json, 视频生成/图生视频/MiniMax-H3 心灵鸡汤口播数字人全流程方案落地-V1版_2089080328391581697.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_82

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 REF2VA-全能参考自动提示词生视频-(8步加速-768P)_2085919158885244930.json、视频生成/图生视频/MiniMax-H3 心灵鸡汤口播数字人全流程方案落地-V1版_2089080328391581697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `INTConstant`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MultiTextConcatenate`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RH_Utils`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowAnything|Mie`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy saveText`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BBS_AnyResolutionZip` —— 1/2 个有
- `Banana2Batch` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MmuuaiGroupBypass` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `WanMoveTracksFromCoords` —— 1/2 个有
- `easy int` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
