---
name: text_to_image_lora_sampler_clip_263
type: Text To Image
frequency: 7
level: strong
coverage: 0.849143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json, 图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json, 图片生成/图生图/角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json, 图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json, 图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json, 图片生成/文生图/Qwen image2.1角色设定卡神器｜1分钟出图效率翻倍_2111098004596940801.json, 图片生成/文生图/Qwen image2.1角色设定卡，一分钟快速出图方案_2111208299730395138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_263

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json、图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json、图片生成/图生图/角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json、图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json、图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `LayerUtility: TextJoin` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `PreviewImage` —— 3/7 个有
- `QwenImage21Cache` —— 3/7 个有
- `easy clearCacheAll` —— 3/7 个有
- `easy imageConcat` —— 3/7 个有
- `ImageScaleBy` —— 2/7 个有
- `CR Prompt List` —— 1/7 个有
- `PIP_图像联结` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
