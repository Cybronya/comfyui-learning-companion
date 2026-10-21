---
name: unknown_workflow_sampler_clip_vae_25
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9846
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/F拉斯_2075877608994201601.json, 图片生成/文生图/flux文生图_1896040375998414850.json, 图片生成/文生图/flux文生图_1896043053692092417.json, 图片生成/文生图/flux文生图基础工作流+双lora_1887374428500549633.json, 图片生成/文生图/flux文生图标准版_在线生图_1892886267414392834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/F拉斯_2075877608994201601.json、图片生成/文生图/flux文生图_1896040375998414850.json、图片生成/文生图/flux文生图_1896043053692092417.json、图片生成/文生图/flux文生图基础工作流+双lora_1887374428500549633.json、图片生成/文生图/flux文生图标准版_在线生图_1892886267414392834.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `LoraLoader` —— 2/5 个有
- `ArgosTranslateTextNode` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `NunchakuTextEncoderLoader` —— 1/5 个有
- `PreviewAny` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 784 - 1536 | 5 | 76% |
| 高度 | 1024 | 1024 - 1536 | 5 | 81% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 784 - 1536，5 个样本
- 高度 中位数 1024，观测区间 1024 - 1536，5 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
