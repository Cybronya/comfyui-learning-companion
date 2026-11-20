---
name: unknown_workflow_lora_sampler_clip_311
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8615
common_nodes: [CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Int, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/文生图/anima双采样工作流_2063507441417019394.json, 图片生成/文生图/z-image真实人像（带反推和扩写）_2064352102926868481.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_311

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/anima双采样工作流_2063507441417019394.json、图片生成/文生图/z-image真实人像（带反推和扩写）_2064352102926868481.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CLIPLoaderGGUF` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ComfyMathExpression` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 16 | - | 2 | 75% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |
| 宽度 | 992 | - | 2 | 97% |
| 高度 | 1488 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 16，样本不足，未给区间，2 个样本
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 宽度 中位数 992，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1488，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
