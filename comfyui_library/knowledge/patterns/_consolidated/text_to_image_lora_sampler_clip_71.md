---
name: text_to_image_lora_sampler_clip_71
type: Text To Image
frequency: 15
level: weak
coverage: 0.842333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, PreviewAny, ResizeImageMaskNode, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2081193864177733633.json, 图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2105591575370887170.json, 图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2108380827204800513.json, 图片生成/图生图/3-Krea2Turbo动漫真人3D互转 万能洗图 风格转绘V2 工作流-RH版_2092778942037057538.json, 图片生成/图生图/Krea2Turbo万能洗图V2｜风格转绘图生图RH版精修_2094742080018010114.json, 图片生成/图生图/Krea2Turbo万能洗图V2｜风格转绘图生图RH版精修_2095683831885029377.json, 图片生成/图生图/Krea2Turbo万能洗图V2｜风格转绘图生图RH版精修_2095692995998871553.json, 图片生成/图生图/Krea2Turbo动漫真人3D互转_万能洗图_风格转绘V2_工作流-RH版_2105591119143858177.json, 图片生成/图生图/Krea2Turbo动漫真人3D互转_万能洗图_风格转绘V2_工作流-RH版_2108380394591711234.json, 图片生成/图生图/Krea2Turbo动漫真人3D风格互转 万能洗图风格转绘_2098295680115765250.json, 图片生成/图生图/Krea2Turbo图生图风格转绘V2｜万能洗图精修_2094520552697458690.json, 图片生成/文生图/Krea2 Turbo 文生图利器｜风格参考巨物四视图V2升级版_2097881094573092866.json, 图片生成/文生图/Krea2Turbo四视图巨物｜风格参考文生图工作流V2_2093425905577316354.json, 图片生成/文生图/Krea2Turbo文生图V2工作流｜风格参考巨物美学四视图生成_2097751520233218050.json, 图片生成/文生图/风格参考巨物四视图｜Krea2Turbo文生图V2工作流_2093755784319553538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2081193864177733633.json、图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2105591575370887170.json、图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2108380827204800513.json、图片生成/图生图/3-Krea2Turbo动漫真人3D互转 万能洗图 风格转绘V2 工作流-RH版_2092778942037057538.json、图片生成/图生图/Krea2Turbo万能洗图V2｜风格转绘图生图RH版精修_2094742080018010114.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `ResizeImageMaskNode`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 12/15 个有
- `MuyeTextEditOutput` —— 12/15 个有
- `PrimitiveStringMultiline` —— 12/15 个有
- `easy stylesSelector` —— 12/15 个有
- `AILab_ImageCompare` —— 11/15 个有
- `AIO_Preprocessor` —— 11/15 个有
- `GetImageSize` —— 11/15 个有
- `LoadImage` —— 11/15 个有
- `PreviewImage` —— 11/15 个有
- `ResizeImagesByLongerEdge` —— 11/15 个有
- `JjkText` —— 9/15 个有
- `solarL_SaveImagesToZip` —— 9/15 个有
- `Krea2ControlApply` —— 8/15 个有
- `Krea2ControlImageEncode` —— 8/15 个有
- `Krea2ControlLoRALoader` —— 8/15 个有
- `VAEEncode` —— 8/15 个有
- `孤海注释` —— 7/15 个有
- `Fast Bypasser (rgthree)` —— 6/15 个有
- `SDXLEmptyLatentSizePicker+` —— 4/15 个有
- `ModelPatchLoader` —— 3/15 个有
- `ModelSamplingAuraFlow` —— 3/15 个有
- `ZImageFunControlnet` —— 3/15 个有
- `easy cleanGpuUsed` —— 3/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 4 | 15 | 48% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 45% |
| 采样算法 | er_sde | - | 15 | 60% |
| 调度器 | beta | - | 15 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 512 | 15 | 16% |
| 高度 | 80 | 80 - 512 | 15 | 16% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 54/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 4，15 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本，取值分散，一致性仅 45%
- 采样算法 最常用 er_sde，15 个样本，一致性 60%
- 调度器 最常用 beta，15 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 512，15 个样本，取值分散，一致性仅 16%
- 高度 中位数 80，观测区间 80 - 512，15 个样本，取值分散，一致性仅 16%
- 高发问题（54/15 个样本）：Steps较低可能导致细节不足
