---
name: unknown_workflow_sampler_unet_vae_42
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.844733
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json, 视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json, 视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json, 视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json, 视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2100287204726755329.json, 视频生成/图生视频/FastVideo FastH3：图生视频_2107413322575470593.json, 视频生成/图生视频/FastVideo-FastH3-8-Step-V2 图生视频_2101581826061062145.json, 视频生成/图生视频/H3-图生视频-首尾帧_2087831020287643649.json, 视频生成/图生视频/MiniMax+H3+图生视频+加速版工作流_2087098569571524609.json, 视频生成/图生视频/MiniMax+H3图生视频（首帧视频、尾帧视频、首尾帧视频）_2084465463463075842.json, 视频生成/图生视频/MiniMaxH3加速版工作流图生视频ENGENG_2087088986627067905.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2087076628211003394.json, 视频生成/文生视频/1-MiniMaxh-H3-文生视频工作流-V2_2084639097741725698.json, 视频生成/文生视频/Fasth3图生视频_2100129417984036866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_42

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2-MiniMax-H3-单图-首尾帧生视频工作流V2_2084639140699795458.json、视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json、视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json、视频生成/图生视频/38.MiniMax H3 图生视频_2085360243923570689.json、视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `GetImageSize` —— 11/15 个有
- `ImageScaleToTotalPixels` —— 11/15 个有
- `ResolutionSelector` —— 10/15 个有
- `MiniMaxH3SigmaShift` —— 9/15 个有
- `LoraLoaderModelOnly` —— 7/15 个有
- `ModelAttentionBackend` —— 6/15 个有
- `BlockSparseAttention` —— 4/15 个有
- `Fast Groups Bypasser (rgthree)` —— 3/15 个有
- `PathchSageAttentionKJ` —— 3/15 个有
- `ResizeImageMaskNode` —— 3/15 个有
- `MiniMaxH3ContextIR` —— 2/15 个有
- `PrimitiveInt` —— 2/15 个有
- `ImpactConditionalBranch` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `PrimitiveStringMultiline` —— 1/15 个有
- `ShowText|pysssss` —— 1/15 个有
- `Text` —— 1/15 个有
- `easy boolean` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
