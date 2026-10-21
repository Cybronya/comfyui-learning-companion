---
name: unknown_workflow_video_sampler_unet_26
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3动漫画风加速低显存全功能工作流_2099295189230772226.json, 视频生成/图生视频/MINIMAX-H3双采加速工作流_2088231306944663554.json, 视频生成/图生视频/MINIMAX-H3打斗专用全自动工作流_2088969218996924417.json, 视频生成/图生视频/MINIMAX-H3打斗视频专用全自动工作流_支持首帧、多图参考_2088902457060585473.json, 视频生成/图生视频/MINIMAX-H3打斗视频专用全自动模版_2088215513892737026.json, 视频生成/图生视频/MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610.json, 视频生成/图生视频/MINIMAX-H3热血战斗单图全自动工作流_2089691196661780481.json, 视频生成/图生视频/MINIMAXH3多图参考打斗全自动工作流_2100407909011247105.json, 视频生成/图生视频/MINIMAXH3多图参考打斗全自动工作流_2100495340662251521.json, 视频生成/文生视频/MINIMAX-H3全自动工作流_2089314933895942146.json, 视频生成/文生视频/MINIMAXH3多图参考打斗全自动工作流_2099696081260081154.json, 视频生成/文生视频/【Work-Fisher】MINIMAX-H3打斗专用全自动工作流_2087897093984837634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_26

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3动漫画风加速低显存全功能工作流_2099295189230772226.json、视频生成/图生视频/MINIMAX-H3双采加速工作流_2088231306944663554.json、视频生成/图生视频/MINIMAX-H3打斗专用全自动工作流_2088969218996924417.json、视频生成/图生视频/MINIMAX-H3打斗视频专用全自动工作流_支持首帧、多图参考_2088902457060585473.json、视频生成/图生视频/MINIMAX-H3打斗视频专用全自动模版_2088215513892737026.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 11/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 11/12 个有
- `PT_H3ConcatAVLatent` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `VAEEncode` —— 11/12 个有
- `Fast Groups Bypasser (rgthree)` —— 10/12 个有
- `PreviewAny` —— 10/12 个有
- `LoadAudio` —— 9/12 个有
- `RH_LLMAPI_Pro_Node` —— 9/12 个有
- `JjkText` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `CR Prompt Text` —— 1/12 个有
- `H3SigmaRefiner` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有
- `MemoryCleaner` —— 1/12 个有
- `Text` —— 1/12 个有
- `easy saveText` —— 1/12 个有
- `llama_cpp_instruct_adv` —— 1/12 个有
- `llama_cpp_model_loader` —— 1/12 个有
- `llama_cpp_parameters` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
