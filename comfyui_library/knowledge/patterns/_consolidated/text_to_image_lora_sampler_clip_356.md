---
name: text_to_image_lora_sampler_clip_356
type: Text To Image
frequency: 5
level: strong
coverage: 0.8928
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/专业AI婚纱工作流V2｜高清直出人为可控精修_2095576824465149954.json, 图片生成/图生图/千问3.5 LLAMA大模型对话工作流｜接入指南附飞书文档_2111267612377309186.json, 图片生成/图生图/千问3.5 LLAMA接入工作流｜大模型能力加持其他场景｜玩法自由拓展_2102276173383421953.json, 图片生成/图生图/千问3.5 LLAMA本地推理，动画剧本辅助生成_2111519934110064642.json, 图片生成/图生图/高清直出人为可控｜专业AI婚纱工作流V2人像写真_2095826559549661186.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_356

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/专业AI婚纱工作流V2｜高清直出人为可控精修_2095576824465149954.json、图片生成/图生图/千问3.5 LLAMA大模型对话工作流｜接入指南附飞书文档_2111267612377309186.json、图片生成/图生图/千问3.5 LLAMA接入工作流｜大模型能力加持其他场景｜玩法自由拓展_2102276173383421953.json、图片生成/图生图/千问3.5 LLAMA本地推理，动画剧本辅助生成_2111519934110064642.json、图片生成/图生图/高清直出人为可控｜专业AI婚纱工作流V2人像写真_2095826559549661186.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/5 个有
- `easy saveText` —— 3/5 个有
- `BatchImagesNode` —— 2/5 个有
- `RH_RhartImageG2ImageToImage` —— 2/5 个有
- `Text` —— 2/5 个有
- `TextConcat` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ImpactMakeImageList` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
