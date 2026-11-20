---
name: unknown_workflow_sampler_unet_vae_379
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7715
common_nodes: [Any Switch (rgthree), CLIPLoader, EmptyLatentImage, JsonExtractString, KSampler, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082.json, 平台全量/QwenImage2.1东方神话 T2I_2118695548684431362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_379

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/QwenImage2.1-T2I_+_官方提示词助手_2117194308204974082.json、平台全量/QwenImage2.1东方神话 T2I_2118695548684431362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `EmptyLatentImage`
- `JsonExtractString`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowAnything|Mie` —— 1/2 个有
- `TextConcatenator` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1324 | - | 2 | 82% |
| 高度 | 1500 | - | 2 | 72% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1324，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 高度 中位数 1500，样本不足，未给区间，2 个样本
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
