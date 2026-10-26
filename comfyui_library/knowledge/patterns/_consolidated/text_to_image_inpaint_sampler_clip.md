---
name: text_to_image_inpaint_sampler_clip
type: Text To Image
frequency: 45
level: moderate
coverage: 0.819533
common_nodes: [AILab_QwenVL, BasicGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Flux2Scheduler, FluxKontextImageScale, GetImageSize, ImageConcatMulti, ImageToMask, KSampler, KSamplerSelect, LaMaInpainting, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, PreviewAny, PreviewImage, RMBG, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageSize, easy isMaskEmpty, easy positive]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/9dianshanghuanbeijing_2048710556697235457.json, 图片生成/反推提示词/9vhobmlvcvj_2059689781319258113.json, 图片生成/反推提示词/9xkgrvabhdn_2059685777801564161.json, 图片生成/图生图/F.2klein9b电商产品主图匹配融合场景_2053459372717690881.json, 图片生成/图生图/F.2klein9b电商产品主图自动匹配场景_2056057704258523138.json, 图片生成/图生图/F.2klein9b电商产品主图自动匹配场景_2057332439487438849.json, 图片生成/图生图/一键生成电商产品主图-自动匹配场景_2049344942828425217.json, 图片生成/图生图/一键生成电商产品主图-自动匹配场景_2050068752007475202.json, 图片生成/图生图/一键生成电商产品主图-自动匹配场景_2112492823684665345.json, 图片生成/图生图/一键生成电商产品主图-自动匹配场景_2112517045182099457.json, 图片生成/图生图/一键生成电商产品主图｜自动匹配场景背景省去修图功夫_2112885806460395522.json, 图片生成/图生图/一键自动匹配生成电商产品主图_2055193619866365953.json, 图片生成/图生图/主打电商产品主图-自动匹配场景2.0_2028658658082562049.json, 图片生成/图生图/产品与场景融合_2037060984275214338.json, 图片生成/图生图/产品主图场景-自动匹配_2057016552922370050.json, 图片生成/图生图/产品自动融进参考图（电商强推）_2028379243427667970.json, 图片生成/图生图/拍摄产品电商产品主图优化-自动匹配场景_2064680465268822017.json, 图片生成/图生图/普通产品生成电商产品主图-美化产品_2065409061193080834.json, 图片生成/图生图/电商-产品主图-自动融合场景_2104840229386539010.json, 图片生成/图生图/电商产品_指令局部调整_产品打光_自动匹配场景_2093952625644498945.json, 图片生成/图生图/电商产品_指令局部调整_产品打光_自动匹配场景_2096500560810827777.json, 图片生成/图生图/电商产品_指令局部调整_产品打光_自动匹配场景_2096806352957038594.json, 图片生成/图生图/电商产品一键替换背景_2029469103563481090.json, 图片生成/图生图/电商产品主图+自动匹配场景_2059183619977076738.json, 图片生成/图生图/电商产品主图-自动匹配场景-邻家AI大女孩_2044790283505766402.json, 图片生成/图生图/电商产品主图-自动匹配场景_2027466614496563202.json, 图片生成/图生图/电商产品主图-自动匹配场景_2028393041299513346.json, 图片生成/图生图/电商产品主图-自动匹配场景_2028630655378132993.json, 图片生成/图生图/电商产品主图-自动匹配场景_2029764410088099841.json, 图片生成/图生图/电商产品主图-自动匹配场景_2034523144861519873.json, 图片生成/图生图/电商产品主图-自动匹配场景_2043661191800692737.json, 图片生成/图生图/电商产品主图-自动匹配场景_2043875036150370305.json, 图片生成/图生图/电商产品主图-自动匹配场景_2044766999854714881.json, 图片生成/图生图/电商产品主图-自动匹配场景_2047114875184353282.json, 图片生成/图生图/电商产品主图-自动匹配场景_2048660104911790082.json, 图片生成/图生图/电商产品主图-自动匹配场景_2059162825695780866.json, 图片生成/图生图/电商产品主图-自动匹配场景_2069038760297324546.json, 图片生成/图生图/电商产品主图-自动匹配场景_2081032730095214593.json, 图片生成/图生图/电商产品主图-自动匹配场景_2085618874015379457.json, 图片生成/图生图/电商产品主图-自动匹配场景_2085626872557297666.json, 图片生成/图生图/电商产品主图自动匹配场景_2058527309212246017.json, 图片生成/图生图/电商产品主图自动匹配场景_2062015763363491842.json, 图片生成/图生图/电商产品主图融合_2062552090437832705.json, 图片生成/图生图/电商产品主图设计-自动匹配场景_2046601997306044417.json, 图片生成/图生图/电商产品图打光换背景 指令局部调整自动匹配场景_2094237962610503682.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 45 个 workflow 归纳得出（图片生成/反推提示词/9dianshanghuanbeijing_2048710556697235457.json、图片生成/反推提示词/9vhobmlvcvj_2059689781319258113.json、图片生成/反推提示词/9xkgrvabhdn_2059685777801564161.json、图片生成/图生图/F.2klein9b电商产品主图匹配融合场景_2053459372717690881.json、图片生成/图生图/F.2klein9b电商产品主图自动匹配场景_2056057704258523138.json…）

