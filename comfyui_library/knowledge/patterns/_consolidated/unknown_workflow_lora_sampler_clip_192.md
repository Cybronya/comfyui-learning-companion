---
name: unknown_workflow_lora_sampler_clip_192
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.912667
common_nodes: [CLIPTextEncode, CR SDXL Aspect Ratio, DualCLIPLoader, FluxGuidance, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kontext Dev文生图-创意灯泡微缩场景_1948791649602871297.json, 图片生成/文生图/Kontext 文生图 加速版_1974142043784130562.json, 图片生成/文生图/flux基础工作流-古琴_1935657646269595649.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Kontext Dev文生图-创意灯泡微缩场景_1948791649602871297.json、图片生成/文生图/Kontext 文生图 加速版_1974142043784130562.json、图片生成/文生图/flux基础工作流-古琴_1935657646269595649.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `TeaCache` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SUPIR_Upscale` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
