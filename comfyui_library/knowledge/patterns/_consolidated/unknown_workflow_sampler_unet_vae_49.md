---
name: unknown_workflow_sampler_unet_vae_49
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.986909
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1964223507485872129.json, 图片生成/文生图/1965805471892443137.json, 图片生成/文生图/1971036023260123138.json, 图片生成/文生图/1976073946242093057.json, 图片生成/文生图/1980191535377584130.json, 图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json, 图片生成/文生图/flux双lora批量出图_1900015521121579010.json, 图片生成/文生图/flux文生图_1896040375998414850.json, 图片生成/文生图/flux文生图_1896043053692092417.json, 图片生成/文生图/flux文生图基础工作流+双lora_1887374428500549633.json, 图片生成/文生图/flux文生图标准版_在线生图_1892886267414392834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_49

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1964223507485872129.json、图片生成/文生图/1965805471892443137.json、图片生成/文生图/1971036023260123138.json、图片生成/文生图/1976073946242093057.json、图片生成/文生图/1980191535377584130.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 8/11 个有
- `LoraLoader` —— 5/11 个有
- `CLIPTextEncodeFlux` —— 3/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `RH_Translator` —— 2/11 个有
- `ArgosTranslateTextNode` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `Text` —— 1/11 个有
- `TextInput_` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 400 - 1536 | 11 | 70% |
| 高度 | 1280 | 400 - 1920 | 11 | 62% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 5 | 89% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 400 - 1536，11 个样本
- 高度 中位数 1280，观测区间 400 - 1920，11 个样本
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，5 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
