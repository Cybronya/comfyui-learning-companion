---
name: text_to_image_lora_sampler_clip_176
type: Text To Image
frequency: 10
level: strong
coverage: 0.9009
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/火山引擎视频去字幕流｜一键擦除画面字幕文字_2098751317052313601.json, 图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json, 图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json, 图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json, 图片生成/文生图/Flux3_klein文生图，其它风格画作创意出图_2111570087491756033.json, 图片生成/文生图/MOSS Image SFT文生图 4步加速写真海报生成工具_2114091509032247297.json, 图片生成/文生图/MOSS image文生图基础版 提示词直出图像生成工具_2113349395633754113.json, 图片生成/文生图/MOSS-Image SFT文生图4步加速版，人像写真画质细腻出图飞快_2114450656412127234.json, 图片生成/文生图/MOSS-Image SFT文生图4步加速版｜人像写真出图效率翻倍_2114298908456349698.json, 图片生成/文生图/MOSS-Image SFT文生图4步加速版｜人像写真海报直出利器_2113890058133659649.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/火山引擎视频去字幕流｜一键擦除画面字幕文字_2098751317052313601.json、图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json、图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json、图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json、图片生成/文生图/Flux3_klein文生图，其它风格画作创意出图_2111570087491756033.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `EmptyFlux2LatentImage` —— 6/10 个有
- `ResolutionSelector` —— 6/10 个有
- `ImpactInt` —— 4/10 个有
- `MuyeTextEditOutput` —— 4/10 个有
- `ClownsharKSampler_Beta` —— 3/10 个有
- `LoraLoader` —— 3/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `RH_VolcSubtitleEraseProVideo` —— 1/10 个有
- `SaveVideo` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（15/10 个样本）：Steps较低可能导致细节不足
