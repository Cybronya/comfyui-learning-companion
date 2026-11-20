---
name: text_to_image_lora_sampler_clip_103
type: Text To Image
frequency: 13
level: weak
coverage: 0.886846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2基础图生图｜通用图像转换高质量生成_2095962002811342850.json, 图片生成/图生图/MOSS-Image人物三视图生成，面部+全身多角度高清直出角色设计利器_2114426707334746114.json, 图片生成/图生图/Moss-Image-人物面部+全身三视图-高清直出_2113912819136679938.json, 图片生成/图生图/Moss-Image-人物面部+全身三视图-高清直出｜人物角色图生图_2114297170357739522.json, 图片生成/图生图/krea2基础图生图_2071358346015371266.json, 图片生成/图生图/krea2基础图生图_2095763877953884162.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2097780554698678273.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098922055084367874.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098980585321623553.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2099656781432709122.json, 图片生成/图生图/基础图生图人像写真｜krea2摄影级生成_2095516228675788802.json, 图片生成/图生图/基础图生图稳定出图｜krea2 日常修图必备工作流_2096254734893146113.json, 图片生成/文生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083015619733180417.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Krea2基础图生图｜通用图像转换高质量生成_2095962002811342850.json、图片生成/图生图/MOSS-Image人物三视图生成，面部+全身多角度高清直出角色设计利器_2114426707334746114.json、图片生成/图生图/Moss-Image-人物面部+全身三视图-高清直出_2113912819136679938.json、图片生成/图生图/Moss-Image-人物面部+全身三视图-高清直出｜人物角色图生图_2114297170357739522.json、图片生成/图生图/krea2基础图生图_2071358346015371266.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 11/13 个有
- `ConditioningZeroOut` —— 9/13 个有
- `MultiTextConcatenate` —— 9/13 个有
- `RH_Captioner` —— 9/13 个有
- `ShowText|pysssss` —— 9/13 个有
- `String Literal` —— 9/13 个有
- `solarL_SaveImagesToZip` —— 9/13 个有
- `孤海注释` —— 8/13 个有
- `PreviewImage` —— 4/13 个有
- `RunningHub Deepcleaner` —— 4/13 个有
- `SeedVR2` —— 4/13 个有
- `TextEncodeQwenImageEditPlus` —— 4/13 个有
- `EmptyImage` —— 3/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1920 | 13 | 0% |
| 高度 | 80 | 80 - 1536 | 13 | 0% |
| 采样步数 | 4 | 4 - 10 | 13 | 57% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 13 | 53% |
| 采样算法 | er_sde | - | 13 | 85% |
| 调度器 | beta | - | 13 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，13 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 10，13 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 85%
- 调度器 最常用 beta，13 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
