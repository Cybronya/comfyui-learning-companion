---
name: unknown_workflow_video_lora_sampler_110
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.891714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX多参官方加速工作流_2085378301211799553.json, 视频生成/图生视频/Minimax H3三图参考(无参考音)_2089300406496219138.json, 视频生成/图生视频/Minimax H3三图参考+2参考音_2089300447696871426.json, 视频生成/图生视频/Minimax H3三图参考+三参考音_2089302046485864449.json, 视频生成/图生视频/Minimax H3单图参考(无参考音)_2084264457093607425.json, 视频生成/图生视频/Minimax H3单图参考+1参考音_2089270431596507137.json, 视频生成/图生视频/Minimax H3双图参考(无参考音)_2089281585597210625.json, 视频生成/图生视频/Minimax H3双图参考+1参考音【口播用】_2090260648876920833.json, 视频生成/图生视频/Minimax H3双图参考+1参考音【批量管理系统api用】_2093664402544353282.json, 视频生成/图生视频/Minimax H3双图参考+2参考音_2089282022698213377.json, 视频生成/图生视频/minimax H3酷炫街舞_2085366057304412161.json, 视频生成/文生视频/MINIMAX-H3 文生_单图_首尾帧 工作流_2085269429079855106.json, 视频生成/文生视频/MiniMax H3最新音乐驱动多图参考MV生成工作流🐘承象_2087393176142303234.json, 视频生成/文生视频/MiniMaxH3+多合一稳定MAX｜4步8步加速（自用）_2092482860316971010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_110

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/MINIMAX多参官方加速工作流_2085378301211799553.json、视频生成/图生视频/Minimax H3三图参考(无参考音)_2089300406496219138.json、视频生成/图生视频/Minimax H3三图参考+2参考音_2089300447696871426.json、视频生成/图生视频/Minimax H3三图参考+三参考音_2089302046485864449.json、视频生成/图生视频/Minimax H3单图参考(无参考音)_2084264457093607425.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 13/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `MiniMaxH3ReferenceToVideo` —— 12/14 个有
- `MiniMaxH3SigmaShift` —— 12/14 个有
- `PrimitiveStringMultiline` —— 12/14 个有
- `INTConstant` —— 9/14 个有
- `LoadAudio` —— 8/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `MiniMaxH3ImageToVideo` —— 3/14 个有
- `Display Any (rgthree)` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `Audio Duration (mtb)` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `LazySwitchKJ` —— 1/14 个有
- `PrimitiveBoolean` —— 1/14 个有
- `SimpleCalculatorKJ` —— 1/14 个有
- `StringReplace` —— 1/14 个有
- `TextGenerate` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有
- `easy int` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
