---
name: unknown_workflow_sampler_unet_vae_57
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.796067
common_nodes: [BasicGuider, CLIPLoader, KSamplerSelect, ManualSigmas, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138.json, 平台全量/MiniMAx H3 Image—文生图_2120426127511613441.json, 平台全量/MiniMax H3 文生图｜极速版_2119390141839134722.json, 平台全量/Minimax H3 Image精准Sigma文生图_2120254734056640513.json, 平台全量/Minimax H3 Image精准Sigma文生图_2120317051934953473.json, 平台全量/Minimax H3 Image精准Sigma文生图_2120446329645264897.json, 平台全量/Minimax H3 Image精准Sigma文生图_2120464176735940609.json, 平台全量/Minimax H3 Image精准Sigma文生图_2120514497784930306.json, 平台全量/MinimaxH3文生图_2120464627199995905.json, 平台全量/P-H3-Image-文生图-Lora-提示词增强_2119976761634148354.json, 平台全量/P-H3-Image图像生成_2119644535872647169.json, 平台全量/P-H3-image-文生图_2118248303166054402.json, 平台全量/P-H3-image-文生图_2118844649732403201.json, 平台全量/P-H3-image-文生图_2119011776565170178.json, 平台全量/P-H3-image-文生图_2119048659806543873.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_57

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/AI图像创作丨minimax_h3_fl2va_pruned_int8_convrot丨文生图_2119626388444635138.json、平台全量/MiniMAx H3 Image—文生图_2120426127511613441.json、平台全量/MiniMax H3 文生图｜极速版_2119390141839134722.json、平台全量/Minimax H3 Image精准Sigma文生图_2120254734056640513.json、平台全量/Minimax H3 Image精准Sigma文生图_2120317051934953473.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `KSamplerSelect`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 8/15 个有
- `PH3ImageConditioning` —— 8/15 个有
- `LoraLoaderModelOnly` —— 7/15 个有
- `MiniMaxH3ImageConditioning` —— 7/15 个有
- `PreviewAny` —— 7/15 个有
- `ComfySwitchNode` —— 2/15 个有
- `LoraLoaderBypassModelOnly` —— 2/15 个有
- `PrimitiveBoolean` —— 2/15 个有
- `StringFormat` —— 2/15 个有
- `TextGenerate` —— 2/15 个有
- `BasicScheduler` —— 1/15 个有
- `PreviewImage` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
