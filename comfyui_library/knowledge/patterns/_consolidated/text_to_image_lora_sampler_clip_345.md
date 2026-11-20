---
name: text_to_image_lora_sampler_clip_345
type: Text To Image
frequency: 6
level: weak
coverage: 0.863167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物面部+全身三视图-高清直出_2072004887482814465.json, 图片生成/图生图/全能图片V2  全能图片2图生图｜低价渠道版API专用_2090407880527798273.json, 图片生成/图生图/全能图片V2.1图生图 高质量参考图生成_2109387867872129026.json, 图片生成/图生图/全能图片低成本生成｜单张一毛批量图生图处理_2093138619555995650.json, 图片生成/图生图/全能图片图像编辑低价版 云端RunningHub高效处理方案_2098125131506864129.json, 图片生成/图生图/全能图片基础版图生图处理生成工作流工具包_2101044518236811265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_345

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/人物面部+全身三视图-高清直出_2072004887482814465.json、图片生成/图生图/全能图片V2  全能图片2图生图｜低价渠道版API专用_2090407880527798273.json、图片生成/图生图/全能图片V2.1图生图 高质量参考图生成_2109387867872129026.json、图片生成/图生图/全能图片低成本生成｜单张一毛批量图生图处理_2093138619555995650.json、图片生成/图生图/全能图片图像编辑低价版 云端RunningHub高效处理方案_2098125131506864129.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `RH_RhartImageNG31FlashImageToImage` —— 2/6 个有
- `RelayBanana2ImageGenerator` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CustomAddLabel` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_RhartImageNNb21ImageToImage` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `SeedVR2` —— 1/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1920 | 6 | 0% |
| 高度 | 80 | 80 - 1080 | 6 | 0% |
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 6 | 67% |
| 采样算法 | er_sde | - | 6 | 83% |
| 调度器 | beta | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1920，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1080，6 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
