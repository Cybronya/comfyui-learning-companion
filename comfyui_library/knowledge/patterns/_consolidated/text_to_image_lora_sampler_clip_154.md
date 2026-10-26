---
name: text_to_image_lora_sampler_clip_154
type: Text To Image
frequency: 11
level: weak
coverage: 0.907364
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-Turbo+ LoRA文生图高清放大2K直出工作流（W版本）懂的都懂_2101631409948545026.json, 图片生成/文生图/Krea2-Turbo+LoRA文生图高清放大2K直出｜W版本人像写真商单利器_2101877172779708417.json, 图片生成/文生图/Krea2人像写真｜古装汉服肚兜美少女文生图_2101186021638627329.json, 图片生成/文生图/Krea2性感长腿美女生成｜人像写真文生图_2095125889968336898.json, 图片生成/文生图/Krea2极品美女生成器，极致身材流量美图文生图_2110872696534949890.json, 图片生成/文生图/Krea2洛茜cos写真生成｜二次元角色cos人像文生图_2095089762595074050.json, 图片生成/文生图/Krea2甜妹人像写真｜长腿白丝美少女文生图_2097208174314090497.json, 图片生成/文生图/Krea2美女高清写真｜文生图人像美少女_2092063279031083010.json, 图片生成/文生图/Krea2长腿白丝甜妹文生图｜人像写真美少女生成_2097076921250177026.json, 图片生成/文生图/Krea2长腿白丝甜妹生成｜美少女人像写真文生图_2094559276558807041.json, 图片生成/文生图/Z-Image Turbo+LoRA文生图高清放大2K直出处理工作流_2102187279212171265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Krea2-Turbo+ LoRA文生图高清放大2K直出工作流（W版本）懂的都懂_2101631409948545026.json、图片生成/文生图/Krea2-Turbo+LoRA文生图高清放大2K直出｜W版本人像写真商单利器_2101877172779708417.json、图片生成/文生图/Krea2人像写真｜古装汉服肚兜美少女文生图_2101186021638627329.json、图片生成/文生图/Krea2性感长腿美女生成｜人像写真文生图_2095125889968336898.json、图片生成/文生图/Krea2极品美女生成器，极致身材流量美图文生图_2110872696534949890.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 10/11 个有
- `JjkText` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `solarL_SaveImagesToZip` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `DF_Integer` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `Fast Groups Muter (rgthree)` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `LayerUtility: PurgeVRAM` —— 3/11 个有
- `SeedVR2LoadDiTModel` —— 3/11 个有
- `SeedVR2LoadVAEModel` —— 3/11 个有
- `SeedVR2VideoUpscaler` —— 3/11 个有
- `EmptySD3LatentImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 0% |
| 高度 | 80 | 80 - 1024 | 11 | 0% |
| 采样步数 | 4 | 4 - 37 | 11 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 76% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 37，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（19/11 个样本）：Steps较低可能导致细节不足
