---
name: unknown_workflow_video_lora_sampler_562
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.441
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH38高动态加速流_2091799612456783873.json, 视频生成/图生视频/MiniMax_H3-单采_2106176867115036673.json, 视频生成/图生视频/MiniMax多图参考生成视频R2V_768_8步_2099766777768136705.json, 视频生成/图生视频/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2093245007657521154.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_562

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH38高动态加速流_2091799612456783873.json、视频生成/图生视频/MiniMax_H3-单采_2106176867115036673.json、视频生成/图生视频/MiniMax多图参考生成视频R2V_768_8步_2099766777768136705.json、视频生成/图生视频/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2093245007657521154.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `ExtendIntermediateSigmas` —— 2/4 个有
- `Text` —— 2/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `Float` —— 1/4 个有
- `FloatConstant` —— 1/4 个有
- `H3SigmaRefiner` —— 1/4 个有
- `Int` —— 1/4 个有
- `MiniMaxH3SigmaShift` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
