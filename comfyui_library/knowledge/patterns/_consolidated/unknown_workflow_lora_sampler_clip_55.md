---
name: unknown_workflow_lora_sampler_clip_55
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.750375
common_nodes: [Any Switch (rgthree), CLIPTextEncode, CR SDXL Aspect Ratio, CR Text, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, KSampler, LoadImage, LoraLoader, PreviewImage, RHHiddenNodes, SaveImage, ShowText|pysssss, StringFunction|pysssss, UNETLoader, VAEDecode, VAELoader, easy hiresFix, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/FLUX 动漫场景设计图上色 色块识别工作流  二次放大_2048804472687697922.json, 图片生成/文生图/FLUX 动漫人物生成专属工作流  二次修复_2048748298902708226.json, 图片生成/文生图/FLUX 动漫场景文生图  二次修复  高清出图_2101998483673796610.json, 图片生成/文生图/FLUX 动漫场景文生图 - 二次修复 - 高清出图_2057801872647479298.json, 图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2057295305439272962.json, 图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2079911753055563778.json, 图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2101996326224486401.json, 图片生成/文生图/FLUX 动漫场景文生图专属工作流  二次修复_2048766649515384834.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX 动漫场景设计图上色 色块识别工作流  二次放大_2048804472687697922.json、图片生成/文生图/FLUX 动漫人物生成专属工作流  二次修复_2048748298902708226.json、图片生成/文生图/FLUX 动漫场景文生图  二次修复  高清出图_2101998483673796610.json、图片生成/文生图/FLUX 动漫场景文生图 - 二次修复 - 高清出图_2057801872647479298.json、图片生成/文生图/FLUX 动漫场景文生图 _ 二次修复 _ 高清出图_2057295305439272962.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy hiresFix`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `ImpactInt` —— 7/8 个有
- `JanusImageUnderstanding` —— 7/8 个有
- `JanusModelLoader` —— 7/8 个有
- `LayerUtility: TextJoin` —— 7/8 个有
- `MathExpression|pysssss` —— 7/8 个有
- `SDXLEmptyLatentSizePicker+` —— 7/8 个有
- `SomethingToString` —— 7/8 个有
- `easy anythingIndexSwitch` —— 7/8 个有
- `ControlNetApplyAdvanced` —— 2/8 个有
- `ControlNetLoader` —— 2/8 个有
- `AIO_Preprocessor` —— 1/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `OpenposePreprocessor` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.95 | - | 2 | 95% |
| LoRA 模型强度 | 0.45 | 0.2 - 0.65 | 8 | 74% |
| LoRA 文本强度 | 0.45 | 0.2 - 0.65 | 8 | 74% |
| 采样步数 | 30 | 30 - 30 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 8 | 71% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 8 | 40% |
| 宽度 | 1024x1024 (1.0) | - | 7 | 100% |
| 高度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- LoRA 模型强度 中位数 0.45，观测区间 0.2 - 0.65，8 个样本
- LoRA 文本强度 中位数 0.45，观测区间 0.2 - 0.65，8 个样本
- 采样步数 中位数 30，观测区间 30 - 30，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，8 个样本，取值分散，一致性仅 40%
- 宽度 最常用 1024x1024 (1.0)，7 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
