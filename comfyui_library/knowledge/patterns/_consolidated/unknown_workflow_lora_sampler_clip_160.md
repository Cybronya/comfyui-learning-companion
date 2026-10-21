---
name: unknown_workflow_lora_sampler_clip_160
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.706
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, CR Seed, CR Text, ColorCorrectOfUtils, EmptyLatentImage, FluxResolutionNode, ImageCASharpening+, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, RHHiddenNodes, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: [CR Text, CR Text Concatenate, ImageCASharpening+, MathExpression|pysssss, easy cleanGpuUsed, CR Seed]
members: [图片生成/文生图/1952858079282065409.json, 图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1952858079282065409.json、图片生成/文生图/【wan2.2文生图V2】gemini3专业级人像摄影提示词_1991427455816790017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `CR Text`
- `ColorCorrectOfUtils`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `ImageCASharpening+`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `RHHiddenNodes`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 676 | - | 2 | 76% |
| 高度 | 864 | - | 2 | 59% |
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 16 | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | bong_tangent | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 676，样本不足，未给区间，2 个样本
- 高度 中位数 864，样本不足，未给区间，2 个样本
- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 16，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 bong_tangent，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 16，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、ImageCASharpening+、MathExpression|pysssss、easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
