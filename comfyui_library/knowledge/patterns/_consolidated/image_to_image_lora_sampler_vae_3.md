---
name: image_to_image_lora_sampler_vae_3
type: Image To Image
frequency: 21
level: moderate
coverage: 0.84881
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen换装_1972259814439055362.json, 图片生成/图生图/qwen真人转网红手办_3D_盲盒手办_效果堪比Naon 全能图片V1_1989295548085751810.json, 图片生成/图生图/ywt低价版2.0_2059997662291779585.json, 图片生成/图生图/ywt低价版3.0_2060024511612936194.json, 图片生成/图生图/ywt低价版4.0_2060256743405473793.json, 图片生成/图生图/ywt低价版5.0_2060394577848258561.json, 图片生成/图生图/【老金驿站】Qwen2509真人转彩绘动漫工作流_1980160554872508417.json, 图片生成/图生图/【老金驿站】Qwen2509镜头转换控制器工作流_1987167593591189505.json, 图片生成/图生图/千问Edit印花提取_1965114537508786178.json, 图片生成/图生图/千问qwen一键服装替换_万物迁移工作流_1997614568350396418.json, 图片生成/图生图/图片改变视角_2005454874915598337.json, 图片生成/图生图/图片视角转变_1989251290163187713.json, 图片生成/图生图/图片视角转变_1989550740198879233.json, 图片生成/图生图/图片视角转变_1991765325454716930.json, 图片生成/图生图/图片视角转变_2001990204246376449.json, 图片生成/图生图/图片视角转变_2016348615001772034.json, 图片生成/图生图/图片视角转变_2044301737418301442.json, 图片生成/图生图/图生图-视角转变_2041686193233989633.json, 图片生成/图生图/控制相机角度_1991030936403943426.json, 图片生成/图生图/视角转换（新版）_1991125652569174017.json, 图片生成/图生图/说话改图工作流大集合_1971841856017526785.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/qwen换装_1972259814439055362.json、图片生成/图生图/qwen真人转网红手办_3D_盲盒手办_效果堪比Naon 全能图片V1_1989295548085751810.json、图片生成/图生图/ywt低价版2.0_2059997662291779585.json、图片生成/图生图/ywt低价版3.0_2060024511612936194.json、图片生成/图生图/ywt低价版4.0_2060256743405473793.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 21 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 20/21 个有
- `UNETLoader` —— 20/21 个有
- `Image Comparer (rgthree)` —— 19/21 个有
- `ImageScaleToTotalPixels` —— 19/21 个有
- `PreviewImage` —— 16/21 个有
- `easy imageSize` —— 10/21 个有
- `RH_Nano_Banana_Image2Image` —— 5/21 个有
- `RH_RhartImageG2ImageToImage` —— 4/21 个有
- `TextEncodeQwenImageEdit` —— 4/21 个有
- `CR Text` —— 2/21 个有
- `UnetLoaderGGUF` —— 2/21 个有
- `ConditioningZeroOut` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `JWImageResizeByLongerSide` —— 1/21 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/21 个有
- `RH_ComfyFluxKontext` —— 1/21 个有
- `RH_Jimeng4_Image2Image` —— 1/21 个有
- `RH_Translator` —— 1/21 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 21 | 56% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 21 | 58% |
| 采样算法 | euler | - | 21 | 100% |
| 调度器 | simple | - | 21 | 90% |
| 重绘幅度 | 1 | 0.72 - 1 | 21 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，21 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，21 个样本
- 采样算法 最常用 euler，21 个样本，一致性 100%
- 调度器 最常用 simple，21 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.72 - 1，21 个样本，取值集中（一致性 88%）
- 高发问题（19/21 个样本）：Steps较低可能导致细节不足
