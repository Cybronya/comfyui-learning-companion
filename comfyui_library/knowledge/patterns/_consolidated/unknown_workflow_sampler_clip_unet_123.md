---
name: unknown_workflow_sampler_clip_unet_123
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8702
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR SDXL Aspect Ratio, SDXLEmptyLatentSizePicker+]
members: [图片生成/文生图/1916390487366762498.json, 图片生成/文生图/1917071528809136129.json, 图片生成/文生图/1935657646269595649.json, 图片生成/文生图/1948791649602871297.json, 图片生成/文生图/1974142043784130562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_123

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1916390487366762498.json、图片生成/文生图/1917071528809136129.json、图片生成/文生图/1935657646269595649.json、图片生成/文生图/1948791649602871297.json、图片生成/文生图/1974142043784130562.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `FluxGuidance` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Flex2Conditioner` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `TeaCache` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `DifferentialDiffusion` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SDXLEmptyLatentSizePicker+` —— 1/5 个有
- `SUPIR_Upscale` —— 1/5 个有
- `Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768x1280 (0.6) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio、SDXLEmptyLatentSizePicker+
