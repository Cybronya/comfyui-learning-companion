---
name: text_to_image_lora_sampler_clip_182
type: Text To Image
frequency: 9
level: strong
coverage: 0.903333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI图生图工作流｜上传参考图一键重绘出新图_2106598292065972225.json, 图片生成/图生图/BiRefNet商品主体抠图 图生图精准商品分割工具_2098695876263899138.json, 图片生成/图生图/BiRefNet商品主体抠图流｜电商产品图精细分离_2098710912726298625.json, 图片生成/图生图/RH DLSS5 Enhance降噪超分增强｜图生图高清放大一步到位，画质纯净耐看_2100502400904810497.json, 图片生成/图生图/图生图工作流多场景覆盖图生图处理高质量创作方案_2109402187142090753.json, 图片生成/图生图/图生图工作流多场景覆盖图生图处理高质量创作方案_2109751600679051265.json, 图片生成/图生图/图生图工作流，多场景覆盖图生图处理高质量创作方案_2106899977481052162.json, 图片生成/图生图/图生图工作流，多场景覆盖图生图处理高质量创作方案_2108735437991927809.json, 图片生成/图生图/姿态迁移工作流｜图生图姿势控制一键复刻动作_2100780774088855553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_182

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/AI图生图工作流｜上传参考图一键重绘出新图_2106598292065972225.json、图片生成/图生图/BiRefNet商品主体抠图 图生图精准商品分割工具_2098695876263899138.json、图片生成/图生图/BiRefNet商品主体抠图流｜电商产品图精细分离_2098710912726298625.json、图片生成/图生图/RH DLSS5 Enhance降噪超分增强｜图生图高清放大一步到位，画质纯净耐看_2100502400904810497.json、图片生成/图生图/图生图工作流多场景覆盖图生图处理高质量创作方案_2109402187142090753.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/9 个有
- `CLIPTextEncodeFlux` —— 5/9 个有
- `DF_Text_Box` —— 5/9 个有
- `DualCLIPLoader` —— 5/9 个有
- `JWImageResizeByLongerSide` —— 5/9 个有
- `VAEEncode` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `LayerMask: BiRefNetUltraV2` —— 3/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/9 个有
- `AspectRatioSelect` —— 1/9 个有
- `DWPreprocessor` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `RH_DLSS5Enhance` —— 1/9 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
