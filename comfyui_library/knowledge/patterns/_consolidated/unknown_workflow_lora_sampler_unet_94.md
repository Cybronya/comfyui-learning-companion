---
name: unknown_workflow_lora_sampler_unet_94
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.916889
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SDXLEmptyLatentSizePicker+, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/游戏图标icon_1953439745546309634.json, 图片生成/文生图/游戏图标icon一键生成_1937517741597179906.json, 图片生成/文生图/蒜-对比2个大模型出图效果_1996919135156256770.json, 平台全量/F.1美女摄影超写实FLUX_1834866126617559042.json, 平台全量/FLUX模型-超写实逼真黑悟空_1826285247011926018.json, 平台全量/Flux Disney Lora_1833161465435217921.json, 平台全量/Flux_ Anime LoRA工作流_1848298311592841217.json, 平台全量/Flux_Art LoRA工作流_1823672555348889601.json, 平台全量/同款迪士尼风格（Flux_ Disney LoRA）_1823673433468375041.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_94

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/游戏图标icon_1953439745546309634.json、图片生成/文生图/游戏图标icon一键生成_1937517741597179906.json、图片生成/文生图/蒜-对比2个大模型出图效果_1996919135156256770.json、平台全量/F.1美女摄影超写实FLUX_1834866126617559042.json、平台全量/FLUX模型-超写实逼真黑悟空_1826285247011926018.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SDXLEmptyLatentSizePicker+`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 8/9 个有
- `CLIPTextEncode` —— 7/9 个有
- `CLIPTextEncodeFlux` —— 2/9 个有
- `DisplayText` —— 2/9 个有
- `TextConcat` —— 2/9 个有
- `Textbox` —— 2/9 个有
- `FluxGuidance` —— 1/9 个有
- `ModelSamplingFlux` —— 1/9 个有
- `ttN imageREMBG` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.6 - 1.2 | 9 | 85% |
| LoRA 文本强度 | 1 | 0.6 - 1 | 9 | 87% |
| 宽度 | 832x1152 (0.72) | - | 9 | 56% |
| 高度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.6 - 1.2，9 个样本，取值集中（一致性 85%）
- LoRA 文本强度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 87%）
- 宽度 最常用 832x1152 (0.72)，9 个样本，一致性 56%
- 高度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
