---
name: unknown_workflow_lora_sampler_clip_265
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8755
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResize+, Int, KSamplerAdvanced, KuwaharaBlur, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, RH_Translator, SaveImage, SimpleMathSlider+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/Z-image策划方案生成器_1999774255132835841.json, 图片生成/图生图/策划方案批量构图_2032699284566577154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_265

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image策划方案生成器_1999774255132835841.json、图片生成/图生图/策划方案批量构图_2032699284566577154.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResize+`
- `Int`
- `KSamplerAdvanced`
- `KuwaharaBlur`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `RH_Translator`
- `SaveImage`
- `SimpleMathSlider+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `ImageBatchMultiple+` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | sgm_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
