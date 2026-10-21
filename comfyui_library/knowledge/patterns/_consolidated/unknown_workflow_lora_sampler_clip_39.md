---
name: unknown_workflow_lora_sampler_clip_39
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.752143
common_nodes: [Any Switch (rgthree), CLIPTextEncode, CR Prompt Text, CR SDXL Aspect Ratio, CR Text, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, ImpactInt, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: TextJoin, LoadImage, LoraLoader, MathExpression|pysssss, PreviewImage, RHHiddenNodes, SDXLEmptyLatentSizePicker+, SaveImage, ShowText|pysssss, SomethingToString, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy hiresFix, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/FLUX 动漫人物生成专属工作流  二次修复_2048748298902708226.json, 图片生成/文生图/FLUX 动漫场景文生图  二次修复  高清出图_2101998483673796610.json, 图片生成/文生图/FLUX 动漫场景文生图 - 二次修复 - 高清出图_2057801872647479298.json, 图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2057295305439272962.json, 图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2079911753055563778.json, 图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2101996326224486401.json, 图片生成/文生图/FLUX 动漫场景文生图专属工作流  二次修复_2048766649515384834.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/FLUX 动漫人物生成专属工作流  二次修复_2048748298902708226.json、图片生成/文生图/FLUX 动漫场景文生图  二次修复  高清出图_2101998483673796610.json、图片生成/文生图/FLUX 动漫场景文生图 - 二次修复 - 高清出图_2057801872647479298.json、图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2057295305439272962.json、图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2079911753055563778.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `ImpactInt`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoader`
- `MathExpression|pysssss`
- `PreviewImage`
- `RHHiddenNodes`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `ShowText|pysssss`
- `SomethingToString`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy hiresFix`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 1/7 个有
- `ControlNetLoader` —— 1/7 个有
- `OpenposePreprocessor` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 7 | 100% |
| 高度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.45 | 0.2 - 0.65 | 7 | 73% |
| LoRA 文本强度 | 0.45 | 0.2 - 0.65 | 7 | 73% |
| 采样步数 | 30 | 30 - 30 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 7 | 69% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 7 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，7 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.45，观测区间 0.2 - 0.65，7 个样本
- LoRA 文本强度 中位数 0.45，观测区间 0.2 - 0.65，7 个样本
- 采样步数 中位数 30，观测区间 30 - 30，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，7 个样本，取值集中（一致性 100%）
