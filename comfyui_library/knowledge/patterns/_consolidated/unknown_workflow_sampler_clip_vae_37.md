---
name: unknown_workflow_sampler_clip_vae_37
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.81
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [easy positive, CR SDXL Aspect Ratio, CR Text, CR Text Concatenate, Evaluate Strings]
members: [图片生成/文生图/1967803688263778306.json, 图片生成/文生图/1968509624422944769.json, 图片生成/文生图/1970701866311053313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_37

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1967803688263778306.json、图片生成/文生图/1968509624422944769.json、图片生成/文生图/1970701866311053313.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `Text` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `Evaluate Strings` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `easy positive` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy positive、CR SDXL Aspect Ratio、CR Text、CR Text Concatenate、Evaluate Strings
