---
name: image_to_image_sampler_clip_unet_7
type: Image To Image
frequency: 23
level: weak
coverage: 0.923043
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Moss Image SFT 重绘洗图｜文生图｜自动反推提示词_2113926001603465218.json, 图片生成/反推提示词/Moss Image SFT 重绘洗图｜自动反推提示词_2112895526298537985.json, 图片生成/图生图/F2_klein图洗图_2056009934218768386.json, 图片生成/图生图/F2_klein图洗图_2056577800190119938.json, 图片生成/图生图/Flux2-Klein-单图编辑 （转真实lora）_2091149910098927618.json, 图片生成/图生图/Flux2-Klein-单图编辑_2087938968968060930.json, 图片生成/图生图/Flux2-Klein-多图编辑_2087940335677825026.json, 图片生成/图生图/FluxKlein白模建筑渲染参考图_2055240069711187969.json, 图片生成/图生图/FluxKlein白模建筑渲染参考图_2059528047891673089.json, 图片生成/图生图/FluxKlein白模建筑渲染参考图_2059824343596756993.json, 图片生成/图生图/FluxKlein白模建筑渲染参考图风格_2064561651784970241.json, 图片生成/图生图/Klein完美一致性分镜图制作_2021413605844979714.json, 图片生成/图生图/Moss Image SFT 重绘洗图｜自动反推提示词_2113063852601602050.json, 图片生成/图生图/Moss Image SFT 重绘洗图｜自动反推提示词_2113091690352435201.json, 图片生成/图生图/工业级产品精修Flux2-klein_2018881806765920258.json, 图片生成/图生图/扩图-Kelin 无痕扩图 真实自然_2070011625867927553.json, 图片生成/图生图/扩图-Kelin_2031616716182134786.json, 图片生成/图生图/扩图-Kelin_2033562314321960961.json, 图片生成/图生图/扩图-Klein_2034187314091528194.json, 图片生成/图生图/扩图-Klein_2035293200839090178.json, 图片生成/图生图/扩图-Klein_2039522371379400706.json, 图片生成/图生图/蒜香卡普-Klein-9b_ 扩图-亚秒级无缝扩图_2034222233765289986.json, 图片生成/图生图/超细节-工业级产品精修_2068953091722010626.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/反推提示词/Moss Image SFT 重绘洗图｜文生图｜自动反推提示词_2113926001603465218.json、图片生成/反推提示词/Moss Image SFT 重绘洗图｜自动反推提示词_2112895526298537985.json、图片生成/图生图/F2_klein图洗图_2056009934218768386.json、图片生成/图生图/F2_klein图洗图_2056577800190119938.json、图片生成/图生图/Flux2-Klein-单图编辑 （转真实lora）_2091149910098927618.json…）

- **类型**：Image To Image
- **样本数**：23
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 21/23 个有
- `EmptyFlux2LatentImage` —— 19/23 个有
- `Image Comparer (rgthree)` —— 18/23 个有
- `ReferenceLatent` —— 17/23 个有
- `Int` —— 10/23 个有
- `LoraLoaderModelOnly` —— 10/23 个有
- `ConditioningZeroOut` —— 9/23 个有
- `FillMaskWithColor` —— 7/23 个有
- `ImagePadForOutpaint` —— 7/23 个有
- `Float` —— 6/23 个有
- `llama_cpp_instruct_adv` —— 4/23 个有
- `llama_cpp_model_loader` —— 4/23 个有
- `孤海注释` —— 4/23 个有
- `CR Prompt Text` —— 2/23 个有
- `ColorMatch` —— 1/23 个有
- `easy promptLine` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 50 | 23 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 23 | 25% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 23 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 50，23 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，23 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，23 个样本，取值集中（一致性 83%）
- 高发问题（19/23 个样本）：Steps较低可能导致细节不足
