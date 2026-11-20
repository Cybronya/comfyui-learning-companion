---
name: unknown_workflow_lora_sampler_vae_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.833
common_nodes: [CRTAutoDLFlux2KleinCLIP, CRTAutoDLFlux2KleinModel, CRTAutoDLFlux2KleinVAE, Flux2KleinEditTextEncode_EditUtils, Flux2KleinKSamplerExperimental, LoadImage, LoraLoaderModelOnly, PrimitiveInt, PrimitiveStringMultiline, SaveImage, VAEDecode]
problems: []
missing: []
members: [平台全量/AI夫妻影楼写真照-Klein 9B 合成+精修+换装 工作流版_2097490668955455489.json, 平台全量/Klein9B结婚证件照·双人照合成中国红底登记照_2096538357206704129.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/AI夫妻影楼写真照-Klein 9B 合成+精修+换装 工作流版_2097490668955455489.json、平台全量/Klein9B结婚证件照·双人照合成中国红底登记照_2096538357206704129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CRTAutoDLFlux2KleinCLIP`
- `CRTAutoDLFlux2KleinModel`
- `CRTAutoDLFlux2KleinVAE`
- `Flux2KleinEditTextEncode_EditUtils`
- `Flux2KleinKSamplerExperimental`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | 0.5 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
