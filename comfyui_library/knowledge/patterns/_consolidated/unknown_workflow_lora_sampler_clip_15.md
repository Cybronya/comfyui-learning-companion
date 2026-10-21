---
name: unknown_workflow_lora_sampler_clip_15
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.923308
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Concatenate, Text Multiline, SDXLEmptyLatentSizePicker+]
members: [图片生成/文生图/1988478076659130370.json, 图片生成/文生图/QwenImage 4K高清大图DyPE直出_2000788947687141378.json, 图片生成/文生图/Qwen_Image_2512_文生图_bf16版本_2008392762101604354.json, 图片生成/文生图/Qwen_Image_2512文生图工作流_2063234247065948161.json, 图片生成/文生图/Qwen白丝长腿丝袜美腿_2019647690329559041.json, 图片生成/文生图/Z-I-B道具快乐美女_2040453074061369345.json, 图片生成/文生图/Z-I-B长腿肉腿刺客美女_2056916021260410881.json, 图片生成/文生图/Z-Image-Base文生图亮亮丝袜美女_2018164986979295233.json, 图片生成/文生图/Z-Image-Turbo 4K高清大图DyPE直出_2000758971898134529.json, 图片生成/文生图/千问Qwen_image文生图海报_fp8_官方版26125_2015389169786294274.json, 图片生成/文生图/基础文生图 Z-Image-Turbo（带LoRA加载节点）_2007330137645260802.json, 图片生成/文生图/多风格绘本_2004518809287491586.json, 图片生成/文生图/沙雕动漫怪兽神兽多视图三视图（加速版）_2002568995201007617.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1988478076659130370.json、图片生成/文生图/QwenImage 4K高清大图DyPE直出_2000788947687141378.json、图片生成/文生图/Qwen_Image_2512_文生图_bf16版本_2008392762101604354.json、图片生成/文生图/Qwen_Image_2512文生图工作流_2063234247065948161.json、图片生成/文生图/Qwen白丝长腿丝袜美腿_2019647690329559041.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 10/13 个有
- `Text Multiline` —— 5/13 个有
- `ConditioningZeroOut` —— 4/13 个有
- `CompressImages` —— 3/13 个有
- `SDXLEmptyLatentSizePicker+` —— 3/13 个有
- `CR Text Concatenate` —— 2/13 个有
- `DyPE_FLUX` —— 2/13 个有
- `RMBG` —— 2/13 个有
- `Anything Everywhere3` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 13 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 13 | 20% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1344x768 (1.75) | - | 3 | 67% |
| 高度 | 1 | 1 - 4 | 3 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，13 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 最常用 1344x768 (1.75)，3 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 高发问题（9/13 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Concatenate、Text Multiline、SDXLEmptyLatentSizePicker+
