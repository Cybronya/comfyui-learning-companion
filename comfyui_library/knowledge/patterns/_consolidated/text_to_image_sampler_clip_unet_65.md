---
name: text_to_image_sampler_clip_unet_65
type: Text To Image
frequency: 11
level: weak
coverage: 0.871091
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2田园风格感文生图处理工作流_2101011311219003393.json, 图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json, 图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json, 图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json, 图片生成/文生图/Qwen image2.1角色设定卡神器｜1分钟出图效率翻倍_2111098004596940801.json, 图片生成/文生图/Qwen image2.1角色设定卡，一分钟快速出图方案_2111208299730395138.json, 图片生成/文生图/krea2 MJ风格工作流 美学风格生成_2109041547172999169.json, 图片生成/文生图/krea2_MJ风格工作流_2108594095500386306.json, 图片生成/文生图/krea2全自动反推工作流_2099842463920902146.json, 图片生成/文生图/krea2田园风格MJ感工作流_2100583054992568322.json, 图片生成/文生图/krea2田园风格MJ感工作流｜文生图氛围感拉满_2100772461267734530.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Krea 2田园风格感文生图处理工作流_2101011311219003393.json、图片生成/文生图/Krea2全自动反推工作流 文生图提示词反推_2100275220467773441.json、图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json、图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json、图片生成/文生图/Qwen image2.1角色设定卡神器｜1分钟出图效率翻倍_2111098004596940801.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `JjkText` —— 8/11 个有
- `solarL_SaveImagesToZip` —— 8/11 个有
- `孤海注释` —— 8/11 个有
- `CR Prompt Text` —— 7/11 个有
- `ConditioningKrea2Rebalance` —— 7/11 个有
- `ConditioningZeroOut` —— 7/11 个有
- `SetNode` —— 7/11 个有
- `TTResolutionSelector` —— 7/11 个有
- `LoadImage` —— 6/11 个有
- `LayerUtility: TextJoin` —— 4/11 个有
- `PreviewAny` —— 4/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `ResolutionSelector` —— 4/11 个有
- `Seed (rgthree)` —— 4/11 个有
- `TextEncodeQwenImage21` —— 4/11 个有
- `Label (rgthree)` —— 3/11 个有
- `MuyeLoadImage` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 56% |
| 采样算法 | er_sde | - | 11 | 73% |
| 调度器 | beta | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1024 | 11 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 73%
- 调度器 最常用 beta，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高发问题（17/11 个样本）：Steps较低可能导致细节不足
