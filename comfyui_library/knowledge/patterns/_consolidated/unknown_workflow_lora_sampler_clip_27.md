---
name: unknown_workflow_lora_sampler_clip_27
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.889857
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR Text Concatenate, Label (rgthree)]
members: [图片生成/文生图/1923645200881602562.json, 图片生成/文生图/1923655528982245378.json, 图片生成/文生图/1926928747302166529.json, 图片生成/文生图/1926971761274093569.json, 图片生成/文生图/1943614394796568578.json, 图片生成/文生图/1948667723191595009.json, 图片生成/文生图/1972618798815698945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1923645200881602562.json、图片生成/文生图/1923655528982245378.json、图片生成/文生图/1926928747302166529.json、图片生成/文生图/1926971761274093569.json、图片生成/文生图/1943614394796568578.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 4/7 个有
- `CR Text` —— 2/7 个有
- `CR Text Concatenate` —— 2/7 个有
- `PMRF` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `DetailDaemonSamplerNode` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `PatchModelAddDownscale` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 768 - 1920 | 7 | 64% |
| 高度 | 1504 | 1024 - 2048 | 7 | 73% |
| LoRA 模型强度 | 0.8 | 0.4 - 1 | 7 | 71% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 768 - 1920，7 个样本
- 高度 中位数 1504，观测区间 1024 - 2048，7 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.4 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、Label (rgthree)
