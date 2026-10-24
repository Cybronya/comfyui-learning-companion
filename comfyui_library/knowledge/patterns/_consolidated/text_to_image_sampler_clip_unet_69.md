---
name: text_to_image_sampler_clip_unet_69
type: Text To Image
frequency: 10
level: weak
coverage: 0.9171
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图_2108503764775821313.json, 图片生成/文生图/文生图_2110627225245671426.json, 图片生成/文生图/文生图ziamge_2015340435937431553.json, 图片生成/文生图/文生图全能直出｜G-2图片生成 电商平面设计利器_2089464781400002562.json, 图片生成/文生图/文生图基础流｜krea2文生图图生图双模式_2089846295853879298.json, 图片生成/文生图/文生图工作流 高质量画面直出稳定出图方案_2109419687699374082.json, 图片生成/文生图/文生图工作流高质量画面直出稳定出图方案 高质量画面直出_2109747077147348994.json, 图片生成/文生图/文生图工作流｜即梦图片4.6中文文字精准生成_2100836535871557633.json, 图片生成/文生图/文生图超快出图｜输入描述秒级生成高质量图片_2101533926996144130.json, 图片生成/文生图/最新qwen+image2512文生图｜基础工作流高质量出图_2095294645029920770.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/文生图_2108503764775821313.json、图片生成/文生图/文生图_2110627225245671426.json、图片生成/文生图/文生图ziamge_2015340435937431553.json、图片生成/文生图/文生图全能直出｜G-2图片生成 电商平面设计利器_2089464781400002562.json、图片生成/文生图/文生图基础流｜krea2文生图图生图双模式_2089846295853879298.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 8/10 个有
- `JjkText` —— 7/10 个有
- `solarL_SaveImagesToZip` —— 7/10 个有
- `孤海注释` —— 7/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `CFGNorm` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `QwenImageLatentAspectRatio` —— 1/10 个有
- `RH_BytedanceJimeng46TextToImage` —— 1/10 个有
- `RH_RhartImageG2TextToImage` —— 1/10 个有
- `Text Multiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 10 | 0% |
| 高度 | 80 | 80 - 1280 | 10 | 0% |
| 采样步数 | 4 | 4 - 10 | 10 | 54% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 10 | 54% |
| 采样算法 | er_sde | - | 10 | 70% |
| 调度器 | beta | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，10 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1280，10 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 10，10 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，10 个样本
- 采样算法 最常用 er_sde，10 个样本，一致性 70%
- 调度器 最常用 beta，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
