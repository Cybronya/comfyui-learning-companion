---
name: text_to_image_lora_sampler_clip_200
type: Text To Image
frequency: 9
level: strong
coverage: 0.890778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/18个月宝宝睡衣产品套图｜居家场景模特产品展示6张图_2104489945556668418.json, 图片生成/图生图/1香2蕉2API图生图｜接口直连出图稳定，批量生产省心之选_2107359008972689410.json, 图片生成/图生图/BiRefNet商品主体抠图 图生图精准商品分割工具_2098695876263899138.json, 图片生成/图生图/BiRefNet商品主体抠图流｜电商产品图精细分离_2098710912726298625.json, 图片生成/图生图/G2.5全能图片编辑经济版 低成本图像处理方案_2098301672375283713.json, 图片生成/图生图/全能图片2.0_2k高清版｜图生图画质细节双在线_2105254608422658050.json, 图片生成/图生图/全能图片2.0图生图 多模式图像处理生成工具_2113728468147064833.json, 图片生成/图生图/全能图片2.0工作流，图生图高质量图像处理方案_2107521089378283521.json, 图片生成/图生图/姿态迁移工作流｜图生图姿势控制一键复刻动作_2100780774088855553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_200

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/18个月宝宝睡衣产品套图｜居家场景模特产品展示6张图_2104489945556668418.json、图片生成/图生图/1香2蕉2API图生图｜接口直连出图稳定，批量生产省心之选_2107359008972689410.json、图片生成/图生图/BiRefNet商品主体抠图 图生图精准商品分割工具_2098695876263899138.json、图片生成/图生图/BiRefNet商品主体抠图流｜电商产品图精细分离_2098710912726298625.json、图片生成/图生图/G2.5全能图片编辑经济版 低成本图像处理方案_2098301672375283713.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Gemini31Flash` —— 4/9 个有
- `LayerMask: BiRefNetUltraV2` —— 3/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/9 个有
- `RH_RhartImageG25SunburstImageToImage` —— 2/9 个有
- `ttN text` —— 2/9 个有
- `AspectRatioSelect` —— 1/9 个有
- `DWPreprocessor` —— 1/9 个有
- `Image Stitch` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_RhartImageG2ImageToImage_Batch` —— 1/9 个有
- `ResizeAndPadImage` —— 1/9 个有
- `StringConstantMultiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
