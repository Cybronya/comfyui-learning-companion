---
name: unknown_workflow_sampler_unet_vae_270
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8598
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/小红书最火墙绘_1923735796107702274.json, 平台全量/小红书模特真实生活照_1925148629513007105.json, 平台全量/文生图写实风格（Flux_Realism LoRA）_1823665769094754305.json, 平台全量/电商端午粽子_1926551895463333890.json, 平台全量/绘本故事一键批量出图_1954383264234520577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_270

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/小红书最火墙绘_1923735796107702274.json、平台全量/小红书模特真实生活照_1925148629513007105.json、平台全量/文生图写实风格（Flux_Realism LoRA）_1823665769094754305.json、平台全量/电商端午粽子_1926551895463333890.json、平台全量/绘本故事一键批量出图_1954383264234520577.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 4/5 个有
- `EmptyLatentImage` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `Text Multiline` —— 2/5 个有
- `BatchPromptSchedule` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SDXLEmptyLatentSizePicker+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1280 | 4 | 90% |
| 高度 | 1024 | 1 - 1024 | 5 | 48% |
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 4 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1280，4 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 1 - 1024，5 个样本，取值分散，一致性仅 48%
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
