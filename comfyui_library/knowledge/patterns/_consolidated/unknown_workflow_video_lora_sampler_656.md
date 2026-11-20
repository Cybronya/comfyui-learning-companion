---
name: unknown_workflow_video_lora_sampler_656
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.452
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ResolutionSelector, SelfLiftH3Sampler, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/AI代码侠土豆-人物替换 影视_短视频 二创_2119717876713218050.json, 平台全量/MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json, 视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_656

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/AI代码侠土豆-人物替换 影视_短视频 二创_2119717876713218050.json、平台全量/MiniMax H3海螺开源版h3-SelfLift影视级人物情绪表达skill提示词自动化工作流_2120105295019077634.json、视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2104111411025764354.json、视频生成/图生视频/AITUDOU-MiniMax+H3+SelfLift+影视级情绪表达+SKILL_2106320510052298754.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `Float` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `Text` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `ModelPreviewOverrideKJ` —— 1/4 个有
- `VHS_LoadVideoFFmpeg` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
