---
name: image_to_image_lora_sampler_vae_6
type: Image To Image
frequency: 15
level: moderate
coverage: 0.848267
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI三视图V2加强版_2019234627726090241.json, 图片生成/图生图/Qwen Edit Plus编辑_1991862068640894977.json, 图片生成/图生图/Qwen edit 完美一致 （千问图像编辑）_1973229898254954497.json, 图片生成/图生图/Qwen_三视图_Edit_2509+双截棍+高清放大_1982510783135399938.json, 图片生成/图生图/qwen2511 图像编辑_2003679937800380418.json, 图片生成/图生图/三视图_1990616354715820033.json, 图片生成/图生图/三视图一键生成（极速版）_1973254506974679041.json, 图片生成/图生图/三视图一键生成（极速版）_2038779660036739073.json, 图片生成/图生图/人物三视图一键生成_2022510758566830081.json, 图片生成/图生图/千文2511 一键三视图 高还原度_1996588676169744385.json, 图片生成/图生图/千问2511 图像编辑 极速_2003680122718855170.json, 图片生成/图生图/巨日禄漫剧角色三视图+特写一键生成_优化排版_2008906093778444289.json, 图片生成/图生图/角色一键三视图_2003679888521478145.json, 图片生成/图生图/角色三视图_一键生成三视图_2019953527921057793.json, 图片生成/图生图/（漫剧）全角色视角_2044835050407075842.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/AI三视图V2加强版_2019234627726090241.json、图片生成/图生图/Qwen Edit Plus编辑_1991862068640894977.json、图片生成/图生图/Qwen edit 完美一致 （千问图像编辑）_1973229898254954497.json、图片生成/图生图/Qwen_三视图_Edit_2509+双截棍+高清放大_1982510783135399938.json、图片生成/图生图/qwen2511 图像编辑_2003679937800380418.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 15 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 14/15 个有
- `TextEncodeQwenImageEditPlus` —— 14/15 个有
- `easy cleanGpuUsed` —— 14/15 个有
- `ImageScaleBy` —— 13/15 个有
- `ImageUpscaleWithModel` —— 13/15 个有
- `UpscaleModelLoader` —— 13/15 个有
- `VAEEncodeTiled` —— 13/15 个有
- `NunchakuQwenImageDiTLoader` —— 12/15 个有
- `CR Latent Input Switch JK` —— 11/15 个有
- `PreviewImage` —— 11/15 个有
- `PrimitiveBoolean` —— 11/15 个有
- `QwenImageLatentAspectRatio` —— 11/15 个有
- `Image Comparer (rgthree)` —— 10/15 个有
- `RH_Translator` —— 10/15 个有
- `easy showAnything` —— 10/15 个有
- `Fast Groups Bypasser (rgthree)` —— 9/15 个有
- `DWPreprocessor` —— 8/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/15 个有
- `UNETLoader` —— 6/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/15 个有
- `ImageConcanate` —— 2/15 个有
- `ttN concat` —— 2/15 个有
- `AILab_QwenVL_Advanced` —— 1/15 个有
- `CR Text Concatenate` —— 1/15 个有
- `GetNode` —— 1/15 个有
- `SetNode` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `easy imageScaleDown` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 15 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 0.3 - 1 | 15 | 51% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，15 个样本
- 高发问题（32/15 个样本）：Steps较低可能导致细节不足