- **类型**：Text To Image
- **样本数**：45
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 45 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `FluxKontextImageScale`
- `GetImageSize`
- `ImageConcatMulti`
- `ImageToMask`
- `KSampler`
- `KSamplerSelect`
- `LaMaInpainting`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `PreviewAny`
- `PreviewImage`
- `RMBG`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageSize`
- `easy isMaskEmpty`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 44/45 个有
- `Image Comparer (rgthree)` —— 42/45 个有
- `LoraLoaderModelOnly` —— 36/45 个有
- `Int` —— 3/45 个有
- `JjkText` —— 2/45 个有
- `ShellAgentPluginOutputText` —— 2/45 个有
- `solarL_SaveImagesToZip` —— 2/45 个有
- `孤海注释` —— 2/45 个有
- `GetNode` —— 1/45 个有
- `ImageBatchMulti` —— 1/45 个有
- `ImageUpscaleWithModel` —— 1/45 个有
- `JWStringReplace` —— 1/45 个有
- `LongTextToList` —— 1/45 个有
- `PrimitiveStringMultiline` —— 1/45 个有
- `SetNode` —— 1/45 个有
- `ShowText|pysssss` —— 1/45 个有
- `SomethingToString` —— 1/45 个有
- `TT_img_enc` —— 1/45 个有
- `UpscaleModelLoader` —— 1/45 个有
- `easy float` —— 1/45 个有
- `easy forLoopEnd` —— 1/45 个有
- `easy forLoopStart` —— 1/45 个有
- `llama_cpp_instruct_adv` —— 1/45 个有
- `llama_cpp_model_loader` —— 1/45 个有
- `llama_cpp_parameters` —— 1/45 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 45 | 82% |
| 高度 | 512 | 80 - 512 | 45 | 82% |
| 采样步数 | 4 | 4 - 4 | 45 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 45 | 38% |
| 采样算法 | euler | - | 45 | 96% |
| 调度器 | simple | - | 45 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 45 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 47/45 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，45 个样本，取值集中（一致性 82%）
- 高度 中位数 512，观测区间 80 - 512，45 个样本，取值集中（一致性 82%）
- 采样步数 中位数 4，观测区间 4 - 4，45 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，45 个样本，取值分散，一致性仅 38%
- 采样算法 最常用 euler，45 个样本，一致性 96%
- 调度器 最常用 simple，45 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，45 个样本，取值集中（一致性 100%）
- 高发问题（47/45 个样本）：Steps较低可能导致细节不足
