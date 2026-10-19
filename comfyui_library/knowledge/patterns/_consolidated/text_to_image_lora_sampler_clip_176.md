---
name: text_to_image_lora_sampler_clip_176
type: Text To Image
frequency: 5
level: weak
coverage: 0.879
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json, 图片生成/文生图/krea2田园风格MJ感工作流_2102923019374125057.json, 图片生成/文生图/krea2田园风格MJ感工作流_2104384123690373122.json, 图片生成/文生图/krea2田园风格MJ感工作流_2104754840189624322.json, 视频生成/图生视频/krea2+Qwen3.5-自动多风格文生图 (1)_2085254333008007169.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json、图片生成/文生图/krea2田园风格MJ感工作流_2102923019374125057.json、图片生成/文生图/krea2田园风格MJ感工作流_2104384123690373122.json、图片生成/文生图/krea2田园风格MJ感工作流_2104754840189624322.json、视频生成/图生视频/krea2+Qwen3.5-自动多风格文生图 (1)_2085254333008007169.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ConditioningKrea2Rebalance` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `JjkText` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `solarL_SaveImagesToZip` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 5 | 48% |
| 高度 | 1024 | 80 - 1024 | 5 | 48% |
| 采样步数 | 8 | 4 - 8 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 5 | 18% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 48%
- 高度 中位数 1024，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 48%
- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，5 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
