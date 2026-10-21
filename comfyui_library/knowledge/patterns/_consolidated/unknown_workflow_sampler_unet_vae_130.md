---
name: unknown_workflow_sampler_unet_vae_130
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.944333
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1976073946242093057.json, 图片生成/文生图/1980191535377584130.json, 图片生成/文生图/1982707861027471361.json, 图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json, 图片生成/文生图/FLIX文生图｜产品写实 超逼真_1896248747091427329.json, 图片生成/文生图/flux双lora批量出图_1900015521121579010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_130

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1976073946242093057.json、图片生成/文生图/1980191535377584130.json、图片生成/文生图/1982707861027471361.json、图片生成/文生图/DP小熊猫 V1.0_1897934794485878785.json、图片生成/文生图/FLIX文生图｜产品写实 超逼真_1896248747091427329.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoraLoader` —— 4/6 个有
- `CLIPTextEncode` —— 3/6 个有
- `CLIPTextEncodeFlux` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `BatchPromptSchedule` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SeargePromptCombiner` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | 400 - 1080 | 6 | 72% |
| 高度 | 1152 | 400 - 1920 | 6 | 57% |
| LoRA 模型强度 | 0.9 | 0.65 - 1 | 4 | 83% |
| LoRA 文本强度 | 1 | 0.65 - 1 | 4 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，观测区间 400 - 1080，6 个样本
- 高度 中位数 1152，观测区间 400 - 1920，6 个样本
- LoRA 模型强度 中位数 0.9，观测区间 0.65 - 1，4 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 0.65 - 1，4 个样本，取值集中（一致性 83%）
