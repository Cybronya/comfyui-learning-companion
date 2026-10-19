---
name: unknown_workflow_video_lora_sampler_462
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.69775
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, DF_Integer, EmptyHunyuanLatentVideo, INTConstant, KSamplerAdvanced, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RH_Prompter, RH_Translator, ShowText|pysssss, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy ifElse]
problems: []
missing: [CR Text, CR Text Concatenate, MathExpression|pysssss, SimpleMath+, Text Multiline]
members: [图片生成/文生图/1957131741351829505.json, 图片生成/文生图/1960634788682096642.json, 视频生成/文生视频/1950000551498006530.json, 视频生成/文生视频/1957131741351829505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_462

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1957131741351829505.json、图片生成/文生图/1960634788682096642.json、视频生成/文生视频/1950000551498006530.json、视频生成/文生视频/1957131741351829505.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `DF_Integer`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RH_Prompter`
- `RH_Translator`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `ShellAgentPluginInputText` —— 2/4 个有
- `ShellAgentPluginSaveVideoVHS` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、MathExpression|pysssss、SimpleMath+、Text Multiline
