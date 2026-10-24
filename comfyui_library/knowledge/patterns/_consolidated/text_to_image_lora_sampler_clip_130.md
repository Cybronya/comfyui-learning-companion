---
name: text_to_image_lora_sampler_clip_130
type: Text To Image
frequency: 11
level: weak
coverage: 0.897
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2基础图生图｜通用图像转换高质量生成_2095962002811342850.json, 图片生成/图生图/LEON 产品精修｜图生图商品图一键出高级感 商详必备_2097581380665438210.json, 图片生成/图生图/LEON 无损放大｜细节恢复加肌理强化 图生图画质起飞_2097573526676000770.json, 图片生成/图生图/krea2基础图生图_2071358346015371266.json, 图片生成/图生图/krea2基础图生图_2095763877953884162.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2097780554698678273.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098922055084367874.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2098980585321623553.json, 图片生成/图生图/krea2基础图生图工作流｜人像写真摄影图片生成_2099656781432709122.json, 图片生成/图生图/基础图生图人像写真｜krea2摄影级生成_2095516228675788802.json, 图片生成/图生图/基础图生图稳定出图｜krea2 日常修图必备工作流_2096254734893146113.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Krea2基础图生图｜通用图像转换高质量生成_2095962002811342850.json、图片生成/图生图/LEON 产品精修｜图生图商品图一键出高级感 商详必备_2097581380665438210.json、图片生成/图生图/LEON 无损放大｜细节恢复加肌理强化 图生图画质起飞_2097573526676000770.json、图片生成/图生图/krea2基础图生图_2071358346015371266.json、图片生成/图生图/krea2基础图生图_2095763877953884162.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 9/11 个有
- `JjkText` —— 9/11 个有
- `MultiTextConcatenate` —— 9/11 个有
- `RH_Captioner` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `String Literal` —— 9/11 个有
- `solarL_SaveImagesToZip` —— 9/11 个有
- `孤海注释` —— 8/11 个有
- `EmptyImage` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `Image Comparer (rgthree)` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `ttN int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1536 | 11 | 0% |
| 采样步数 | 4 | 4 - 10 | 11 | 55% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 65% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 10，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（9/11 个样本）：Steps较低可能导致细节不足
