---
name: unknown_workflow_sampler_unet_vae_300
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6325
common_nodes: [BasicGuider, CLIPLoader, ComfySwitchNode, JsonExtractString, KSamplerSelect, ManualSigmas, MiniMaxH3ImageConditioning, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, TextGenerateV2, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMax H3-Image｜中文海报烧字_2120393071899799553.json, 平台全量/Minimax H3 Image精准Sigma图像编辑_2120254692004556802.json, 平台全量/Minimax-H3 Image 文生图 Sigma精准调度&自动提示词_2120391350930731009.json, 平台全量/minimaxh3 文生图_2120496330027130881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_300

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/MiniMax H3-Image｜中文海报烧字_2120393071899799553.json、平台全量/Minimax H3 Image精准Sigma图像编辑_2120254692004556802.json、平台全量/Minimax-H3 Image 文生图 Sigma精准调度&自动提示词_2120391350930731009.json、平台全量/minimaxh3 文生图_2120496330027130881.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfySwitchNode`
- `JsonExtractString`
- `KSamplerSelect`
- `ManualSigmas`
- `MiniMaxH3ImageConditioning`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `TextGenerateV2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 3/4 个有
- `LoadImage` —— 2/4 个有
- `BasicScheduler` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ResizeImageMaskNode` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
