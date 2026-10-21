---
name: text_to_image_lora_sampler_clip_199
type: Text To Image
frequency: 6
level: weak
coverage: 0.891
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Kera2 Turbo 4步极速出图｜美少女写实文生图_2098723233347493890.json, 图片生成/文生图/Kera2 Turbo 4步极速出图｜美少女写实文生图_2098731918736056321.json, 图片生成/文生图/Kera2 Turbo 4步极速工作流_2098378466390536193.json, 图片生成/文生图/Krea 2田园风格感文生图处理工作流_2101011311219003393.json, 图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json, 图片生成/文生图/krea2田园风格MJ感工作流｜文生图氛围感拉满_2100772461267734530.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_199

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Kera2 Turbo 4步极速出图｜美少女写实文生图_2098723233347493890.json、图片生成/文生图/Kera2 Turbo 4步极速出图｜美少女写实文生图_2098731918736056321.json、图片生成/文生图/Kera2 Turbo 4步极速工作流_2098378466390536193.json、图片生成/文生图/Krea 2田园风格感文生图处理工作流_2101011311219003393.json、图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 5/6 个有
- `solarL_SaveImagesToZip` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `CR Prompt Text` —— 3/6 个有
- `ConditioningKrea2Rebalance` —— 3/6 个有
- `JjkShowText` —— 3/6 个有
- `ResolutionSelector` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `TTResolutionSelector` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `Text to String` —— 3/6 个有
- `llama_cpp_parameters` —— 3/6 个有
- `LoadImage` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 6 | 67% |
| 采样算法 | er_sde | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 512 | 6 | 0% |
| 高度 | 80 | 80 - 512 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 512，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 512，6 个样本，取值分散，一致性仅 0%
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
