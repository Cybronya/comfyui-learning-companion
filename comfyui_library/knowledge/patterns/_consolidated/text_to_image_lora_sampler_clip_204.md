---
name: text_to_image_lora_sampler_clip_204
type: Text To Image
frequency: 9
level: strong
coverage: 0.879111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Image2.5直出PSD分层文件图层拆分图生图处理工具_2101375618482003969.json, 图片生成/图生图/Image2单张低至1分钱图生图处理生成工具_2101741318761439234.json, 图片生成/图生图/RH全能图片PRO官方稳定版｜图生图不出幺蛾子，海报制作靠得住_2099536861491453954.json, 图片生成/图生图/image2单张生成｜低至一毛图生图价格浮动直出_2091265327224152066.json, 图片生成/图生图/image2超值出图｜单张低至1分钱价格随市场浮动_2101512110328074241.json, 图片生成/图生图/全能图片G Image2.5图生图 多模式图像处理工具_2114070976534241281.json, 图片生成/图生图/全能图片G Image2.5图生图 高质量改图方案_2110368621951279106.json, 图片生成/图生图/全能图片PRO图生图官方稳定版 风格复刻构图可控_2099212184491479042.json, 图片生成/文生图/全能图片G2.5图生图高品质版处理工具_2100659592215744513.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Image2.5直出PSD分层文件图层拆分图生图处理工具_2101375618482003969.json、图片生成/图生图/Image2单张低至1分钱图生图处理生成工具_2101741318761439234.json、图片生成/图生图/RH全能图片PRO官方稳定版｜图生图不出幺蛾子，海报制作靠得住_2099536861491453954.json、图片生成/图生图/image2单张生成｜低至一毛图生图价格浮动直出_2091265327224152066.json、图片生成/图生图/image2超值出图｜单张低至1分钱价格随市场浮动_2101512110328074241.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

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
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 4/9 个有
- `RelayGPTImage2Generator` —— 3/9 个有
- `RH_RhartImageNProOfficialEdit` —— 2/9 个有
- `Text` —— 2/9 个有
- `SynVowPsdLayerComposer` —— 1/9 个有
- `SynVowTransparentAssetPromptGenerator` —— 1/9 个有
- `SynVowTransparentPngSavePreview` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
