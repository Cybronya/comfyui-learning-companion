---
name: unknown_workflow_lora_sampler_clip_175
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.84
common_nodes: [BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/Bernini + Klein放大 文生图_2064670777449996290.json, 图片生成/文生图/Bernini文生图_2064181963208093697.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Bernini + Klein放大 文生图_2064670777449996290.json、图片生成/文生图/Bernini文生图_2064181963208093697.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `Text` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 27 | - | 2 | 15% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | sa_solver | - | 2 | 50% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 27，样本不足，未给区间，2 个样本，取值分散，一致性仅 15%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，2 个样本，一致性 50%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
