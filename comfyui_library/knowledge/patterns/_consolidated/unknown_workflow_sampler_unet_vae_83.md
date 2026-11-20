---
name: unknown_workflow_sampler_unet_vae_83
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.870231
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/minimaxh3全参官方指南自动扩展提示词T7_2085624158054084610.json, 平台全量/minimaxh3全参官方指南自动扩展提示词T7_2104842876663455745.json, 数字人/数字人/图生视频教学工作流_2091871574247952386.json, 数字人/数字人/首尾帧逻辑_2087967441874931713.json, 视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json, 视频生成/图生视频/360度旋转_minimax_h3_2109928610961387522.json, 视频生成/图生视频/A-4 MiniMax H3 图生视频 _ 首尾帧控制 _ 原生音频 _ 两张图变一段电影_2084559447325757441.json, 视频生成/图生视频/MINIMAX-H3图生视频工作流_2102372635475791873.json, 视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2084154545424388098.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2087935494813478914.json, 视频生成/图生视频/MinimaxH3图生视频8步工作流_2099783471219699713.json, 视频生成/图生视频/minimaxH3多参提示词优化_2086425483746566146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_83

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/minimaxh3全参官方指南自动扩展提示词T7_2085624158054084610.json、平台全量/minimaxh3全参官方指南自动扩展提示词T7_2104842876663455745.json、数字人/数字人/图生视频教学工作流_2091871574247952386.json、数字人/数字人/首尾帧逻辑_2087967441874931713.json、视频生成/图生视频/360度旋转_minimax_h3_2109107290178678786.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 12/13 个有
- `CreateVideo` —— 11/13 个有
- `ResolutionSelector` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `MiniMaxH3ImageToVideo` —— 10/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/13 个有
- `SolAttnPatch` —— 5/13 个有
- `Text` —— 5/13 个有
- `easy showAnything` —— 4/13 个有
- `ImageConcatenateMulti_UTK` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `RHHiddenNodes` —— 3/13 个有
- `VHS_VideoCombine` —— 3/13 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 3/13 个有
- `MiniMaxH3SigmaShift` —— 2/13 个有
- `PrimitiveInt` —— 2/13 个有
- `CacheDiT_Model_Optimizer` —— 1/13 个有
- `Int` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
