---
name: text_to_image_lora_sampler_clip_218
type: Text To Image
frequency: 3
level: strong
coverage: 0.821
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [PIP_图像联结, easy clearCacheAll, easy imageConcat]
members: [图片生成/图生图/2106092844099391489.json, 图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json, 图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_218

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2106092844099391489.json、图片生成/文生图/Qwen Image 2.1角色设定卡一分钟出图工作流，角色设计文生图工具_2107186101369790465.json、图片生成/文生图/Qwen image2.1角色设定卡极速出图｜一分钟搞定角色设计_2107001532909703169.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `LayerUtility: TextJoin` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `PIP_图像联结` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenImage21Cache` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：PIP_图像联结、easy clearCacheAll、easy imageConcat
