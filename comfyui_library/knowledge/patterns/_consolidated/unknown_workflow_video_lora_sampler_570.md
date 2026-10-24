---
name: unknown_workflow_video_lora_sampler_570
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.830333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, DF_Integer, EmptyHunyuanLatentVideo, INTConstant, KSamplerAdvanced, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, RH_Prompter, RH_Translator, ShowText|pysssss, SimpleMath+, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy ifElse]
problems: []
missing: []
members: [图片生成/文生图/Living Comic Style-wan2.2 T2V (speed)+auto prompt_1957131741351829505.json, 图片生成/文生图/Wan2.2文生视频_自动提示词_1960634788682096642.json, 视频生成/文生视频/wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_570

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Living Comic Style-wan2.2 T2V (speed)+auto prompt_1957131741351829505.json、图片生成/文生图/Wan2.2文生视频_自动提示词_1960634788682096642.json、视频生成/文生视频/wan2.2 文生视频 (加速版)+ 提示词自动润色_1950000551498006530.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ShellAgentPluginInputText` —— 1/3 个有
- `ShellAgentPluginSaveVideoVHS` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
