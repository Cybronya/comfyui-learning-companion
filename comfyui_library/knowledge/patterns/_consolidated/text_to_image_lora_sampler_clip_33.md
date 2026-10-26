---
name: text_to_image_lora_sampler_clip_33
type: Text To Image
frequency: 21
level: weak
coverage: 0.90781
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MOSS_4步_FP32模型VS25步_SFT模型文生图｜美少女写实两版对比_2114253844162113538.json, 图片生成/文生图/MOSS_Image_SFT_BF16+4步加速LoRA文生图｜美少女写实出图快_2114248990190559233.json, 图片生成/文生图/MOSS与Krea2双模型文生图 高质量图像生成处理工具_2113761690222415874.json, 图片生成/文生图/MOSS与Krea2联合文生图｜双模型加持创意生图更出片_2113529543649751042.json, 图片生成/文生图/MOSS动漫加速工作流 动漫游戏角色文生图处理工具_2113700438838177794.json, 图片生成/文生图/MOSS动漫加速工作流_2113206327819456514.json, 图片生成/文生图/MOSS动漫加速工作流｜动漫角色游戏角色文生图快速产出_2113510899704225793.json, 图片生成/文生图/MOSS文生图2K极速 人物特效角色一致性生成工具_2114130557742444546.json, 图片生成/文生图/MOSS文生图2K极速 角色设计表演高速生成工具_2113734631899090946.json, 图片生成/文生图/MOSS文生图2K极速 高速标准模式图像生成处理工具_2113339863922728961.json, 图片生成/文生图/MOSS文生图2K极速版 写实美少女图像生成工具_2113774445595811841.json, 图片生成/文生图/MOSS文生图2K极速版 写实美少女高速图像生成工具_2113483541777567746.json, 图片生成/文生图/MOSS文生图2K极速版 高速文生图处理生成工具_2112975792320892929.json, 图片生成/文生图/MOSS文生图2K极速版工作流，美少女写实风一键生成高清图_2114460846381420546.json, 图片生成/文生图/MOSS文生图2K极速版文生图｜美少女写实风出图不限量_2114275926564491266.json, 图片生成/文生图/MOSS文生图2K极速版，人物更真实皮肤质感自然高清直出_2114452341444403202.json, 图片生成/文生图/MOSS文生图2K极速版，美少女写实风格一键直出高清图片_2114484676936159233.json, 图片生成/文生图/MOSS文生图2K极速版｜美少女写实文生图秒出_2114049430289731586.json, 图片生成/文生图/MOSS文生图2K极速版｜美少女写实风格快速出图体验_2113579003356471297.json, 图片生成/文生图/MOSS联合Krea2双模型文生图｜创意文字出图新玩法体验_2113502670672719874.json, 图片生成/文生图/遇见AI Moss image 文生图｜8步加速基础流省时_2112458024404209665.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/MOSS_4步_FP32模型VS25步_SFT模型文生图｜美少女写实两版对比_2114253844162113538.json、图片生成/文生图/MOSS_Image_SFT_BF16+4步加速LoRA文生图｜美少女写实出图快_2114248990190559233.json、图片生成/文生图/MOSS与Krea2双模型文生图 高质量图像生成处理工具_2113761690222415874.json、图片生成/文生图/MOSS与Krea2联合文生图｜双模型加持创意生图更出片_2113529543649751042.json、图片生成/文生图/MOSS动漫加速工作流 动漫游戏角色文生图处理工具_2113700438838177794.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
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
- `JjkText` —— 20/21 个有
- `solarL_SaveImagesToZip` —— 20/21 个有
- `孤海注释` —— 20/21 个有
- `ResolutionSelector` —— 19/21 个有
- `EmptyFlux2LatentImage` —— 18/21 个有
- `PreviewImage` —— 10/21 个有
- `SkipLayerGuidanceDiTSimple` —— 8/21 个有
- `CR Text` —— 4/21 个有
- `CR Prompt Text` —— 3/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `JoinStringMulti` —— 3/21 个有
- `ModelSamplingAuraFlow` —— 3/21 个有
- `SeedNode` —— 3/21 个有
- `ImageBatch` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 21 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3.5 - 4.5 | 21 | 95% |
| 采样算法 | er_sde | - | 21 | 95% |
| 调度器 | beta | - | 21 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 1024 | 21 | 0% |
| 高度 | 80 | 80 - 1024 | 21 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，21 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3.5 - 4.5，21 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，21 个样本，一致性 95%
- 调度器 最常用 beta，21 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，21 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，21 个样本，取值分散，一致性仅 0%
- 高发问题（35/21 个样本）：Steps较低可能导致细节不足
