---
name: unknown_workflow_sampler_unet_vae_155
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9066
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/海螺H3八步极速生成文图首尾帧视频3合一工作流_2088515866974576641.json, 视频生成/图生视频/海螺图生视频_2085524828332843010.json, 视频生成/文生视频/10ErosMax test4 对比测试_2087783168324759554.json, 视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json, 视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_155

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/海螺H3八步极速生成文图首尾帧视频3合一工作流_2088515866974576641.json、视频生成/图生视频/海螺图生视频_2085524828332843010.json、视频生成/文生视频/10ErosMax test4 对比测试_2087783168324759554.json、视频生成/文生视频/Wan2.2_H3_Motion_LoRA对比测试_2087900011068739586.json、视频生成/文生视频/海螺H3首尾帧生视频_2087721274360553473.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
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
- `LoraLoaderModelOnly` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `GetImageSize` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `AnyBooleanSwitch` —— 1/5 个有
- `BOOLConstant` —— 1/5 个有
- `CM_BoolBinaryOperation` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImpactConditionalBranch` —— 1/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `Switch image [Crystools]` —— 1/5 个有
- `easy float` —— 1/5 个有
- `easy imageIndexSwitch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
