---
name: text_to_image_lora_sampler_clip_63
type: Text To Image
frequency: 16
level: strong
coverage: 0.891563
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json, 图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json, 图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json, 图片生成/文生图/Bkz人像摄影应用｜krea2-turbo-bf16人物特效文生图_2095790317579620353.json, 图片生成/文生图/Flux3_klein文生图，其它风格画作创意出图_2111570087491756033.json, 图片生成/文生图/Krea2人像摄影应用｜turbo-bf16写实人像生成_2095562706337230850.json, 图片生成/文生图/Krea2文生图极简工作流｜输入描述直接出高质量图_2107649169803534338.json, 图片生成/文生图/MOSS文生图2K极速版｜美少女写实出图快到飞起_2114026495923544065.json, 图片生成/文生图/Moss Base文生图基础版 基础模式图像生成处理工具_2113776137825513473.json, 图片生成/文生图/Moss SFT Fixed文生图 修正版高质量图像生成工具_2113722107573129217.json, 图片生成/文生图/Moss SFT文生图极简版 极简模式高质量生成工具_2113777659305095170.json, 图片生成/文生图/Moss Sft Fixed文生图｜SFT微调模型稳定文生图体验_2113592740046000130.json, 图片生成/文生图/Z-Image Turbo特定风格人像大作文生图处理工具_2101751504242831361.json, 图片生成/文生图/flux3_image_klein文生图，创意形象高效直出_2111545656975384578.json, 图片生成/文生图/flux3_image_klein文生图｜学AI曹同学同款直出流_2111340043469156354.json, 图片生成/文生图/自动词优化版Moss-image Sft文生图｜描述更省心_2112412795026370562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json、图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json、图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json、图片生成/文生图/Bkz人像摄影应用｜krea2-turbo-bf16人物特效文生图_2095790317579620353.json、图片生成/文生图/Flux3_klein文生图，其它风格画作创意出图_2111570087491756033.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 13/16 个有
- `EmptyFlux2LatentImage` —— 9/16 个有
- `ConditioningZeroOut` —— 6/16 个有
- `PrimitiveStringMultiline` —— 6/16 个有
- `ClownsharKSampler_Beta` —— 3/16 个有
- `LoraLoader` —— 3/16 个有
- `ModelSamplingAuraFlow` —— 3/16 个有
- `TextGenerate` —— 3/16 个有
- `KSamplerAdvanced` —— 2/16 个有
- `LatentUpscaleBy` —— 2/16 个有
- `Seed (rgthree)` —— 2/16 个有
- `PreviewAny` —— 1/16 个有
- `easy anythingIndexSwitch` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（19/16 个样本）：Steps较低可能导致细节不足
