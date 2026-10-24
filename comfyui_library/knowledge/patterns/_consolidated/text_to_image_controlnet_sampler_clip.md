---
name: text_to_image_controlnet_sampler_clip
type: Text To Image
frequency: 20
level: strong
coverage: 0.883
common_nodes: [CLIPTextEncode, CR Apply ControlNet, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/SD1.5图生图+Canny真人转动漫_1927539264094113794.json, 图片生成/图生图/SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177.json, 图片生成/图生图/SD1.5图生图+DW真人转动漫_1927159529778139137.json, 图片生成/图生图/SD1.5图生图+PyraCanny室内_1927536286360571905.json, 图片生成/图生图/SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442.json, 图片生成/图生图/SD1.5图生图+TileSimple增多细节_1927531339803680769.json, 图片生成/图生图/SD1.5图生图+Tile细节增强_1927529405239681026.json, 图片生成/图生图/SD1.5图生图+animal pose真人转动漫_1927169591133503490.json, 图片生成/图生图/SD1.5图生图+canny风景_1927533289735610369.json, 图片生成/图生图/SD1.5图生图+dense pose真人转动漫_1927166776063459329.json, 图片生成/图生图/SD1.5图生图+media pipe-face mesh真人转动漫_1927164145626468353.json, 图片生成/图生图/SD1.5图生图+open pose真人转动漫_1927161870132662273.json, 图片生成/图生图/一键转绘卡通动漫人物_1925726820229156865.json, 图片生成/图生图/一键转绘卡通动漫儿童绘本动物_1925730885440868354.json, 图片生成/图生图/一键转绘油画风鎏金山水_1925720633903108097.json, 图片生成/图生图/一键转绘灵动山水室内_1925719183672168449.json, 图片生成/图生图/动漫转CG_1926806244302987266.json, 图片生成/图生图/真人转线稿_1926090759286509570.json, 图片生成/图生图/窗台桌面场景变幻_1926809920631640065.json, 图片生成/图生图/色彩变幻_1926088992847269889.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/SD1.5图生图+Canny真人转动漫_1927539264094113794.json、图片生成/图生图/SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177.json、图片生成/图生图/SD1.5图生图+DW真人转动漫_1927159529778139137.json、图片生成/图生图/SD1.5图生图+PyraCanny室内_1927536286360571905.json、图片生成/图生图/SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Apply ControlNet`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 19/20 个有
- `AIO_Preprocessor` —— 16/20 个有
- `ClipInterrogator` —— 16/20 个有
- `LoraLoaderModelOnly` —— 15/20 个有
- `VAELoader` —— 7/20 个有
- `WD14Tagger|pysssss` —— 4/20 个有
- `CannyEdgePreprocessor` —— 3/20 个有
- `DeepTranslatorTextNode` —— 1/20 个有
- `HEDPreprocessor` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 20 | 100% |
| 高度 | 1536 | 1536 - 1536 | 20 | 100% |
| 采样步数 | 30 | 25 - 30 | 20 | 92% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 20 | 100% |
| 采样算法 | dpmpp_2m | - | 20 | 100% |
| 调度器 | karras | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，20 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 25 - 30，20 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，20 个样本，一致性 100%
- 调度器 最常用 karras，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
