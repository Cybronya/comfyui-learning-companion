---
name: text_to_image_lora_sampler_clip_73
type: Text To Image
frequency: 15
level: strong
coverage: 0.869133
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/VOSR2图像高清放大工作流_图片超分辨率增强_2101214595330433025.json, 图片生成/图生图/VOSR2图像高清放大工作流_图片超分辨率增强_2101452460052279297.json, 图片生成/图生图/VOSR2文字海报放大工作流，图生图高清保留文字细节不模糊_2102896144153145345.json, 图片生成/图生图/VOSR2文字海报放大工作流，图生图高清保留文字细节不模糊_2104740265851449345.json, 图片生成/图生图/VOSR2高保真高清放大工作流不脑部处理保留原始细节，图生图高清放大工具_2107574604486238209.json, 图片生成/图生图/VOSR2高保真高清放大工作流，不脑部处理保留原始细节_2106918565352919042.json, 图片生成/图生图/VOSR2高清放大方案，图生图画质增强超分一步到位_2110869502345961474.json, 图片生成/图生图/Vosr_2图像高清化神器｜10秒冲上4K分辨率，老素材直接救活_2099546801169854466.json, 图片生成/图生图/image2自用稳定版_2085450601940480001.json, 图片生成/图生图/全能图片CPT-Image-2.5官方稳定版，图生图全能处理_2111521414405775361.json, 图片生成/图生图/全能图片G-2.5图生图高品质版｜老图翻新不糊边，质感直接上一档_2099482216635129857.json, 图片生成/图生图/全能图片G_image2.5sunburst图生图｜图片模型直出，质感不掉档_2099476469230690305.json, 图片生成/图生图/文字高清修复工作流｜模糊文字一键变清晰｜图生图细节增强实用款_2112070421783863298.json, 图片生成/图生图/文字高清图生图修复，模糊字迹照片一键锐化变清晰_2112337165173743618.json, 数字人/数字人/图像高清放大工作流｜Vosr2数字人图片画质增强_2097525104493293570.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/VOSR2图像高清放大工作流_图片超分辨率增强_2101214595330433025.json、图片生成/图生图/VOSR2图像高清放大工作流_图片超分辨率增强_2101452460052279297.json、图片生成/图生图/VOSR2文字海报放大工作流，图生图高清保留文字细节不模糊_2102896144153145345.json、图片生成/图生图/VOSR2文字海报放大工作流，图生图高清保留文字细节不模糊_2104740265851449345.json、图片生成/图生图/VOSR2高保真高清放大工作流不脑部处理保留原始细节，图生图高清放大工具_2107574604486238209.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
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
- `PreviewImage` —— 11/15 个有
- `VOSR2ModelLoader` —— 11/15 个有
- `VOSR2Upscale` —— 11/15 个有
- `孤海注释` —— 11/15 个有
- `Image Comparer (rgthree)` —— 7/15 个有
- `EmptyImage` —— 6/15 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 3/15 个有
- `Int` —— 2/15 个有
- `PrimitiveInt` —— 2/15 个有
- `MuyeTextEditOutput` —— 1/15 个有
- `PDIMAGE_LongerSize` —— 1/15 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/15 个有
- `easy saveText` —— 1/15 个有
- `图像缩放范围孤海` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
