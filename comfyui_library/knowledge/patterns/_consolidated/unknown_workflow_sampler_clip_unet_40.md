---
name: unknown_workflow_sampler_clip_unet_40
type: Unknown Workflow
frequency: 18
level: weak
coverage: 0.959444
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json, 图片生成/文生图/ZImageBase文生图亮亮丝袜美女_2063529324246036482.json, 图片生成/文生图/ZImageBase文生图美女丝袜_2064861858766614530.json, 图片生成/文生图/ZImage女神_2063571918896328705.json, 图片生成/文生图/Z_image2512文生图_2055512539395567617.json, 图片生成/文生图/Z_image_tubf16全量模型出图_2055504260586065921.json, 图片生成/文生图/Z_image_turbo_文生图_1998723273162641410.json, 图片生成/文生图/Z_image_turbo出图_2055508247259435010.json, 图片生成/文生图/Z_image_turbo即梦生图免费版_1998032212584988673.json, 图片生成/文生图/Z_image_turbo工作流_1994234495897452546.json, 图片生成/文生图/Z_image文生图标准版_2064278139861299201.json, 图片生成/文生图/Zimage-Turbo文生图+写实光影+Engineer大师模式_2042080099603845121.json, 图片生成/文生图/danotebook-qwen-image-2512_2062470910413725697.json, 图片生成/文生图/image_ovis_文生图_1998947182181015554.json, 图片生成/文生图/image_qwen_Image_2512 BF16_2073295897374584833.json, 图片生成/文生图/qwen-image 4步极速生图_1954932387395223553.json, 图片生成/文生图/qwen-image 8步快速生图_1954932461516963842.json, 图片生成/文生图/qwen-image 极速生图_1956936946464296962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json、图片生成/文生图/ZImageBase文生图亮亮丝袜美女_2063529324246036482.json、图片生成/文生图/ZImageBase文生图美女丝袜_2064861858766614530.json、图片生成/文生图/ZImage女神_2063571918896328705.json、图片生成/文生图/Z_image2512文生图_2055512539395567617.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 16/18 个有
- `LoraLoaderModelOnly` —— 11/18 个有
- `CR Text` —— 5/18 个有
- `CR SDXL Aspect Ratio` —— 3/18 个有
- `CLIPLoaderGGUF` —— 1/18 个有
- `ClipLoaderGGUF` —— 1/18 个有
- `Float` —— 1/18 个有
- `Int` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `TTResolutionSelector` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 18 | 32% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 18 | 19% |
| 采样算法 | euler | - | 18 | 72% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，18 个样本，取值分散，一致性仅 32%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，18 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，18 个样本，一致性 72%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（13/18 个样本）：Steps较低可能导致细节不足
