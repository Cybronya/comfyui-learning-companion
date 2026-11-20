---
name: text_to_image_lora_sampler_clip_295
type: Text To Image
frequency: 7
level: strong
coverage: 0.890857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json, 图片生成/图生图/千问Qwen Image 2.1多图编辑｜一次处理多张素材图_2103029100855255041.json, 图片生成/图生图/模特换头换脸神器｜Face+Swap++Qwen-Image-2.1 电商出图必备_2105513776450723842.json, 图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json, 图片生成/图生图/角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json, 图片生成/文生图/文生图参考生图2合1 二合一图像生成方案_2108618211246825474.json, 图片生成/文生图/文生图参考生图二合一改进版｜双模式图像生成工作流_2108383787649425409.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_295

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen2.1角色卡立绘工作流，图生图角色设计生成工具_2106472690608599042.json、图片生成/图生图/千问Qwen Image 2.1多图编辑｜一次处理多张素材图_2103029100855255041.json、图片生成/图生图/模特换头换脸神器｜Face+Swap++Qwen-Image-2.1 电商出图必备_2105513776450723842.json、图片生成/图生图/绅士私房写真图片Qwen2.1工作流，图生图人像写真处理工具_2106121029063102465.json、图片生成/图生图/角色头部替换Qwen2.1工作流，图生图面部替换处理工具_2106092844099391489.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 5/7 个有
- `llama_cpp_model_loader` —— 5/7 个有
- `BatchImagesNode` —— 4/7 个有
- `TextGenerateLTX2Prompt` —— 4/7 个有
- `easy imageConcat` —— 4/7 个有
- `PreviewAny` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `easy clearCacheAll` —— 3/7 个有
- `llama_cpp_parameters` —— 3/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
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
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
