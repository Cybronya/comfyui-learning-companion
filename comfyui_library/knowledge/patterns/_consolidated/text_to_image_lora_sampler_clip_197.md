---
name: text_to_image_lora_sampler_clip_197
type: Text To Image
frequency: 9
level: weak
coverage: 0.870556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS文生图全节点注释版 反推提示词图生图处理工具_2112993127761006593.json, 图片生成/反推提示词/MOSS文生图全节点注释版｜附反推提示词新手照抄就能跑_2112927305474596865.json, 图片生成/图生图/G image2.5全能系列模型｜单张成本低至7分钱_2098728369797025793.json, 图片生成/图生图/Moss简洁文生图流程，图生图搭配玩法不设限_2112692396340375554.json, 图片生成/文生图/MOSS Image SFT文生图 4步加速写真海报生成工具_2114091509032247297.json, 图片生成/文生图/MOSS-Image SFT文生图4步加速版，人像写真画质细腻出图飞快_2114450656412127234.json, 图片生成/文生图/MOSS-Image SFT文生图4步加速版｜人像写真出图效率翻倍_2114298908456349698.json, 图片生成/文生图/MOSS-Image SFT文生图4步加速版｜人像写真海报直出利器_2113890058133659649.json, 图片生成/文生图/MOSS文生图+全节点注释_2112471507770372097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/MOSS文生图全节点注释版 反推提示词图生图处理工具_2112993127761006593.json、图片生成/反推提示词/MOSS文生图全节点注释版｜附反推提示词新手照抄就能跑_2112927305474596865.json、图片生成/图生图/G image2.5全能系列模型｜单张成本低至7分钱_2098728369797025793.json、图片生成/图生图/Moss简洁文生图流程，图生图搭配玩法不设限_2112692396340375554.json、图片生成/文生图/MOSS Image SFT文生图 4步加速写真海报生成工具_2114091509032247297.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 8/9 个有
- `ResolutionSelector` —— 8/9 个有
- `solarL_SaveImagesToZip` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `MuyeTextEditOutput` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 5/9 个有
- `ImpactInt` —— 4/9 个有
- `SkipLayerGuidanceDiTSimple` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `VOSR2ModelLoader` —— 3/9 个有
- `VOSR2Upscale` —— 3/9 个有
- `CreateBoundingBoxes` —— 1/9 个有
- `LLGPTImage25Generator` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `MOSSImageLayoutPrompt` —— 1/9 个有
- `PreviewAny` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 73% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 1024 | 9 | 0% |
| 高度 | 80 | 80 - 1024 | 9 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 0%
- 高发问题（15/9 个样本）：Steps较低可能导致细节不足
