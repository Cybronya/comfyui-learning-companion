---
name: unknown_workflow_video_sampler_unet_32
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.829273
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3单独放大工作流_2086693326912311298.json, 视频生成/图生视频/H3极速高清文生视频_2089189623070281729.json, 视频生成/图生视频/MINIMAX H3 风扇三段变装展示-双采加速流_2107201355315240961.json, 视频生成/图生视频/MINIMAX-H3双采加速工作流_2088231306944663554.json, 视频生成/图生视频/MINIMAX-H3打斗专用全自动工作流_2088969218996924417.json, 视频生成/图生视频/MINIMAX-H3打斗视频专用全自动工作流_支持首帧、多图参考_2088902457060585473.json, 视频生成/图生视频/MINIMAX-H3打斗视频专用全自动模版_2088215513892737026.json, 视频生成/图生视频/MINIMAX-H3热血战斗Qwen3.8 提示词增强单图全自动工作流_2089736069146308610.json, 视频生成/图生视频/MINIMAX-H3热血战斗单图全自动工作流_2089691196661780481.json, 视频生成/图生视频/MINIMAXH3多图参考打斗全自动工作流_2100407909011247105.json, 视频生成/图生视频/MINIMAXH3多图参考打斗全自动工作流_2100495340662251521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/H3单独放大工作流_2086693326912311298.json、视频生成/图生视频/H3极速高清文生视频_2089189623070281729.json、视频生成/图生视频/MINIMAX H3 风扇三段变装展示-双采加速流_2107201355315240961.json、视频生成/图生视频/MINIMAX-H3双采加速工作流_2088231306944663554.json、视频生成/图生视频/MINIMAX-H3打斗专用全自动工作流_2088969218996924417.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 10/11 个有
- `LoraLoaderBypassModelOnly` —— 10/11 个有
- `MiniMaxH3AudioConditioningT8` —— 10/11 个有
- `MiniMaxH3DualClockSamplerT8` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `LoadImage` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `PreviewAny` —— 7/11 个有
- `RH_LLMAPI_Pro_Node` —— 6/11 个有
- `LoadAudio` —— 5/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `CLIPTextEncode` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `MemoryCleaner` —— 1/11 个有
- `Text` —— 1/11 个有
- `VAEEncodeAudio` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `easy saveText` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有
- `llama_cpp_parameters` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
