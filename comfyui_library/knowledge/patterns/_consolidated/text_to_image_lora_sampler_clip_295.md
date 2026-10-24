---
name: text_to_image_lora_sampler_clip_295
type: Text To Image
frequency: 6
level: strong
coverage: 0.8715
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Image2.5直出PSD分层文件图层拆分图生图处理工具_2101375618482003969.json, 图片生成/图生图/Image2单张低至1分钱图生图处理生成工具_2101741318761439234.json, 图片生成/图生图/InspyrenetRembg智能抠图 图生图一键去除背景_2094216339488600065.json, 图片生成/图生图/image2单张生成｜低至一毛图生图价格浮动直出_2091265327224152066.json, 图片生成/图生图/image2超值出图｜单张低至1分钱价格随市场浮动_2101512110328074241.json, 图片生成/文生图/全能图片G2.5图生图高品质版处理工具_2100659592215744513.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_295

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Image2.5直出PSD分层文件图层拆分图生图处理工具_2101375618482003969.json、图片生成/图生图/Image2单张低至1分钱图生图处理生成工具_2101741318761439234.json、图片生成/图生图/InspyrenetRembg智能抠图 图生图一键去除背景_2094216339488600065.json、图片生成/图生图/image2单张生成｜低至一毛图生图价格浮动直出_2091265327224152066.json、图片生成/图生图/image2超值出图｜单张低至1分钱价格随市场浮动_2101512110328074241.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `RelayGPTImage2Generator` —— 3/6 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 2/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `SynVowPsdLayerComposer` —— 1/6 个有
- `SynVowTransparentAssetPromptGenerator` —— 1/6 个有
- `SynVowTransparentPngSavePreview` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
