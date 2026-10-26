---
name: text_to_image_lora_sampler_clip_130
type: Text To Image
frequency: 12
level: strong
coverage: 0.8975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3人物三视图和场景图生成优化版V3工具-参考双图_2101865637562904577.json, 图片生成/图生图/Image-2.5九图图生图版本 多图编辑处理_2098304496907669505.json, 图片生成/图生图/InspyrenetRembg智能抠图 图生图一键去除背景_2094216339488600065.json, 图片生成/图生图/MiniMax H3人物三视图可生成场景图生图处理工具_2102137579343794177.json, 图片生成/图生图/Minimax H3人物三视图和场景图生成 超清优化版_2105125698879975425.json, 图片生成/图生图/Minimax H3人物三视图和场景图生成超清优化版 角色设定批量产出_2109367390558580737.json, 图片生成/图生图/openAI生图工作流｜图生图创意绘图模板直出_2097897249505374210.json, 图片生成/图生图/openAI生图工作流｜图生图图片生成处理_2097844315547594753.json, 图片生成/图生图/openAI生图工作流｜智能图生图创意绘制方案_2097898857920294913.json, 图片生成/图生图/上衣替换换衣服｜Image2服装替换展示图生图生成_2094802942401536001.json, 图片生成/图生图/人物三视图场景图｜Minimax H3超清优化版图生图_2092918394403250177.json, 图片生成/图生图/俯视图拆九宫格平视分镜横板｜全能图像G低价渠道，图生图分镜省时省力_2100441395935924225.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_130

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/H3人物三视图和场景图生成优化版V3工具-参考双图_2101865637562904577.json、图片生成/图生图/Image-2.5九图图生图版本 多图编辑处理_2098304496907669505.json、图片生成/图生图/InspyrenetRembg智能抠图 图生图一键去除背景_2094216339488600065.json、图片生成/图生图/MiniMax H3人物三视图可生成场景图生图处理工具_2102137579343794177.json、图片生成/图生图/Minimax H3人物三视图和场景图生成 超清优化版_2105125698879975425.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `RH_RhartImageG2ImageToImage` —— 10/12 个有
- `CR Prompt Text` —— 7/12 个有
- `CR Text Concatenate` —— 5/12 个有
- `KOOK_SaveJPGImage` —— 5/12 个有
- `EmptyImage` —— 1/12 个有
- `GuHaiAutoImageSplit` —— 1/12 个有
- `InspyrenetRembg` —— 1/12 个有
- `MaskPreview+` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/12 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
