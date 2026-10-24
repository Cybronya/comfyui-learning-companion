---
name: unknown_workflow_sampler_clip_unet_45
type: Unknown Workflow
frequency: 17
level: weak
coverage: 0.952353
common_nodes: [CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json, 图片生成/文生图/ZImageBase文生图亮亮丝袜美女_2063529324246036482.json, 图片生成/文生图/ZImageBase文生图美女丝袜_2064861858766614530.json, 图片生成/文生图/ZImage女神_2063571918896328705.json, 图片生成/文生图/Z_image2512文生图_2055512539395567617.json, 图片生成/文生图/Z_image_tubf16全量模型出图_2055504260586065921.json, 图片生成/文生图/Z_image_turbo_文生图_1998723273162641410.json, 图片生成/文生图/Z_image_turbo出图_2055508247259435010.json, 图片生成/文生图/Z_image_turbo即梦生图免费版_1998032212584988673.json, 图片生成/文生图/Z_image_turbo工作流_1994234495897452546.json, 图片生成/文生图/Z_image文生图标准版_2064278139861299201.json, 图片生成/文生图/Zimage-Turbo文生图+写实光影+Engineer大师模式_2042080099603845121.json, 图片生成/文生图/Zimage文成图V1.0_2061670898217873409.json, 图片生成/文生图/z-image base 插画 文生图 工作流_2028391930756866049.json, 图片生成/文生图/z-image base 插画 文生图 工作流_2028716736136089602.json, 图片生成/文生图/【KKAI】开班课生图工作流_2037521440781639682.json, 图片生成/文生图/文生图+写实光影LORA+Engineer大师模式_2029093017558196225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_45

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/ZIMAGE-Turbo文生图+写实光影LORA+Engineer大师模式_2015980476426620929.json、图片生成/文生图/ZImageBase文生图亮亮丝袜美女_2063529324246036482.json、图片生成/文生图/ZImageBase文生图美女丝袜_2064861858766614530.json、图片生成/文生图/ZImage女神_2063571918896328705.json、图片生成/文生图/Z_image2512文生图_2055512539395567617.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 16/17 个有
- `CLIPLoader` —— 14/17 个有
- `LoraLoaderModelOnly` —— 11/17 个有
- `CR Text` —— 4/17 个有
- `CLIPLoaderGGUF` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `ClipLoaderGGUF` —— 1/17 个有
- `HAIGC_SaveImagesToZip` —— 1/17 个有
- `QwenImageLatentAspectRatio` —— 1/17 个有
- `TTResolutionSelector` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 36 | 17 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 17 | 25% |
| 采样算法 | euler | - | 17 | 53% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 36，17 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，17 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，17 个样本，一致性 53%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（9/17 个样本）：Steps较低可能导致细节不足
