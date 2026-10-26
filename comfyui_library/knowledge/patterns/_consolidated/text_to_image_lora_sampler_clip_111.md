---
name: text_to_image_lora_sampler_clip_111
type: Text To Image
frequency: 13
level: strong
coverage: 0.868231
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/全能图片V2  全能图片2图生图｜低价渠道版API专用_2090407880527798273.json, 图片生成/图生图/全能图片V2.1图生图 高质量参考图生成_2109387867872129026.json, 图片生成/图生图/全能图片V2图生图官方版｜提示词优化稳定出图新手放心用_2106213567543472129.json, 图片生成/图生图/全能图片V2图生图官方稳定版提示词优化工作流，图生图处理方案_2106513907606188034.json, 图片生成/图生图/全能图片低成本生成｜单张一毛批量图生图处理_2093138619555995650.json, 图片生成/图生图/全能图片图像编辑低价版 云端RunningHub高效处理方案_2098125131506864129.json, 图片生成/图生图/全能图片基础版图生图处理生成工作流工具包_2101044518236811265.json, 图片生成/图生图/卡塔尔饰品海报一键生成｜图生图中东异域风情海报素材_2099160429791633409.json, 图片生成/图生图/双图服装替换工作流｜全能图片2官方稳定版_2095583561020698625.json, 图片生成/图生图/商用版人物介绍产品四宫格 全能图片2图生图排版_2094236619254616065.json, 图片生成/图生图/商用版全能图片2｜人物介绍产品四宫格图生图生成_2094355396973649921.json, 图片生成/图生图/超清优化人物三视图场景图｜Minimax H3图生图生成_2092718678612729857.json, 图片生成/文生图/H3人物三视图和场景图生成优化版V3工具_2100664259473657857.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/全能图片V2  全能图片2图生图｜低价渠道版API专用_2090407880527798273.json、图片生成/图生图/全能图片V2.1图生图 高质量参考图生成_2109387867872129026.json、图片生成/图生图/全能图片V2图生图官方版｜提示词优化稳定出图新手放心用_2106213567543472129.json、图片生成/图生图/全能图片V2图生图官方稳定版提示词优化工作流，图生图处理方案_2106513907606188034.json、图片生成/图生图/全能图片低成本生成｜单张一毛批量图生图处理_2093138619555995650.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
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
- `CR Prompt Text` —— 5/13 个有
- `RH_RhartImageG2ImageToImage` —— 5/13 个有
- `CR Text Concatenate` —— 4/13 个有
- `KOOK_SaveJPGImage` —— 4/13 个有
- `PreviewAny` —— 3/13 个有
- `PrimitiveStringMultiline` —— 3/13 个有
- `RH_RhartImageNG31FlashImageToImage` —— 3/13 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 3/13 个有
- `RHLLMChatNode` —— 2/13 个有
- `RelayBanana2ImageGenerator` —— 2/13 个有
- `RH_RhartImageNNb21ImageToImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
