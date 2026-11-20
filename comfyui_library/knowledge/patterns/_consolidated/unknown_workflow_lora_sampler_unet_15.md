---
name: unknown_workflow_lora_sampler_unet_15
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.83296
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/8步高质量极速Minimax H3开源版_2108184548386365441.json, 视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2099462450285473794.json, 视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2099464334022897666.json, 视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2100551150692032513.json, 视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2105262941045088257.json, 视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2105264487803740162.json, 视频生成/图生视频/Dasiwa HybirdturboV1混合版_2094425018229944321.json, 视频生成/图生视频/Dasiwa MinimaxH3参考图生视频_2092127662033686529.json, 视频生成/图生视频/Dasiwa MinimaxH3参考图生视频_2100150349800755202.json, 视频生成/图生视频/H3 音频驱动｜双采短片版_2098724093511159810.json, 视频生成/图生视频/H3_高动态双采放大_2102818737027117058.json, 视频生成/图生视频/H3_高动态双采放大_2106167971315011585.json, 视频生成/图生视频/H3双采多参加速格斗工作流-_2097995370008764418.json, 视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json, 视频生成/图生视频/MiniMax H3 电商带货-双采全能工作流_2107862335695183874.json, 视频生成/图生视频/MiniMax H3-动态最强-参考生视频-V1_2094782408347447298.json, 视频生成/图生视频/MiniMax H3双采全能工作流V2-文戏不油，武戏动态强-电商带货-参考生视频_2102717112467943425.json, 视频生成/图生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-参考生视频_2098795077903671298.json, 视频生成/图生视频/MiniMax H3双采全能工作流V2-音频驱动数字人-电商带货-二采_2102718883990958081.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3-语义桥-文戏不油，武戏动态强-参考生视频_2105138065181339649.json, 视频生成/图生视频/MiniMax H3多参双采参考长视频--Pov第一视角_2104777353225396225.json, 视频生成/图生视频/双采双采_2114061579145797634.json, 视频生成/文生视频/(长视频优化版)H3_2106677452302016514.json, 视频生成/文生视频/0928(30秒长视频-文武双修均衡版-高清)视频_2104358294361038849.json, 视频生成/文生视频/MiniMax H3--Dasiwa v双采生视频_2106929502843658241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/8步高质量极速Minimax H3开源版_2108184548386365441.json、视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2099462450285473794.json、视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2099464334022897666.json、视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2100551150692032513.json、视频生成/图生视频/8步高质量极速Minimax海螺h3图生视频加速优化版t8_2105262941045088257.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 24/25 个有
- `VHS_VideoCombine` —— 23/25 个有
- `CR Prompt Text` —— 22/25 个有
- `ModelAttentionBackend` —— 20/25 个有
- `SolAttnMiniMax` —— 19/25 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 17/25 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 17/25 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 17/25 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 17/25 个有
- `LoraLoaderModelOnly` —— 14/25 个有
- `Float` —— 12/25 个有
- `CreateVideo` —— 7/25 个有
- `SaveVideo` —— 7/25 个有
- `GetNode` —— 6/25 个有
- `LoadAudio` —— 6/25 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 6/25 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 6/25 个有
- `SetNode` —— 6/25 个有
- `easy anythingIndexSwitch` —— 6/25 个有
- `Astra` —— 5/25 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 5/25 个有
- `RunningHub Deepcleaner` —— 5/25 个有
- `easy cleanGpuUsed` —— 5/25 个有
- `孤海注释` —— 5/25 个有
- `Fast Groups Bypasser (rgthree)` —— 4/25 个有
- `PrimitiveStringMultiline` —— 3/25 个有
- `DuckHideNode` —— 2/25 个有
- `SaveImage` —— 2/25 个有
- `ConcatTextOfUtils` —— 1/25 个有
- `EmptyImage` —— 1/25 个有
- `PreviewImage` —— 1/25 个有
- `easy int` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
