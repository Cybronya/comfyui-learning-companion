---
name: unknown_workflow_lora_sampler_vae_8
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7455
common_nodes: [CR Text, ImageLoader, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, MultiplePathsInput, PrimitiveStringMultiline, ProcessString, SaveImage, Text Find and Replace, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, easy cleanGpuUsed, easy convertAnything, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen一图裂变多图图片生成多个姿势动作图片pose模特模特动作图片生成_1985533239932633090.json, 图片生成/图生图/Qwen一图裂变多图图片生成多个姿势动作图片pose模特模特动作图片生成_2060206994371473409.json, 图片生成/图生图/Qwen模特动作随机裂变1-8张可选，尺寸可选_2014011672737882114.json, 图片生成/图生图/Qwen模特无限生成器2025版 一图变多图_1983715380814389250.json, 图片生成/图生图/一图变多图，多动作裂变，服装类目及小红书必备_1985753374798819329.json, 图片生成/图生图/模特套图惰性裂变-QWEN_2043730720052482050.json, 图片生成/图生图/🍑Qwen模特无限孵蛋器V3版 一图裂变多图🍑_1983360553869582337.json, 平台全量/Qwen无限裂变套图-模特人物专用_1988923477430243329.json, 平台全量/Qwen模特无限孵蛋器V3版+一图裂变多图 高一致性多姿生成  人脸、服饰、风格、光影 上保持高_1988502714554433538.json, 平台全量/一图生成多角度视图 不同姿势随机变化 电商模特图-裂变多图_1987673966187843585.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen一图裂变多图图片生成多个姿势动作图片pose模特模特动作图片生成_1985533239932633090.json、图片生成/图生图/Qwen一图裂变多图图片生成多个姿势动作图片pose模特模特动作图片生成_2060206994371473409.json、图片生成/图生图/Qwen模特动作随机裂变1-8张可选，尺寸可选_2014011672737882114.json、图片生成/图生图/Qwen模特无限生成器2025版 一图变多图_1983715380814389250.json、图片生成/图生图/一图变多图，多动作裂变，服装类目及小红书必备_1985753374798819329.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 10 个 workflow 都包含：
- `CR Text`
- `ImageLoader`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `MultiplePathsInput`
- `PrimitiveStringMultiline`
- `ProcessString`
- `SaveImage`
- `Text Find and Replace`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `Qwen3_VQA` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `VAELoader` —— 9/10 个有
- `RH_LLMAPI_NODE` —— 7/10 个有
- `easy anythingIndexSwitch` —— 7/10 个有
- `GLM_Vision_ImageToPrompt` —— 3/10 个有
- `ImpactSwitch` —— 3/10 个有
- `RHHiddenNodes` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `StringToInt` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta57 | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta57，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
